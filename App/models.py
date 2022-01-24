from sqlalchemy import text
from datetime import datetime

from App import db

class Calendar(db.Model):
    date = db.Column(db.Date, primary_key=True)
    day = db.Column(db.String(3), comment="星期")
    is_holiday = db.Column(db.Boolean, default=False, server_default=text('0'))
    note = db.Column(db.String(128))
    is_closed = db.Column(db.Boolean, default=False, server_default=text('0'))
    #  設置關聯relationship：一對多的『一』，relationship("類名")
    booked = db.relationship("Booking", backref="calendar", lazy="dynamic")

class User(db.Model):
    __tablename__ = "users"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    create_datetime = db.Column(db.DateTime, default=datetime.now)
    is_del = db.Column(db.Boolean, default=False, server_default=text("0"))

class Booking(db.Model):
    #  設置外鍵ForeignKey，一對多的『多』，ForeignKey("table_name.col_name")
    date = db.Column(db.Date, db.ForeignKey("calendar.date"), primary_key=True)
    room_no = db.Column(db.String(64), primary_key=True)
    order_id = db.Column(db.String(64), nullable=False)
    room_name = db.Column(db.String(128))