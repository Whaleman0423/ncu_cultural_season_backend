"""
建立一個 DAO 用來讀取 JSON 資料
"""

from __future__ import annotations
import json
import os 

from models.line_bot_demo import LineBotDemo
from typing import List


class LineBotDemoDaoJson:
    """讀取 JSON 後，將資料放入 LineBotDemo 物件，在回傳
    """
    @classmethod
    def get_all_line_bot_demo(cls) -> List[LineBotDemo]:
        """
        取得所有的 line 官方帳號資料
        並將資料轉換成 LineBotDemo 物件
        最後回傳 LineBotDemo 物件 清單

        邏輯:
            1. 讀取 JSON 檔案
            2. 逐筆將裡面的資料轉換成 LineBotDemo 物件並放入清單
            3. 回傳清單
        """
        print('LineBotDemoDaoJson - get_all_line_bot_demo')
        try:
            print('開 line_bot_demos.json 檔')
            with open('./line_bot_demos.json', 'r', encoding='utf-8') as file:
                line_bot_demos_list = [LineBotDemo.from_dict(json.loads(line_bot_demo_dict)) for line_bot_demo_dict in file]
            return line_bot_demos_list
        except FileNotFoundError:
            print("沒有找到 line_bot_demos.json 檔")
            return None