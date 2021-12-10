from flask import session, jsonify, request
from flask.helpers import make_response
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies

from . import auth
from model.db import Mydb

@auth.route("/user", methods=["POST"])
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
                session["user"] = user_info
                access_token = create_access_token(identity=user_info[0])
                resp = make_response(jsonify({
                    "ok": True
                }), 200)                
                set_access_cookies(resp, access_token)

                return resp
            
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

@auth.route("/user", methods=["DELETE"])
def logout():
    if session.get("user"):
        del session["user"]

    resp = make_response(jsonify({"ok": True}), 200)
    unset_jwt_cookies(resp)
    
    return resp

@auth.route("/user")
def get_current_user():
    return jsonify({
        "data": session.get("user")
    }), 200
