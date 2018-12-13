#!/usr/bin/env python  
# encoding: utf-8

class SeleniumMethod(object):

    def __init__(self, driver):
        self.driver = driver

        #构造函数
    def getTitle(self):
        #获取页面标题
        return self.driver.title

    def clearAndInput(self, location, value):
        #根据xpath，清除并输入
        element = self.driver.find_element_by_xpath(location)
        element.clear()
        element.send_keys(value)

    def click(self, location):
        return self.driver.find_element_by_xpath(location).click()

    def getText(self, location):
        #根据xpth获取文本值
        return self.driver.find_element_by_xpath(location).text
