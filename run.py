import os
from textual_web.environment import ENVIRONMENTS, Environment
api_server = os.getenv("API_SERVER", "127.0.0.1:8080")
ENVIRONMENTS["local"] = Environment(
        name="local",
        api_url=f"ws://{api_server}/api/",
        url=f"ws://{api_server}/app-service/",
    )
from textual_web.cli import app


if __name__ == "__main__":
    app(["-e", "local", "-r", "posting --collection . --env .env"])
