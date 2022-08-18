"""globals: App wide global variables"""
from pathlib import Path
from typing import Union

from werkzeug.wrappers import Response

# Type hint globals
FlaskResponse = Union[str, Response]

# Paths
APP_PATH = Path(__file__).parents[1]
PROJECT_ROOT_PATH = APP_PATH.parent
STATIC_PATH = APP_PATH.joinpath("static")
TEMPLATE_PATH = APP_PATH.joinpath("templates")

TRANSIT_API_ENDPOINT = "https://api-v3.mbta.com/"
