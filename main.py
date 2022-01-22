from email.mime import application
from App import create_app

#dev, pro, test，配置文件因運行環境而異
env = "dev"
application = create_app(env)

if __name__=="__main__":
    #Rroduction Environment：
    if env=="pro":
        application.run(host="0.0.0.0", port=3000)

    #Development Environment:default host="127.0.0.1" port=5000
    else:
        application.run()