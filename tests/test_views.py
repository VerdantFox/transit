"""text_views: functional tests for the app.web.views module.

Note we do not mock calls to the external API here. This has the advantage of
testing that the external API integrates correctly with our app.
It has the following disadvantages:
1. The API could go down.
2. The API could change.
3. Calls to the API are slower than mocking them, especially for broad scope calls.
I believe the advantages outweigh the disadvantages.
"""
from flask.testing import FlaskClient

from tests.conftest import get_and_decode


def test_page_not_found(client: FlaskClient) -> None:
    """Test that a 404 redirects to page not found page."""
    html = get_and_decode(client, "/fake-page", status_code=404)
    assert "Oops! The page you requested was not found." in html


def test_server_error(client_with_failing_route: FlaskClient) -> None:
    """Test that a 500 redirects to server error page."""
    client = client_with_failing_route
    html = get_and_decode(client, "/test-error/", status_code=500)
    assert "Something went wrong." in html


def test_index_redirect(client: FlaskClient) -> None:
    """Test that the index page redirects to the routes page."""
    get_and_decode(client, "/", follow_redirects=False, status_code=302)
    html = get_and_decode(client, "/")
    assert "All routes" in html


def test_routes_all(client: FlaskClient) -> None:
    """Test that the routes view works."""
    html = get_and_decode(client, "/routes")
    assert "All routes" in html
    assert '<div hx-get="/routes-table"' in html


def test_routes_with_stop(client: FlaskClient) -> None:
    """Test that the routes view works with a stop."""
    valid_stop = "4230"
    html = get_and_decode(client, "/routes", query_string={"stop": valid_stop})
    assert "All routes for the 4230 stop" in html
    assert '<div hx-get="/routes-table?stop=4230"' in html


def test_routes_table_all(client: FlaskClient) -> None:
    """Test that the routes table view works."""
    html = get_and_decode(client, "/routes-table")
    assert "<table" in html
    assert '<td><a href="/stops/?route=Red">Red</a></td>' in html


def test_routes_table_valid_stop(client: FlaskClient) -> None:
    """Test that the routes table view works with a valid stop."""
    valid_stop = "4230"
    html = get_and_decode(client, "/routes-table", query_string={"stop": valid_stop})
    assert "<table" in html
    assert '<td><a href="/stops/?route=238">238</a></td>' in html


def test_routes_table_invalid_stop(client: FlaskClient) -> None:
    """Test that the routes table view works with an invalid stop."""
    invalid_stop = "fake-stop"
    html = get_and_decode(client, "/routes-table", query_string={"stop": invalid_stop})
    assert "<table" in html
    assert "<td>" not in html


def test_stops_all(client: FlaskClient) -> None:
    """Test that the stops view works."""
    html = get_and_decode(client, "/stops")
    assert "All stops" in html
    assert '<div hx-get="/stops-table"' in html


def test_stops_with_route(client: FlaskClient) -> None:
    """Test that the stops view works with a route."""
    valid_route = "Red"
    html = get_and_decode(client, "/stops", query_string={"route": valid_route})
    assert "All stops for the Red route" in html
    assert '<div hx-get="/stops-table?route=Red"' in html


def test_stops_table_all(client: FlaskClient) -> None:
    """Test that the stops table view works."""
    html = get_and_decode(client, "/stops-table")
    assert "<table" in html
    assert '<td><a href="/routes/?stop=4230">4230</a></td>' in html


def test_stops_table_valid_route(client: FlaskClient) -> None:
    """Test that the stops table view works with a valid route."""
    valid_route = "Red"
    html = get_and_decode(
        client, "/stops-table", query_string={"route": valid_route}, write_file=True
    )
    assert "<table" in html
    assert '<td><a href="/routes/?stop=place-alfcl">place-alfcl</a></td>' in html


def test_stops_table_invalid_route(client: FlaskClient) -> None:
    """Test that the stops table view works with an invalid route."""
    invalid_route = "fake-route"
    html = get_and_decode(client, "/stops-table", query_string={"route": invalid_route})
    assert "<table" in html
    assert "<td>" not in html
