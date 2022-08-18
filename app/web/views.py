"""views: Flask views for the transit_routes routes"""
from typing import Optional

from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.exceptions import HTTPException

from app.web.globals import FlaskResponse
from app.web.utils import get_routes_from_api, get_stops_from_api

# In a more complex app, we would have a range of blueprints for different routes.
router = Blueprint("all", __name__)


@router.route("/", methods=["GET"])
def index() -> FlaskResponse:
    """Redirect homepage to /routes"""
    return redirect(url_for("all.list_routes"))


@router.route("/routes/", methods=["GET"])
def list_routes(stop: Optional[str] = None) -> FlaskResponse:
    """This view lists all routes from the transit API for a given stop.

    If no stop is provided, it lists all routes.
    On HTML load, an HTMX request will trigger the render_routes_table function
    to load the routes table asynchronously (for improved speed and improved UX).
    """
    stop = request.args.get("stop")
    return render_template("routes.html", stop=stop)


@router.route("/routes-table", methods=["GET"])
def render_routes_table(stop: Optional[str] = None) -> FlaskResponse:
    """Render the routes table for all routes of a given stop.

    If no stop is provided, render the routes table for all stops.
    """
    stop = request.args.get("stop")
    return render_template(
        "routes_table.html", routes=get_routes_from_api(stop), stop=stop
    )


@router.route("/stops/", methods=["GET"])
def list_stops(route: Optional[str] = None) -> FlaskResponse:
    """This view lists all stops from the transit API for a given route.

    If no route is provided, it lists all stops.
    On HTML load, an HTMX request will trigger the render_stops_table function
    to load the routes table asynchronously (for improved speed and improved UX).
    """
    route = request.args.get("route")
    return render_template("stops.html", route=route)


@router.route("/stops-table", methods=["GET"])
def render_stops_table(route: Optional[str] = None) -> FlaskResponse:
    """Render the stops table for all stops of a given route.

    If no route is provided, render the stops table for all routes.
    """
    route = request.args.get("route")
    return render_template(
        "stops_table.html", stops=get_stops_from_api(route), route=route
    )


# Error handlers
@router.app_errorhandler(404)
def error_404(error: HTTPException) -> FlaskResponse:
    """Error for pages not found."""
    default = (
        "The requested URL was not found on the server. "
        "If you entered the URL manually please check your spelling and try again."
    )
    if error.description == default:
        error.description = "Oops! The page you requested was not found."
    return render_template("all_errors.html", error=error), 404


@router.app_errorhandler(500)
def error_500(error: HTTPException) -> FlaskResponse:
    """Error for pages not found."""
    default = (
        "The server encountered an internal error and was unable to complete your "
        "request. Either the server is overloaded or there is an error in the application."
    )
    if error.description == default:
        error.description = "Something went wrong. It's not you, it's us..."
    return render_template("all_errors.html", error=error), 500
