#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class diaoyangongzuo09Test(MyTest):

    def test_click_diaoyangongzuo09(self):
        '''"调研工作栏第9条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_diaoyangongzuo()
        diaoyangongzuo09Title = pagehome.getText(pagehome.diaoyangongzuo09) #获取链接的文本值
        pagehome.click_diaoyangongzuo09()   #点击链接
        wait_title(self, diaoyangongzuo09Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == diaoyangongzuo09Title), "标题不是“%s”，测试不通过" % diaoyangongzuo09Title

if __name__ == '__main__':
    unittest.main()