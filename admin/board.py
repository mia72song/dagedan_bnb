from flask import render_template, session, redirect
from datetime import datetime, timedelta

from model.db import Mydb
from model.seven_days import getSevenDays
from . import admin

@admin.route("/board")
def board():
    if session.get("user") :
        return render_template(
            "board.html", 
            user = (session.get("user"))[1], 
            data = getSevenDays(datetime.today()), 
            next_page = "/admin/board/1"
            )
    else:
        return redirect("/admin")

@admin.route("/board/<int:page>")
def next_page(page):
    if page==0:
        return redirect("/admin/board")
    if session.get("user") :
        seven_days = timedelta(days=7)
        today = datetime.today()
        return render_template(
            "board.html", 
            user = (session.get("user"))[1], 
            data = getSevenDays(today+seven_days*page), 
            next_page = "/admin/board/"+str(page+1),
            pre_page = "/admin/board/"+str(page-1)
        )
    else:
        return redirect("/admin/board")