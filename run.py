from app import pity

@pity.route('/')
def helloworld():
    return "helloworld"

if __name__=="__main__":
    pity.run("0.0.0.0",port="7777",threaded=True)


