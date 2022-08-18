"""utils: Utility functions for the transit_routes web app"""
from typing import Optional

import requests

from app.web.globals import TRANSIT_API_ENDPOINT
from app.web.models import RouteModel, StopModel

TRANSIT_ROUTES_ENDPOINT = f"{TRANSIT_API_ENDPOINT}/routes"
TRANSIT_STOPS_ENDPOINT = f"{TRANSIT_API_ENDPOINT}/stops"


def get_attrs(data: dict) -> dict:
    """Get attributes from a data object dictionary from the transit api"""
    return data.get("attributes", {})


def get_routes_from_api(stop: Optional[str]) -> list:
    """Get all routes from the transit api"""
    if stop:
        url = f"{TRANSIT_ROUTES_ENDPOINT}?filter[stop]={stop}"
    else:
        url = TRANSIT_ROUTES_ENDPOINT
    response = requests.get(url)
    routes_data = response.json().get("data")
    return [
        RouteModel(
            id=route.get("id"),
            long_name=get_attrs(route).get("long_name"),
            short_name=get_attrs(route).get("short_name"),
            description=get_attrs(route).get("description"),
            direction=tuple(get_attrs(route).get("direction_names", [])),
            destinations=tuple(get_attrs(route).get("direction_destinations", [])),
        )
        for route in routes_data
    ]


def get_stops_from_api(route: Optional[str]) -> list:
    """Get all stops from the transit api"""
    if route:
        url = f"{TRANSIT_STOPS_ENDPOINT}?filter[route]={route}"
    else:
        url = TRANSIT_STOPS_ENDPOINT
    response = requests.get(url)
    stops_data = response.json().get("data")
    return [
        StopModel(
            id=stop.get("id"),
            name=get_attrs(stop).get("name"),
            municipality=get_attrs(stop).get("municipality"),
            description=get_attrs(stop).get("description"),
            address=get_attrs(stop).get("address"),
            lat_long=(
                get_attrs(stop).get("latitude"),
                get_attrs(stop).get("longitude"),
            ),
        )
        for stop in stops_data
    ]
