"""
做一個 Flask 後端應用，用來讀取與並回復前端的要求。

"""
from flask import Flask, request, abort
from controllers.line_bot_demo_controller import LineBotDemoController

# import logging
# import os


app = Flask(__name__, static_url_path="/", static_folder="templates")

@app.route('/ping')
def hello_world():  # put application's code here
    return 'pong'

@app.route('/line_bot_demos', methods=['GET'])
def line_bot_demos():
    """
    取得所有 line_bot_demo json 的清單
    """
    print('取 line_bot_demos')
    return LineBotDemoController.list_all_line_bot_demo()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
