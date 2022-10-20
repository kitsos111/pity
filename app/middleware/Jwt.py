import hashlib

from datetime import datetime,timedelta

import jwt
from flask import jsonify
from jwt.exceptions import ExpiredSignatureError


EX_HOUR=3

class UserToken(object):
    key="pitytoker"
    salt="pity"

    @staticmethod
    def get_token(data):
        now_data=dict({"exp":datetime.utcnow()+timedelta(hours=EX_HOUR)},**data)
        return jwt.encode(now_data,keyy=UserToken.key).decode()



    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token,key=UserToken.key)
        except ExpiredSignatureError:
            raise Exception("token已过期，请重新登录")

    @staticmethod
    def add_salt(passwd):
        m=hashlib.md5()
        bt=f"{passwd}{UserToken.salt}".encode("utf-8")
        m.update(bt)
        return m.hexdigest()




