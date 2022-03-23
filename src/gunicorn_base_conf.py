# -*- coding: utf-8 -*-
#  bind = "unix:/root/play/homepage/src/main.sock"  # 监听地址和端口号
workers = 1
mask = 777
threads = 1  # 指定每个进程的线程数，默认为 1
worker_connections = 2000  # 最大客户并发量
timeout = 200  # 超时时间，默认 30s
keepalive = 2  # 默认值
reload = True  # 开发模式，代码更新时自动重启
daemon = False  # 守护 Gunicorn 进程，默认 False
capture_output = True  # 抓取stdout

accesslog = "../log/access.log"  # 访问日志文件
errorlog = "../log/error.log"
loglevel = "debug"  # 日志输出等级，debug, info, warning, error, critical
