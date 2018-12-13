#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class zhongyaowenjian03Test(MyTest):

    def test_click_zhongyaowenjian03(self):
        '''"重要文件栏第3条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zhongyaowenjian()
        zhongyaowenjian03Title = pagehome.getText(pagehome.zhongyaowenjian03) #获取链接的文本值
        pagehome.click_zhongyaowenjian03()   #点击链接
        wait_title(self, zhongyaowenjian03Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == zhongyaowenjian03Title), "标题不是“%s”，测试不通过" % zhongyaowenjian03Title

if __name__ == '__main__':
    unittest.main()