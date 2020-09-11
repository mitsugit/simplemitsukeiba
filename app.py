# coding: utf-8
from flask import Flask, render_template
app = Flask(__name__)
import test
import pyfolder.keisan as keisan



'''
@app.route('/')
def main():
    return "Hello world!"
'''

# @app.route("/", methods=["GET", "POST"])
# def main_page():
# num = 1111
#     return render_template("mainpage.html",num=num)

@app.route("/")
def main_page():
    num = 1111
    return render_template("mainpage.html",num=num)

@app.route("/", methods=["POST"])
def sum_cal():
    result = keisan.sum_cal()
    return render_template("mainpage.html",result=result)


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


@app.route("/goukei")
def goukei():
    return render_template("goukei.html")