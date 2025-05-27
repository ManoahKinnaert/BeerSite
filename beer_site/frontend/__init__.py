from flask import Blueprint, render_template

front_bp = Blueprint("frontend", __name__, static_folder="static", template_folder="templates",
                     static_url_path="/frontend/static")

@front_bp.route("/")
def home():
    return render_template("home.html")

@front_bp.route("/paper")
def paper():
    return render_template("oc_paper.html")

@front_bp.route("/chat_with_beer")
def chat():
    return render_template("chat.html")

@front_bp.route("/gallery")
def gallery():
    return render_template("gallery.html")
