#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class zhongyaowenjian01Test(MyTest):

    def test_click_zhongyaowenjian01(self):
        '''"重要文件栏第1条新闻"链接测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zhongyaowenjian()
        zhongyaowenjian01Title = pagehome.getText(pagehome.zhongyaowenjian01) #获取链接的文本值
        pagehome.click_zhongyaowenjian01()   #点击链接
        wait_title(self, zhongyaowenjian01Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == zhongyaowenjian01Title), "标题不是“%s”，测试不通过" % zhongyaowenjian01Title

if __name__ == '__main__':
    unittest.main()