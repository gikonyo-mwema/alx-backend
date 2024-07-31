#!/usr/bin/env python3
"""
Flask Application
This module sets up a simple Flask application with one route.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content for the root route.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
