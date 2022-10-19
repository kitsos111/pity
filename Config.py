import os

class Config():
    Root=os.path.dirname(os.path.abspath(__file__))
    LOG_NAME=os.path.join(Root,'logs','pity.log')
    JSON_AS_ASCII=False
