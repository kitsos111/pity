from app import pity
from app.utils.logger import Log
from app import dao
from app.controller.auth.user import auth
from app.controller.auth.UserDao import UserDao

pity.register_blueprint(auth)


@pity.route('/')
def helloworld():
    log=Log("helloworld")
    log.info("test")
    return "helloworld"

if __name__=="__main__":
    pity.run("0.0.0.0",port="7777",threaded=True)


