#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class SearchTest(MyTest):

    def test_click_search(self):
        '''"搜索"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_search()
        wait_title(self, pagehome.searchTitle)
        #第二种切换窗口的方法
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        assert(pagehome.driver.title == pagehome.searchTitle), "标题不是“总队主站”，测试不通过"

if __name__ == '__main__':
    unittest.main()