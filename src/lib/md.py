import os
import time
import markdown
from lib.log import logging

MD_FOLDER = "static/md"
HTML_FOLDER = "html/md_content"

if not os.path.exists(HTML_FOLDER):
    os.mkdir(HTML_FOLDER)


def need_update(md_fp, html_fp):
    if not os.path.exists(html_fp):
        return True
    if os.stat(md_fp).st_ctime > os.stat(html_fp).st_mtime:
        return True
    return False


def makesure_html_exists(filename, folder=""):
    logging.debug(f"convert: {filename} in {folder}")
    md_fp = os.path.join(MD_FOLDER, folder, f"{filename}.md")
    html_fp = os.path.join(HTML_FOLDER, folder, f"{filename}.html")

    if need_update(md_fp, html_fp):
        logging.debug(f"convert: {md_fp} --> {html_fp} ing")
        markdown.markdownFromFile(input=md_fp, output=html_fp, encoding="utf-8", extensions=["tables"])
        logging.info(f"convert: {md_fp} --> {html_fp}")
