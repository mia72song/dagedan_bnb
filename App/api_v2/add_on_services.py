from flask import jsonify

from . import api
from App.models import Apidb

# 初始化response content
body = "" #json
status_code = 0

@api.route("/add_on_services")
def get_add_on_services():
    cols = ["id", "name", "price", "images", "description"]
    try:
        mydb = Apidb()
        results = mydb.getAddOnServices()
        data = {}
        for r in results:
            id = r[0]
            data_dict = dict(zip(cols[1:], r[1:-1]))
            if data_dict["images"]:
                data_dict["images"] = data_dict["images"].split(", ")
                
            data_dict["price"] = int(data_dict["price"])
            data[id] = data_dict

        body = jsonify({"data": data})
        status_code = 200

    except Exception as e:
        body = jsonify({
            "error": True,
            "message": f"伺服器內部錯誤：{e}"
        })
        status_code = 500

    return body, status_code