from flask import request, Flask, render_template, redirect
from lib.log import logging
from lib.auth import get_auth_status, do_the_login, do_the_logout

main = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="html")


@main.route("/login", methods=["POST"])
def login():
    """
    login (or register)
    """
    username = request.form["nick_name"]
    password = request.form["password"]
    status, action, token = do_the_login(username, password)
    resp = redirect(request.referrer)
    resp.set_cookie("status", str(status))
    resp.set_cookie("action", action)
    resp.set_cookie("token", token)
    return resp


@main.route("/logout", methods=["POST"])
def logout():
    """
    logout
    """
    token = request.cookies.get("token", None)
    do_the_logout(token)
    resp = redirect(request.referrer)
    resp.delete_cookie("status")
    resp.delete_cookie("action")
    resp.delete_cookie("token")
    return resp


@main.route("/main")
def index():
    content = get_auth_status(request.cookies)
    return render_template("main.html", **content)
