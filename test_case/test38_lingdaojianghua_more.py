#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class lingdaojianghua_moreTest(MyTest):

    def test_click_lingdaojianghua_more(self):
        '''领导讲话栏“更多”按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_lingdaojianghua()
        pagehome.click_lingdaojianghua_more()   #点击链接
        wait_title(self, pagehome.lingdaojianghua_more_title)
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == pagehome.lingdaojianghua_more_title), "标题不是“%s”，测试不通过" % pagehome.lingdaojianghua_more_title

if __name__ == '__main__':
    unittest.main()