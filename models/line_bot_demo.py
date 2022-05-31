from __future__ import annotations


class LineBotDemo(object):
    '''
    提供 to_dict 和 from_dict 兩個方法，方便快速轉換 json <-> 物件
    提供打印方法 __repr__ ，方便快速打印字串

    Attributes:
        line_bot_name (str):
            Line 官方帳號名稱
        line_bot_description (str):
            Line 官方帳號描述
        line_bot_author (List[str]):
            Line 官方帳號作者名字
        line_bot_author_department_grade (List[str]):
            Line 官方帳號作者系級
        line_bot_tag (List[str]):
            Line 官方帳號特色標籤
        line_bot_entrance_basic_ID (str):
            Line 官方帳號 basic ID 
                ex. @100qffhp
        line_bot_pic_url (str):
            Line 官方帳號大頭貼的 url
        youtube_link (str):
            youtube 影片連結
        
    '''
    def __init__(self, line_bot_name, line_bot_description=" ", line_bot_author=[' '], line_bot_author_department_grade=[' '], line_bot_tag=[' '], line_bot_entrance_basic_ID=" ", line_bot_pic_url=" ", youtube_link=" "):
        '''建構子'''
        self.line_bot_name = line_bot_name
        self.line_bot_description = line_bot_description
        self.line_bot_author = line_bot_author
        self.line_bot_author_department_grade = line_bot_author_department_grade
        self.line_bot_tag = line_bot_tag
        self.line_bot_entrance_basic_ID = line_bot_entrance_basic_ID
        self.line_bot_pic_url = line_bot_pic_url
        self.youtube_link = youtube_link

    @staticmethod
    def from_dict(linebotdemo_dict: dict) -> LineBotDemo:
        '''將 LineBotDemo 的 json 快速轉成 LineBotDemo 物件的方法
        
        argument:linebotdemo_dict:
            LineBotDemo 的 dict
        
        return:
            LineBotDemo
        '''
        linebotdemo = LineBotDemo(
            line_bot_name=linebotdemo_dict.get('line_bot_name'),
			line_bot_description=linebotdemo_dict.get('line_bot_description', " "),
			line_bot_author=linebotdemo_dict.get('line_bot_author', [' ']),
			line_bot_author_department_grade=linebotdemo_dict.get('line_bot_author_department_grade', [' ']),
			line_bot_tag=linebotdemo_dict.get('line_bot_tag', [' ']),
			line_bot_entrance_basic_ID=linebotdemo_dict.get('line_bot_entrance_basic_ID', " "),
			line_bot_pic_url=linebotdemo_dict.get('line_bot_pic_url', " "),
            youtube_link = linebotdemo_dict.get('youtube_link', " ")
			
        )
        return linebotdemo

    def to_dict(self):
        '''將 LineBotDemo 的物件快速轉換成 Python dict 的方法
        
        return:
            LineBotDemo 的 dict
        '''
        linebotdemo_dict = {
            'line_bot_name': self.line_bot_name,
			'line_bot_description': self.line_bot_description,
			'line_bot_author': self.line_bot_author,
			'line_bot_author_department_grade': self.line_bot_author_department_grade,
			'line_bot_tag': self.line_bot_tag,
			'line_bot_entrance_basic_ID': self.line_bot_entrance_basic_ID,
			'line_bot_pic_url': self.line_bot_pic_url,
            'youtube_link': self.youtube_link
		}
        return linebotdemo_dict

    def __repr__(self):
        '''打印 LineBotDemo 的方法'''
        return (f'''LineBotDemo(
            line_bot_name={self.line_bot_name},
			line_bot_description={self.line_bot_description},
			line_bot_author={self.line_bot_author},
			line_bot_author_department_grade={self.line_bot_author_department_grade},
			line_bot_tag={self.line_bot_tag},
			line_bot_entrance_basic_ID={self.line_bot_entrance_basic_ID},
			line_bot_pic_url={self.line_bot_pic_url},
            youtube_link={self.youtube_link}
        )''')
    