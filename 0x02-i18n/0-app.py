#!/usr/bin/env python3
"""
Flask Application
This module sets up a simple Flask application with one route.
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content for the root route.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
