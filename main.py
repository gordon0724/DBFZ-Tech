from flask import Flask, render_template
import glob
from datetime import datetime
import os

app = Flask("DBFZ")

@app.route("/learn/<c>")
def category(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  fill = []
  # ADD
  for i, f in enumerate(fs):
      a = open(f)
      article = a.read()
      a.close()
      fp = f.split("/")[-1].replace(".txt", "")
      utc = datetime.utcfromtimestamp(os.path.getmtime(f))
      # ADD
      t = (i, fp, str(utc), article)
      fill.append(t)
  return render_template("learn.html", cat=fill, title=c)

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

@app.route("/info")
def info():
  fill = []
  return render_template("info.html", cat=fill)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="3000")
