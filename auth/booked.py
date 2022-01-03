from flask import jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime

from . import auth
from models import Authdb
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

