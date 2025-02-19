from flask import Flask, render_template, redirect, url_for, jsonify

def start_website(port=5000):
    app = Flask(__name__)
    
    @app.route("/")
    def index():
        return "<h1>Hello World</h1>"
    
    if __name__=="_main__":
        app.run(port=port)