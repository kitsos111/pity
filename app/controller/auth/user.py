import requests
from flask import Blueprint
from flask import jsonify
from flask import request

from app.controller.auth.UserDao import UserDao

auth=Blueprint("auth",__name__,url_prefix="/auth")

@auth.route("/register",methods=["POST"])
def register():
    req=request.get_json()
    username,email=req.get("username"),req.get("email")
    if not username:
        return jsonify(dict(code=101, msg='请输入帐号'))
    if not email:
        return jsonify(dict(code=101, msg='请输入邮箱'))
    user,password=req.get("user"),req.get("password")
    if not user or not password:
        return jsonify(dict(code=101, msg='请输入用户名与密码'))
    print(req.get("email"))
    users=UserDao.register_user(username,user, password, email)
    if users is not None:
        return jsonify(dict(code=110, msg=users))
    return jsonify(dict(code=0,msg='注册成功'))