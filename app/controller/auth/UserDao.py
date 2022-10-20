from sqlalchemy import or_
from app.models.user import User
from app.middleware.Jwt import UserToken
from app.models.user import db
from app.utils.logger import Log


class UserDao(object):
    log=Log("UserDao")

    @staticmethod
    def register_user(username,user,password,email):
        try:
            users=User.query.filter(or_(User.username==username,User.email==email)).all()
            if users:
                raise Exception("帐号或者邮箱已注册")
            pwd=UserToken.add_salt(password)
            user=User(username,user,pwd,email)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            UserDao.log.error(f"注册失败{str(e)}")
            return str(e)
        return None



