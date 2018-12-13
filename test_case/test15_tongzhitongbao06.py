#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class tongzhitongbao06Test(MyTest):

    def test_click_tongzhitongbao06(self):
        '''"通知通报栏第六条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_tongzhitongbao()
        tongzhitongbao06Title = pagehome.getText(pagehome.tongzhitongbao06) #获取链接的文本值
        pagehome.click_tongzhitongbao06()   #点击链接
        wait_title(self, tongzhitongbao06Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == tongzhitongbao06Title), "标题不是“%s”，测试不通过" % tongzhitongbao06Title

if __name__ == '__main__':
    unittest.main()