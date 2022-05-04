# 中大文化季的 liff 頁面後端
<br />
## Model
中大文化季需定義一個 model 
稱為 line_bot_demo
屬性有：
機器人名稱
    line_bot_name: String
機器人描述
    line_bot_description: String
作者
    line_bot_author: List[String]
作者系級
    line_bot_author_department_grade: List[String]
機器人標籤
    line_bot_tag: List[String]
機器人 Bot basic ID 
    line_bot_entrance_basic_ID: String
機器人圖片網址
    line_bot_pic_url: String

由於資料不是很多，可能也沒有要維持很久，
因此會將資料整理成 json 檔
圖片的部分需要網址，網址須公開可以先測試
如果圖片放在 google 雲端硬碟，設為公開，
看能不能讓 flutter 讀取

<br />

