"""Minimal Flask application setup for the SQLAlchemy assignment."""
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# These extension instances are shared across the app and models
# so that SQLAlchemy can bind to the application context when the
# factory runs.
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    """Application factory used by Flask and the tests.

    The optional ``test_config`` dictionary can override settings such as
    the database URL to keep student tests isolated.
    """

    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here so SQLAlchemy is aware of them before migrations
    # or ``create_all`` run. Students will flesh these out in ``models.py``.
    import models  # noqa: F401

    @app.route("/")
    def index():
        """Simple sanity check route."""

        return jsonify({"message": "Welcome to the Flask + SQLAlchemy assignment"})

    @app.route("/users", methods=["GET", "POST"])
    def users():
        """List or create users.

        TODO: Students should query ``User`` objects, serialize them to JSON,
        and handle incoming POST data to create new users.
        """

        return (
            jsonify({"message": "TODO: implement user listing/creation"}),
            501,
        )

    @app.route("/posts", methods=["GET", "POST"])
    def posts():
        """List or create posts.

        TODO: Students should query ``Post`` objects, include user data, and
        allow creating posts tied to a valid ``user_id``.
        """

        return (
            jsonify({"message": "TODO: implement post listing/creation"}),
            501,
        )

    return app


# Expose a module-level application for convenience with certain tools
app = create_app()


if __name__ == "__main__":
    # Running ``python app.py`` starts the development server.
    app.run(debug=True)
