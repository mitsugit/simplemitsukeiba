# coding: utf-8
from flask import Flask, render_template
app = Flask(__name__)
import test

'''
@app.route('/')
def main():
    return "Hello world!"
'''

@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("mainpage.html")

"""
@app.route("/<name>", methods=["GET", "POST"])
def namepage(name):
    return render_template("name.html")
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")


@app.route('/test')
def get():
    # ↓　実行したいファイルの関数
    return test.hello()