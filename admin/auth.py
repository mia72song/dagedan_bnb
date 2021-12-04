from flask import session, redirect
import functools

#驗證是登入狀態的裝飾器
def login_required(view_func):
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        if session.get("user") is not None:
            return view_func(*args, **kwargs)
        else:
            return redirect("/admin")
    return wrapper