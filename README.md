# Learn-DBFZ

## 專案介紹

此測試網站架設於repl.it  <br>
排版不適請見諒  <br>
提供給DBFZ的玩家不專業的教學
## 成品展示

[網站網址(host by heroku)](learndbfz.herokuapp.com)

![](https://github.com/gordon0724/DBFZ-Tech/raw/master/index.png)

## 使用技術

工具名稱 | 用途
---------|----------
Python 3 | 建立活網頁
Flask(python) | 建立伺服器
favicon | 網站icon
Repl.it | 撰寫網頁
HTML/CSS  | 網頁表示和排版
Heroku   | 託管網頁
Github   | 存放原始碼

## 程式碼片段

```python
@app.route("/")
def home():
    temp = glob.glob("articles/*")
    fill = []
    for t in temp:
        length = len(glob.glob(t + "/*.txt"))
        category = t.replace("articles/", "")
        f = (category, length)
        fill.append(f)
    return render_template("index.html", cat=fill)

```
