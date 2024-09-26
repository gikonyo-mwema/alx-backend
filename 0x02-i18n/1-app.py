#!/usr/bin/env python3
"""
Flask Application with Babel for i18n
This module stes up a simple Flask application with internatinalization
support
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Configuration class for the Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content for the root route.

    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
