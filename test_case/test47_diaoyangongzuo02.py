#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class diaoyangongzuo02Test(MyTest):

    def test_click_diaoyangongzuo02(self):
        '''"调研工作栏第2条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_diaoyangongzuo()
        diaoyangongzuo02Title = pagehome.getText(pagehome.diaoyangongzuo02) #获取链接的文本值
        pagehome.click_diaoyangongzuo02()   #点击链接
        wait_title(self, diaoyangongzuo02Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == diaoyangongzuo02Title), "标题不是“%s”，测试不通过" % diaoyangongzuo02Title

if __name__ == '__main__':
    unittest.main()