#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class zhongyaowenjian_moreTest(MyTest):

    def test_click_zhongyaowenjian_more(self):
        '''重要讲话栏“更多”按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zhongyaowenjian()
        pagehome.click_zhongyaowenjian_more()   #点击链接
        wait_title(self, pagehome.zhongyaowenjian_more_title)
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == pagehome.zhongyaowenjian_more_title), "标题不是“%s”，测试不通过" % pagehome.zhongyaowenjian_more_title

if __name__ == '__main__':
    unittest.main()