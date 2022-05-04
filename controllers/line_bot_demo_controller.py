from flask import jsonify, Response
from daos.line_bot_demo_dao import LineBotDemoDaoJson


class LineBotDemoController:
    
    @classmethod
    def list_all_line_bot_demo(cls):
        print("LineBotDemoController - list_all_line_bot_demo")
        line_bot_demo_list = LineBotDemoDaoJson.get_all_line_bot_demo()
        if line_bot_demo_list:
            print("已取得line_bot_demo_list:\n", line_bot_demo_list)
            return jsonify([line_bot_demo.to_dict() for line_bot_demo in line_bot_demo_list])
        else:
            print('沒取到東西')
            return Response(response="""{"message": "NOT FOUND"}""", status=404)