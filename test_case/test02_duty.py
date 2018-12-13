#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class DutyTest(MyTest):

    def test_click_duty(self):
        '''"今日值班"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_duty()
        wait_title(self, pagehome.dutyTitle)
        #第二种切换窗口的方法
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        assert(pagehome.driver.title == pagehome.dutyTitle), "标题不是“%s”，测试不通过" % pagehome.dutyTitle

if __name__ == '__main__':
    unittest.main()