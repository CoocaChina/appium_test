import os
from config.globalparameter import img_path

def save_img(wd, img_name):
    """
        传入一个img_name, 并存储到默认的文件路径下
    :param img_name:
    :return:
    """
    wd.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))