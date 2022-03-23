# 开发记录

- 这里目前先只放一个活动主页

# 开发约定

1. 网站中每个业务运行一个单独的 gunicorn 服务器，所有通用功能用 main.py 对应的独立 gunicorn 服务器，以保证相互可以独立更新而不中断其余业务
2. 在 html、html/md_content、static/js、static/css、static/img、static/md 这些目录中，每个业务都拥有独立的文件夹，以保证相互独立开发而不影响；而不彻底拆分，则是为了可以使用在共同的上级目录中通用的代码

# 资料记录

- [How to manage logs with Django, Gunicorn and NGINX](https://mattsegal.dev/django-gunicorn-nginx-logging.html)
- [关于前后端密码传输与存储？ -- v2ex](http://webcache.googleusercontent.com/search?q=cache:gWtXUF3WtQMJ:https://www.v2ex.com/t/789385&hl=zh-CN&gl=us&strip=1&vwsrc=0)
