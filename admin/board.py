from flask import render_template, session, redirect
from datetime import datetime, timedelta

from model.db import Mydb
from . import admin
from .auth import login_required
from api_v1.utils import dateFormatter, bookingDateFormatter

@login_required
@admin.route("/board")
def board():
    booking_list = []
    today = datetime.today()
    start_date_string = datetime.strftime(today, dateFormatter) # 轉字串
    end_date_string = datetime.strftime((today + timedelta(days=6)), dateFormatter) # 轉字串
    try:
        user = (session.get("user"))[1]
        mydb = Mydb()
        booking_list = mydb.getBookingByDate(start_date_string, end_date_string)
    
    except TypeError:
        return redirect("/admin")
    
    except Exception as e:
        print("資料庫出錯囉：", e)
    
    return render_template(
        "board.html", 
        user = user, 
        data = booking_list, 
        next_page = "/admin/board/1"
        )
    
@login_required
@admin.route("/board/<int:page>")
def next_page(page):
    booking_list = []
    if page>0 :
        today = datetime.today()
        start_date = today + timedelta(days=7)*page
        start_date_string = datetime.strftime(start_date, dateFormatter) # 轉字串
        end_date_string = datetime.strftime((start_date + timedelta(days=6)), dateFormatter) # 轉字串
        try:
            user = (session.get("user"))[1]
            mydb = Mydb()
            booking_list = mydb.getBookingByDate(start_date_string, end_date_string)
            
        except TypeError:
            return redirect("/admin")
        
        except Exception as e:
            print("資料庫出錯囉：", e)
        
        return render_template(
            "board.html", 
            user = user, 
            data = booking_list, 
            next_page = "/admin/board/"+str(page+1),
            pre_page = "/admin/board/"+str(page-1)
        )
    else:
        return redirect("/admin/board")