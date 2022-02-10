from sqlalchemy import text
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
import enum

from App import db
from .mydb import Mydb

class Calendar(db.Model):
    date = db.Column(db.Date, primary_key=True)
    day = db.Column(db.String(3), comment="星期")
    is_holiday = db.Column(db.Boolean, default=False, server_default=text('0'))
    note = db.Column(db.String(128))
    is_closed = db.Column(db.Boolean, default=False, server_default=text('0'))
    
    booked = db.relationship("Booking", backref="c", lazy="dynamic")

class User(db.Model):
    __tablename__ = "users"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    create_datetime = db.Column(db.DateTime, default=datetime.now)
    is_del = db.Column(db.Boolean, default=False, server_default=text("0"))

    def setPassword(self, input_value):
        self.password = generate_password_hash(input_value)

    def checkPassword(self, input_value):
        return check_password_hash(self.password, input_value)

class Booking(db.Model):
    date = db.Column(db.Date, db.ForeignKey("calendar.date"), primary_key=True)
    room_no = db.Column(db.String(64), db.ForeignKey("rooms.room_no"), primary_key=True)
    order_id = db.Column(db.String(64), db.ForeignKey("orders.oid"), primary_key=True)
    is_del = db.Column(db.Boolean, default=False, server_default=text("0"))

class Order(db.Model):
    __tablename__ = "orders"
    oid = db.Column(db.String(64), primary_key=True)
    create_datetime = db.Column(db.DateTime, default=datetime.now)    
    amount = db.Column(db.Integer, nullable=False)
    payment_deadline = db.Column(db.Date, nullable=False)
    payment_id = db.Column(db.String(32), db.ForeignKey("payment_atm.pid"))
    class OrderStatus(enum.Enum):
        NEW = "NEW"
        PENDING = "PENDING"
        PAID = "PAID"
        CANCEL = "CANCEL"
        REFUND = "REFUND"
    status = db.Column(db.Enum(OrderStatus), server_default="NEW")
    update_datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    update_user = db.Column(db.String(64))
    note = db.Column(db.String(255))

    booked = db.relationship("Booking", backref="o", lazy="dynamic")
    detail = db.relationship("OrderDetail", backref="o", uselist=False)
    payment = db.relationship("PaymentAtm", backref="o", uselist=False)
        
    def getDataDict(self):
        table_name = self.__tablename__
        pk_col = "oid"
        pk_value = self.oid
        mydb = Mydb()
        data_dict = mydb.getAllByPk(table_name, (pk_col, pk_value))
        return data_dict

class OrderDetail(db.Model):
    __tablename__ = "order_details"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.String(64), db.ForeignKey("orders.oid"), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    nights = db.Column(db.Integer, server_default=text("1"))
    num_of_guests = db.Column(db.Integer, server_default=text("1"))
    room_type = db.Column(db.String(64), db.ForeignKey("room_types.type"), nullable=False)
    room_quantity = db.Column(db.Integer, server_default=text("1"))

    booker_name = db.Column(db.String(128), nullable=False)
    class Gender(enum.Enum):
        M = "先生"
        F = "小姐"
    booker_gender = db.Column(db.Enum(Gender), server_default="M")
    booker_phone = db.Column(db.String(10), nullable=False)
    booker_email = db.Column(db.String(128), nullable=False)
    arrival_datetime = db.Column(db.DateTime)

    room = db.relationship("RoomType", backref="od", uselist=False)

    def getDataDict(self):
        table_name = self.__tablename__
        pk_col = "id"
        pk_value = self.id
        mydb = Mydb()
        data_dict = mydb.getAllByPk(table_name, (pk_col, pk_value))
        return data_dict

class Room(db.Model):
    __tablename__ = "rooms"
    room_no = db.Column(db.String(64), primary_key=True)
    room_type = db.Column(db.String(64), db.ForeignKey("room_types.type"), nullable=False)
    is_available = db.Column(db.Boolean, default=False, server_default=text("1"))

    booked = db.relationship("Booking", backref="r", lazy="dynamic")

class RoomType(db.Model):
    __tablename__ = "room_types"
    type = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128))
    accommodate = db.Column(db.Integer)
    rate_weekday = db.Column(db.Integer, nullable=False)
    rate_holiday = db.Column(db.Integer, nullable=False)
    single_discount = db.Column(db.Float)
    description = db.Column(db.Text)
    images = db.Column(db.Text)
    is_del = db.Column(db.Boolean, default=False, server_default=text("0"))

    rooms = db.relationship("Room", backref="rt", lazy="dynamic")

    def getDataDict(self):
        table_name = self.__tablename__
        pk_col = "type"
        pk_value = self.type
        if not self.is_del:
            mydb = Mydb()
            data_dict = mydb.getAllByPk(table_name, (pk_col, pk_value))
            return data_dict
        else:
            return None    

class PaymentAtm(db.Model):
    __tablename__ = "payment_atm"
    pid = db.Column(db.String(32), primary_key=True)
    bank = db.Column(db.String(128), nullable=False)
    account_no = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    transfer_date = db.Column(db.Date, nullable=False)
    update_datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    update_user = db.Column(db.String(64))
    is_del = db.Column(db.Boolean, default=False, server_default=text("0"))

    def getDataDict(self):
        table_name = self.__tablename__
        pk_col = "pid"
        pk_value = self.pid
        mydb = Mydb()
        data_dict = mydb.getAllByPk(table_name, (pk_col, pk_value))
        return data_dict
