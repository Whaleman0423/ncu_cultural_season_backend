# 中大文化季的 liff 頁面後端

## Model
<br />

中大文化季需定義一個 model  
稱為 line_bot_demo  
屬性有：  
機器人名稱  
    &emsp;line_bot_name: String  
機器人描述  
    &emsp;line_bot_description: String  
作者  
    &emsp;line_bot_author: List[String]  
作者系級  
    &emsp;line_bot_author_department_grade: List[String]  
機器人標籤  
    &emsp;line_bot_tag: List[String]  
機器人 Bot basic ID  
    &emsp;line_bot_entrance_basic_ID: String  
機器人圖片網址  
    &emsp;line_bot_pic_url: String  

由於資料不是很多，可能也沒有要維持很久，  
因此會將資料整理成 json 檔  
圖片的部分，估計會用 google 表單收集，所以應該可以上傳圖片  
表單會自動轉成網址，表單要設定成限定圖片檔
<br />

## Dao
<br />
用來讀取 JSON 檔案並轉換成 Model 的 py 檔
<br />

## controller 
將物件轉換成 json，回傳給 app

## app 
flask 伺服器的總機，接收前端頁面的 request 並回傳資料給前端頁面

