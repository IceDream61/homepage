import os
import markdown
from flask import request, Flask, render_template, redirect, url_for
from lib.md import makesure_html_exists
from lib.log import logging
from lib.auth import get_auth_status

activity = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="html")


@activity.route("/activity/questionnaire/result/<i>")
def questionnaire_result_i(i):
    content = get_auth_status(request.cookies)
    content["filename"] = f"activity/questionnaire_result_{i}"
    makesure_html_exists(f"questionnaire_result_{i}", "activity")
    return render_template("activity/questionnaire_result_i.html", **content)


@activity.route("/activity")
def index():
    content = get_auth_status(request.cookies)
    content["filename"] = "activity/index"
    makesure_html_exists("index", "activity")
    return render_template("activity/index.html", **content)
