#!/usr/bin/env python3
"""
Web server with five redirects and multiple status codes
"""
from flask import Flask, redirect
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """
    Root - redirect to /r1 with 301
    """
    return redirect("http://localhost:5050/r1", code=301)

@app.route("/r1", strict_slashes=False)
def r1():
    """
    /r1 - redirect to /r2 with 302
    """
    return redirect("http://localhost:5050/r2", code=302)

@app.route("/r2", strict_slashes=False)
def r2():
    """
    /r2 - redirect to /r3 with 303
    """
    return redirect("http://localhost:5050/r3", code=303)

@app.route("/r3", strict_slashes=False)
def r3():
    """
    /r3 - redirect to /r4 with 304
    """
    return redirect("http://localhost:5050/r4", code=304)

@app.route("/r4", strict_slashes=False)
def r4():
    """
    /r4 - redirect to /r5 with 307
    """
    return redirect("http://localhost:5050/r5", code=307)

@app.route("/r5", strict_slashes=False)
def r5():
    """
    /r5 - final destination
    """
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
