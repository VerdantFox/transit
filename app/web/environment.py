"""File for getting environment variables."""
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuration settings for the Transit App

    These settings are loaded automatically from the environment.
    These settings are first loaded from an environment file.
    By default, that file is `.env.dev`. That file can be overwritten to anything
    (typically `.env` though) with the environment variable `ENV_FILE`
    (e.g. `export ENV_FILE=.env`). The settings from the environment file
    are then overwritten by any actual environment variables found.
    Settings can be loaded from CAPITALIZED_ENVIRONMENT_VARIABLES with the same
    name as their lower_case attributes, defined below.
    """

    secret_key: str

    class Config:
        """Configuration for the parent class."""

        extra = "forbid"
        env_file = os.environ.get("ENV_FILE", ".env.dev")
        env_file_encoding = "utf8"


settings = Settings()
