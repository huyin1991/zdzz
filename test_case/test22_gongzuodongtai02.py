#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class gongzuodongtai02Test(MyTest):

    def test_click_gongzuodongtai02(self):
        '''"工作动态栏第2条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_gongzuodongtai()
        gongzuodongtai02Title = pagehome.getText(pagehome.gongzuodongtai02) #获取链接的文本值
        pagehome.click_gongzuodongtai02()   #点击链接
        wait_title(self, gongzuodongtai02Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == gongzuodongtai02Title), "标题不是“%s”，测试不通过" % gongzuodongtai02Title

if __name__ == '__main__':
    unittest.main()