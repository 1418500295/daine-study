from flask import *
import json

app = Flask(__name__)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == "GET":
        user = request.args.get("user")
        passwd = request.args.get("passwd")
        return user +"\n" +passwd
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        return username + "\n" + password


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=1478, debug=True)