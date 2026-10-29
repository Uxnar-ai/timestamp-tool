#!/usr/bin/env python3.12
# ts —— 时间戳与人能看懂的时间互转，一行一条，全在浏览器里算
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("page.html")


@app.get("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("TS_PORT", "8890")), debug=False)
