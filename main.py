"""run.py

This is the main file called to run the flask application
"""
from app.web.factory import create_app

if __name__ == "__main__":  # pragma: no cover
    app = create_app()
    app.run()
