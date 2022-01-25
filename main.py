#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import MigrateCommand

from App import create_app

app = create_app()

manager = Manager(app)
manager.add_command("db", MigrateCommand)

'''依賴降级：
pip install Flask-Migrate==2.6.0
pip install "Flask==1.1.4"
pip install "werkzeug==1.0.1"
'''

'''flask_migrate命令
初始化数据库：python main.py db init
迁移新更改：python main.py db migrate
升级：python main.py db upgrade
查看當前版本：python main.py db current
'''

if __name__=="__main__":
    '''生產環境啟動：
    $ export FLASK_ENV=production
    $ export FLASK_APP=main.py
    $ flask run --reload --debugger --host 0.0.0.0 --port 80
    OR
    $ python main.py runserver --host 0.0.0.0 --port 80
    '''
    #Development Environment:
    manager.run()