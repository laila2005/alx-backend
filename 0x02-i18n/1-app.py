#!/usr/bin/env python3
"""
Flask application for i18n project.
Sets up Babel configuration with English and French support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for the Flask app.

    It defines the available languages,
    default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Handle the root route.

    Returns:
        Rendered HTML template for index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
