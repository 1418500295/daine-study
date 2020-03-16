from flask import *
import json

app = Flask(__name__)
# 处理接口返回无法显示中文的问题
app.config['JSON_AS_ASCII'] = False

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        user = request.args.get("user")
        passwd = request.args.get("passwd")
        return user +"\n" +passwd
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        return username + "\n" + password

@app.route('/task',methods=['GET'])
def get_all_task():

    task = {
        "data": {
            "loginName": "admin",
            "rule": 1
        },
        "statusCode": {
            "code": 0,
            "msg": "成功"
        },
        "success": 1

    }
    data = jsonify(task)
    return data

@app.route("/getMain",methods=["GET"])
def get_main():
    name = request.args.get("name")
    age = request.args.get("age")
    return "hello"

@app.route("/postMain",methods=["POST"])
def post_main():
    sex = request.form["sex"]
    color = request.form["color"]
    json_data = {
        "msg": "成功",
        "success": 1
    }
    # 将结果转换为json格式
    return jsonify(json_data)

def post_json_data():
    request


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=1478, debug=True)