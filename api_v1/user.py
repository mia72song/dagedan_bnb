from flask import session, jsonify, request

from . import api
from model.db import Mydb

@api.route("/user", methods=["POST"])
def login():
    login_data = request.get_json()
    if login_data:
        if login_data["username"]=="" or login_data["password"]=="":
            return jsonify({
                "error": True,
                "message": "登入資料皆不得為空值"
            }), 400
        
        try:
            mydb = Mydb()
            user_info = mydb.getUser(login_data["username"], login_data["password"])
            
            if user_info:
                print("登入成功")
                session["user"] = user_info
                return jsonify({"ok": True}), 200
            
            else:
                return jsonify({
                    "error": True,
                    "message": "帳號或密碼錯誤"
                }), 400
        
        except Exception as e:
            return jsonify({
                "error": True,
                "message": f"伺服器內部錯誤：{e}"
            }), 500
    else:
        return jsonify({
            "error": True,
            "message": "無資料"
        }), 500

@api.route("/user", methods=["DELETE"])
def logout():
    if session.get("user"):
        del session["user"]
    return jsonify({"ok": True}), 200

@api.route("/user")
def get_current_user():
    return jsonify({
        "data": session.get("user")
    }), 200
