#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class tongzhitongbao04Test(MyTest):

    def test_click_tongzhitongbao04(self):
        '''"通知通报栏第四条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_tongzhitongbao()
        tongzhitongbao04Title = pagehome.getText(pagehome.tongzhitongbao04) #获取链接的文本值
        pagehome.click_tongzhitongbao04()   #点击链接
        wait_title(self, tongzhitongbao04Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == tongzhitongbao04Title), "标题不是“%s”，测试不通过" % tongzhitongbao04Title

if __name__ == '__main__':
    unittest.main()