#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class tongzhitongbao_moreTest(MyTest):

    def test_click_tongzhitongbao_more(self):
        '''通知通报栏“更多”按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_tongzhitongbao()
        pagehome.click_tongzhitongbao_more()   #点击链接
        wait_title(self, pagehome.tongzhitongbao_more_title)
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == pagehome.tongzhitongbao_more_title), "标题不是“%s”，测试不通过" % pagehome.tongzhitongbao_more_title

if __name__ == '__main__':
    unittest.main()