import os
import logging
import httpx
from pathlib import Path
from textual_web.environment import ENVIRONMENTS, Environment

api_server = os.getenv("API_SERVER", "127.0.0.1:8080")
ENVIRONMENTS["local"] = Environment(
    name="local",
    api_url=f"ws://{api_server}/api/",
    url=f"ws://{api_server}/app-service/",
)
from textual_web.cli import app

logger = logging.getLogger()

CONFIG_FILE = Path("ganglion.toml")
KEY_LOCATION = os.getenv("KEY_LOCATION", ".keys/")
DECRYPTION_KEY = os.getenv("DECRYPTION_KEY", None)
ACCOUNT = os.getenv("APP_ACCOUNT", None)


def get_name() -> str:
    return os.getenv("APP_NAME", None)


def get_key() -> str | None:
    if ACCOUNT:
        try:
            if KEY_LOCATION.startswith("http"):
                key_url = f"{KEY_LOCATION}/{ACCOUNT}"
                response = httpx.get(key_url)
                response.raise_for_status()
                key = response.text.strip()
            else:
                key_file = Path(KEY_LOCATION) / ACCOUNT
                with key_file.open() as fp:
                    key = fp.readline()
            if DECRYPTION_KEY:
                from cryptography.fernet import Fernet

                fernet = Fernet(DECRYPTION_KEY)
                return fernet.decrypt(key.encode()).decode()
            return key.strip()
        except IOError as exc:
            logger.warning("Could not read file %s. Error: %s", key_file, exc)
        except httpx.HTTPError as exc:
            logger.warning("Could not read URL %s. Error: %s", key_url, exc)
    return None


if __name__ == "__main__":
    app_name = get_name()
    api_key = get_key()
    if not api_key and ACCOUNT:
        logger.error(
            "No API key found. Please set the APP_ACCOUNT/KEY_LOCATION environment variables."
        )
        exit(1)
    with CONFIG_FILE.open("w") as fp:
        if app_name:
            fp.write(
                f'[app.{app_name}]\ncommand = "posting --collection . --env .env"\n\n'
            )
        if api_key:
            fp.write(f'[account]\napi_key = "{api_key}"\n')

    app(["-e", "local", "-c", f"{CONFIG_FILE}"])
