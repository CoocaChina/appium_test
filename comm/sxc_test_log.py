import os
import logging
import time

pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(pro_path, 'result')


class logger(object):
    def __init__(self):
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __console(self,level,message):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""

        # 创建一个file_handler
        file_handler =  logging.FileHandler(self.logname, 'a', encoding='utf-8')
        file_handler.setFormatter(self.formatter)
        file_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)
        # 创建一个stream_handler,控制台输出用
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':

            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(file_handler)

        file_handler.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == "__main__":
    log = logger()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试结束----")