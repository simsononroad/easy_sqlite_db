from flask import Flask, render_template, redirect, url_for, jsonify


def start_website(port=5000):
    app = Flask(__name__)
    @app.route("/")
    def index():
        return render_template("index.html")
    return app
