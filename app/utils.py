import logbook
from app import pity
from app.decorator import Singletondecorator

@Singletondecorator
class Log(object):
    handle=None

    def __init__(self,name='pity',filename=pity.config['LOG_NAME']):
        self.handle=logbook.FileHandler(filename,encoding='utf-8')
        self.logger=logbook.Logger(name)
        self.handle.push_application()
        logbook.set_datetime_format("local")

    def info(self,*args,**kwargs):
        return self.logger.info(*args,**kwargs)

    def warning(self,*args,**kwargs):
        return self.logger.warning(*args,**kwargs)

    def debug(self,*args,**kwargs):
        return self.logger.debug(*args,**kwargs)

    def error(self,*args,**kwargs):
        return self.logger.error(*args,**kwargs)
