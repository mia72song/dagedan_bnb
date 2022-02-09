from flask import jsonify, request
from datetime import datetime

from . import auth
from App.models import Booking
from App.constants import DATETIME_FORMATTER, DATE_FORMATTER
from App.admin.auth import login_required

@auth.route("/booked")
@login_required
def get_booked_list():
    if request.args.get("start") and request.args.get("end"):
        booked = Booking.query.filter(Booking.date.between(request.args.get("start"), request.args.get("end")))
        data = []
        for b in booked:
            if b.o.status.value=="PAID":
                data_dict = {}
                data_dict["date"] = datetime.strftime(b.date, DATE_FORMATTER)
                data_dict["room_no"] = b.room_no
                data_dict["order_id"] = b.order_id
                od = b.o.detail
                data_dict["booker"] = od.booker_name +" "+od.booker_gender.value
                data_dict["phone"] = od.booker_phone
                data_dict["arrival_datetime"] = datetime.strftime(od.arrival_datetime, DATETIME_FORMATTER)
                data.append(data_dict)
        
        return jsonify({"data": data})

    else:
        return jsonify({"data": None})