#!/usr/bin/env python  
# encoding: utf-8

import sys
from basePage import ZdzzPage
sys.path.append("./models")
from models.myunit import *

class NavigationTest(MyTest):
    '''省厅网站一级导航栏测试'''
    def test01_click_homepageBotton(self):
        '''"首页"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_homepageBotton()
        wait_title(self, pagehome.homepageTitle)
        assert(pagehome.driver.title == pagehome.homepageTitle), "标题不是“首页标题”，测试不通过"

    def test02_click_zdProfile(self):
        '''"总队概况"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zdProfile()
        wait_title(self, pagehome.zdProfileTitle)
        assert(pagehome.driver.title == pagehome.zdProfileTitle), "标题不是“总队概况”，测试不通过"

    def test03_click_flfg(self):
        '''"法律法规"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_flfg()
        wait_title(self, pagehome.flfgTitle)
        assert(pagehome.driver.title == pagehome.flfgTitle), "标题不是“法律法规”，测试不通过"

    def test04_click_zdSubmission(self):
        '''"信息投稿"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zdSubmission()
        wait_title(self, pagehome.zdSubmissionTitle)
        assert(pagehome.driver.title == pagehome.zdSubmissionTitle), "标题不是“信息投稿”，测试不通过"

    def test05_click_gzjb(self):
        '''"工作简报"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_gzjb()
        wait_title(self, pagehome.gzjbTitle)
        assert(pagehome.driver.title == pagehome.gzjbTitle), "标题不是“工作简报”，测试不通过"

    def test06_click_zdUploadfile(self):
        '''"文件上传"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zdUploadfile()
        wait_title(self, pagehome.zdUploadfileTitle)
        assert(pagehome.driver.title == pagehome.zdUploadfileTitle), "标题不是“文件上传”，测试不通过"

    def test07_click_wjxz(self):
        '''"文件下载"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_wjxz()
        wait_title(self, pagehome.wjxzTitle)
        assert(pagehome.driver.title == pagehome.wjxzTitle), "标题不是“文件下载”，测试不通过"

    def test08_click_zdnw(self):
        '''"总队内网"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_zdnw()
        wait_title(self, pagehome.zdnwTitle)
        #第一种切换窗口的方法
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                break
        assert(pagehome.driver.title == pagehome.zdnwTitle),"标题不是“总队内网”，测试不通过"

    def test09_click_manage(self):
        '''"后台管理"按钮测试'''
        pagehome = ZdzzPage(self.driver)
        pagehome.click_manage()
        wait_title(self, pagehome.manageTitle)
        #第二种切换窗口的方法
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        assert(pagehome.driver.title == pagehome.manageTitle), "标题不是“后台管理”，测试不通过"

if __name__ == '__main__':
    unittest.main()