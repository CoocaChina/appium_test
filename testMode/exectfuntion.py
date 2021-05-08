""" 
@author: lileilei
@file: exectfuntion.py 
@time: 2018/4/17 13:46 
"""
from comm.operyaml import open_da
from comm.log import logger, LOG
import time
from comm.py_app import deriver_fengzhuang as feng

'''解析测试步骤，按照需求进行测试用例
   默认的定位的最后的一组为断言
'''


@logger('解析测试步骤')
class Makeappcase():
    def __init__(self, deriver, path):
        self.deriver = deriver
        self.path = path

    def open_file(self):
        return open_da(path=self.path)

    def exce_case(self):
        data = self.open_file()['data']
        case_der = feng(driver=self.deriver)
        LOG.info(data)
        LOG.info(len(data) - 1)
        for i in range(len(data) - 1):
            LOG.info((data[i]['index']))
            f = case_der.find_ele(lujing=data[i]['element_info'], fangfa=data[i]['find_type'])
            if data[i]['operate_type'] == 'click':
                LOG.info(data[i]['operate_type'])
                f.click()
            elif data[i]['operate_type'] == 'text':
                f.text
            elif data[i]['operate_type'] == 'send_key':
                # f[int(data[i]['index'])].clear()
                f.send_key(data[i]['text'])
            else:
                LOG.info('请检查您的测试步骤')
            i += 1
            time.sleep(8)
        # f = case_der.find_ele(lujing=data[-1]['element_info'], fangfa=data[-1]['find_type'])
        # if data[-1]['operate_type'] == 'text':
        #     duanyan = {'code': 0, 'data': f[int(data[-1]['index'])].text}
        # else:
        #     duanyan = {'code': 1, 'data': "请检查您的测试步骤最后一步为断言用的"}
        #     LOG.info('请检查您的测试步骤最后一步为断言用的')
        # return duanyan
