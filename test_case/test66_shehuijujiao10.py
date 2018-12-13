#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class shehuijujiao10Test(MyTest):

    def test_click_shehuijujiao10(self):
        '''"社会聚焦栏第10条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_shehuijujiao()
        shehuijujiao10Title = pagehome.getText(pagehome.shehuijujiao10) #获取链接的文本值
        pagehome.click_shehuijujiao10()   #点击链接
        wait_title(self, shehuijujiao10Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == shehuijujiao10Title), "标题不是“%s”，测试不通过" % shehuijujiao10Title

if __name__ == '__main__':
    unittest.main()