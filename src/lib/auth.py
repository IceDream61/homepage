import os
import time
import datetime
import hashlib
from lib.log import logging
from lib.data_base import set_filedata, get_filedata, has_filedata, is_filedata, del_filedata


USERS_FILENAME = "users"
TOKENS_FILENAME = "tokens"
TOKEN_ALIVE_TIMEINTERVAL = 12 * 3600  # 12小时后登录超时


def has_user(username):
    return has_filedata(USERS_FILENAME, username)


def is_user(username, mp):
    is_filedata(USERS_FILENAME, username, mp)


def add_user(username, mp):
    set_filedata(USERS_FILENAME, username, mp)


def add_token(username, token):
    set_filedata(
        TOKENS_FILENAME,
        token,
        {
            "username": username,
            "timestamp": time.mktime(time.localtime(time.time())),
        },
    )


def make_token(username):
    token = str(hashlib.sha1(os.urandom(24)).hexdigest())
    add_token(username, token)
    return token


def calculate_md5(username, password):
    # 当前策略：前端计算md5传输过来，后端再加对每个人都不同的盐
    m = hashlib.md5()
    m.update((password + username + "cbzz!").encode("utf-8"))
    return m.hexdigest()


def do_the_login(username, password):
    mp = calculate_md5(username, password)
    if not has_user(username):
        add_user(username, mp)
        return True, "Register", make_token(username)
    elif is_user(username, mp):
        return True, "Login", make_token(username)
    else:
        return False, "Login", ""


def is_alive(ts):
    dt = datetime.datetime.utcfromtimestamp(ts)
    dt_now = datetime.datetime.now()
    return (dt_now - dt).seconds < TOKEN_ALIVE_TIMEINTERVAL


def search_token(token):
    value = get_filedata(TOKENS_FILENAME, token)
    if value and is_alive(value["timestamp"]):
        return value["username"]
    return None


def do_the_logout(token):
    del_filedata(TOKENS_FILENAME, token)


def get_auth_status(cookies):
    status = cookies.get("status", None)
    action = cookies.get("action", None)
    token = cookies.get("token", None)
    logging.info(f"get_auth_status() in: status={status} action={action} token={token}")
    content = {}
    if status == None:
        content = {"status": 0}
    elif status == "True":
        username = search_token(token)
        if username != None:
            content = {"status": 1, "action": action, "username": username}
        else:
            content = {"status": 2}
    else:
        content = {"status": 3}
    status_comment = {
        0: "游客进入主页",
        1: "登录成功/注册成功",
        2: "令牌失效(超时)",
        3: "登陆失败(密码错误)",
    }
    logging.info(f"get_auth_status() out: {status_comment[content['status']]}, content={content}")
    return content
