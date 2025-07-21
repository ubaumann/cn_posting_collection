import os
import logging
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
KEY_DIRECTORY = Path(".keys/")


def get_name() -> str:
    return os.getenv("APP_NAME", None)


def get_key() -> str | None:
    account = os.getenv("APP_ACCOUNT", None)
    if account:
        try:
            key_file = KEY_DIRECTORY / account
            with key_file.open() as fp:
                return fp.readline()
        except IOError as exc:
            logger.warning("Could not read file %s. Error: %s", key_file, exc)
    return None


if __name__ == "__main__":
    app_name = get_name()
    api_key = get_key()
    with CONFIG_FILE.open("w") as fp:
        if app_name:
            fp.write(
                f'[app.{app_name}]\ncommand = "posting --collection . --env .env"\n\n'
            )
        if api_key:
            fp.write(f'[account]\napi_key = "{api_key}"\n')

    app(["-e", "local", "-c", f"{CONFIG_FILE}"])
