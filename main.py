# -*- coding: utf-8 -*-

from App import create_app

app = create_app()

'''flask_migrate命令
初始化数据库：flask db init
迁移新更改：flask db migrate
升级：flask db upgrade
查看當前版本：flask db current
'''

if __name__=="__main__":
    '''生產環境啟動：
    $ export FLASK_ENV=production
    $ export FLASK_APP=main.py
    $ flask run --reload --debugger --host 0.0.0.0 --port 80
    '''
    #Development Environment:
    app.run()