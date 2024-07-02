"""
导入核心的flask包
"""

from flask import Flask
from dotenv import load_dotenv
from helper import is_isbn_or_key

__author__ = '七月'

# 读取环境变量 FLASK_ENV,通过os.getenv()方法中引入字段名称来读取
from gevent import os

from yushu_book import YuShuBook

load_dotenv(dotenv_path='.flaskenv', override=True)
appName = os.getenv("FLASK_APP")
port = os.getenv("PORT")

# 实例化
app = Flask(
    appName,  # 导入路径（寻找静态目录与模板目录位置的参数）
    static_url_path='/web',  # 访问静态资源的url前缀，默认值是static
    static_folder='static',  # 静态文件存放的目录，默认值是static
    template_folder='templates',  # 模板文件存放的目录，默认值是templates
)
app.config.from_object("config")
app.config.setdefault("JSON_AS_ASCII", False)
app.config.setdefault("JSONIFY_MIMETYPE", "application/json;charset=utf-8")


# 视图函数
@app.route('/hello/')
def index():
    # ----------------------
    # status code 200,400,301
    # content-type: http headers, html标签不会显示。
    # content-type = text/html 所以默认html标签不显示,但可以修改，如下就是修改方法：
    # 返回Response对象，并非文本
    # return '<html>'+name + ':生日快乐!</html>'  # 基于类的视图（即插视图)
    # 'content-type': 'application/json', #可以返回json
    # ----------------------
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.bing.com'  # 会重定向指bing
    }
    # response = make_response("<html></html>", 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers


#  http://192.168.1.27:5000/book/search/郭敬明/1
#  http://192.168.1.27:5000/book/isbn/9787501524044
#  http://192.168.1.27:5000/book/search/9787501524044/1
# 将关键字搜索与isbn搜索放在一块，一个入口，通过程序区分
@app.route("/book/search/<q>/<page>")
def book_search(q="", page=1):
    """
    q: 普通关键字还是isbn
    page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        # pycharm自动导入 alt + Enter
        result =  YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    # dict
    return result;


# nginx+uwsgi
# 生产环境有uwsgi后，uwsgi执行了应用，app.run可不执行。
# 生产环境中不执行，"__main__"保证
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
