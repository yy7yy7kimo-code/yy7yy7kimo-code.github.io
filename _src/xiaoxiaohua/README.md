# 小小花網站產生程式

`python3 _src/xiaoxiaohua/build.py` 會重新產生 `xiaoxiaohua/` 裡的所有頁面、sitemap.xml、llms.txt。
新文章：在 build.py 的 `ARTICLES` 最前面加一筆（slug、date、title、desc、img、body），img 用 `xiaoxiaohua/images/` 裡已有的圖。
這個資料夾以底線開頭，GitHub Pages 不會發佈它。
