from app import pity
from app.utils import Log
@pity.route('/')
def helloworld():
    log=Log("helloworld")
    log.info("test")
    return "helloworld"

if __name__=="__main__":
    pity.run("0.0.0.0",port="7777",threaded=True)


