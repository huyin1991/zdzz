#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class diaoyangongzuo05Test(MyTest):

    def test_click_diaoyangongzuo05(self):
        '''"调研工作栏第5条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_diaoyangongzuo()
        diaoyangongzuo05Title = pagehome.getText(pagehome.diaoyangongzuo05) #获取链接的文本值
        pagehome.click_diaoyangongzuo05()   #点击链接
        wait_title(self, diaoyangongzuo05Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == diaoyangongzuo05Title), "标题不是“%s”，测试不通过" % diaoyangongzuo05Title

if __name__ == '__main__':
    unittest.main()