"""conftest: root level conftest file for pytest.

Used for defining fixtures and other things that need to be available in all tests.
"""
from pathlib import Path
from typing import Optional

import pytest
from flask import Blueprint
from flask.testing import FlaskClient

from app.web.factory import create_app


def get_and_decode(
    client: FlaskClient,
    url: str,
    query_string: Optional[dict] = None,
    status_code: int = 200,
    follow_redirects: bool = True,
    write_file: bool = False,
) -> str:
    """GET a url, assert its status code and return decoded data"""
    response = client.get(
        url, query_string=query_string, follow_redirects=follow_redirects
    )
    html = response.data.decode()
    # Can write to file for debugging
    if write_file:  # pragma: no cover
        tmp_dir = Path(__file__).parent / "tmp"
        tmp_dir.mkdir(exist_ok=True)
        tmp_file = tmp_dir / "html.html"
        tmp_file.write_text(html)
    assert response.status_code == status_code
    return html


@pytest.fixture
def client() -> FlaskClient:
    """Create a fresh flask client for a function"""
    app = create_app()
    with app.test_client() as client:
        ctx = app.app_context()
        ctx.push()
        yield client
        ctx.pop()


test_bp = Blueprint("test", __name__)


@test_bp.route("/", methods=["GET"])
def failing_route() -> None:
    """A test route that raises an error."""
    raise RuntimeError("Fake error")


@pytest.fixture
def client_with_failing_route() -> FlaskClient:
    """Create a Flask app with a failing route"""
    app = create_app()
    app.register_blueprint(test_bp, url_prefix="/test-error")
    with app.test_client() as client:
        ctx = app.app_context()
        ctx.push()
        yield client
        ctx.pop()
