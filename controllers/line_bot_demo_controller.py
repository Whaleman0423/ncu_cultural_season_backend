from flask import jsonify, Response, Request
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

    @classmethod
    def find_robot_label(cls, data: Request):
        """Q1, Q2, Q3, Q4 represents the answer of the four questions (either 1 or 0)"""
        try:
        #                  0       1      2       3       4       5      6       7  
            LabelList = ["愛情", "推理", "美食", "挑戰", "旅遊", "驚悚", "科技", "運動"]
            result = ''
            answere_dict = data.get_json()
            answeres_list = answere_dict["answeres"]
            for q in answeres_list:
                result += ('1' if q is True else '0') 

            # transfer binary index to hex index and get the Label
            return LabelList[ int(result, 2)%9 ]
        except:
            return Response(response="""{"message": "system error"}""", status=404)
