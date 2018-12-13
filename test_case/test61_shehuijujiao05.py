#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class shehuijujiao05Test(MyTest):

    def test_click_shehuijujiao05(self):
        '''"社会聚焦栏第5条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_shehuijujiao()
        shehuijujiao05Title = pagehome.getText(pagehome.shehuijujiao05) #获取链接的文本值
        pagehome.click_shehuijujiao05()   #点击链接
        wait_title(self, shehuijujiao05Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == shehuijujiao05Title), "标题不是“%s”，测试不通过" % shehuijujiao05Title

if __name__ == '__main__':
    unittest.main()