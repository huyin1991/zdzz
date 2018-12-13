#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class zhuanxianggongzuo02Test(MyTest):

    def test_click_zhuanxianggongzuo02(self):
        '''"专项工作"第1条链接测试'''
        pagehome = ZdzzPage(self.driver)
        zhuanxianggongzuo02Title = pagehome.getText(pagehome.zhuanxianggongzuo02) #获取链接的文本值
        pagehome.click_zhuanxianggongzuo02()   #点击链接
        wait_title(self, zhuanxianggongzuo02Title)
        #切换窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        #判断新页面的title是否与链接的文本值相同
        assert(pagehome.driver.title == zhuanxianggongzuo02Title), "标题不是“%s”，测试不通过" % zhuanxianggongzuo02Title

if __name__ == '__main__':
    unittest.main()