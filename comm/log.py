'''日志相关'''
import os, logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps
from config.globalparameter import log_path

check_path = log_path
LOG_DIR = log_path
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


def get_logger(name='appium', file_log=file_stream, level=''):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger(file_log=file_stream, level='INFO')


def logger(param):
    def wrap(function):
        @wraps(function)
        def _wrap(*args, **kwargs):
            LOG.info("当前模块 {}".format(param))
            LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            return function(*args, **kwargs)

        return _wrap

    return wrap
