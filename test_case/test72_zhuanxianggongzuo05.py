#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class zhuanxianggongzuo05Test(MyTest):

    def test_click_zhuanxianggongzuo05(self):
        '''"专项工作"第5条链接测试'''
        pagehome = ZdzzPage(self.driver)
        zhuanxianggongzuo05Title = pagehome.getText(pagehome.zhuanxianggongzuo05) #获取链接的文本值
        pagehome.click_zhuanxianggongzuo05()   #点击链接
        wait_title(self, zhuanxianggongzuo05Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == zhuanxianggongzuo05Title), "标题不是“%s”，测试不通过" % zhuanxianggongzuo05Title

if __name__ == '__main__':
    unittest.main()