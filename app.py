"""
做一個 Flask 後端應用，用來讀取與並回復前端的要求。

"""
from flask import Flask, request, abort
from controllers.line_bot_demo_controller import LineBotDemoController
from flask_cors import CORS, cross_origin

# import logging
# import os


app = Flask(__name__, static_url_path="/", static_folder="templates")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/ping')
def hello_world():  # put application's code here
    return 'pong'

@app.route('/line_bot_demos', methods=['GET'])
@cross_origin()
def line_bot_demos():
    """
    取得所有 line_bot_demo json 的清單
    """
    print('取 line_bot_demos') 
    return LineBotDemoController.list_all_line_bot_demo()

@app.route('/answere_for_label', methods=['PUT'])
@cross_origin()
def answere_for_tag():
    """
    接收三個布林值，判斷是哪個標籤後，回傳該標籤
    接收的樣子
        {"answeres": [True, False, True]}
    """
    return LineBotDemoController.find_robot_label(data=request)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
