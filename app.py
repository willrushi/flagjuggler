from math import remainder
import flagjuggler
from flask import Flask, render_template, request
import json

app = Flask(__name__, static_url_path='', static_folder='static')

challenges = ["challenge1", "challenge2", "challenge3"]

@app.route("/")
def index():
    if not request.cookies.get("username"):
        return render_template("login.html")
    else:
        return render_template("index.html", challenges=challenges)

@app.route("/start_challenge", methods=["POST"])
def start_challenge():
    challenge_name = request.form.get("challenge_name")
    username = request.cookies.get("username")

    if not username or not challenge_name:
        return {"success": False, "error": "Missing username or challenge name"}
    
    port = flagjuggler.create_container(challenge_name, username, 8000)

    if port == -1:
        return {"success": False, "error": "Error creating container"}

    return {"success": True, "port": port}

@app.route("/stop_challenge", methods=["POST"])
def stop_challenge():
    challenge_name = request.form.get("challenge_name")
    username = request.cookies.get("username")

    if not username or not challenge_name:
        return {"success": False, "error": "Missing username or challenge name"}
    
    ret = flagjuggler.kill_container(challenge_name, username)

    if not ret:
        return {"success": False, "error": "Error destroying container"}

    return {"success": True}

@app.route("/challenge_active", methods=["POST"])
def check_challenge_active():
    challenge_name = request.form.get("challenge_name")
    username = request.cookies.get("username")

    if not username or not challenge_name:
        return {"success": False, "error": "Missing username or challenge name"}
    
    port = flagjuggler.container_exists(challenge_name, username)

    return {"success": True, "port": port}