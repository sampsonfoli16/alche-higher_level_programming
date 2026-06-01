#!/usr/bin/env python3
"""
Web server with one redirect
"""
from flask import Flask, redirect
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """
    Root - redirect to /redirected with 301
    """
    return redirect("http://localhost:5050/redirected", code=301)

@app.route("/redirected", strict_slashes=False)
def redirected():
    """
    /redirected - final destination
    """
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
