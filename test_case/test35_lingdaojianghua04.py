#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class lingdaojianghua04Test(MyTest):

    def test_click_lingdaojianghua04(self):
        '''"领导讲话栏第4条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_lingdaojianghua()
        lingdaojianghua04Title = pagehome.getText(pagehome.lingdaojianghua04) #获取链接的文本值
        pagehome.click_lingdaojianghua04()   #点击链接
        wait_title(self, lingdaojianghua04Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == lingdaojianghua04Title), "标题不是“%s”，测试不通过" % lingdaojianghua04Title

if __name__ == '__main__':
    unittest.main()