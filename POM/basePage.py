#!/usr/bin/env python  
# encoding: utf-8

from WebDriverMethod import SeleniumMethod

class ZdzzPage(SeleniumMethod):

    #一级导航栏btn Xpath

    homepageBotton = '//*[@id="webnav"]/li[1]/a'
    homepageTitle = "浙江治安监督管理信息网"

    zdProfile = '//*[@id="webnav"]/li[2]/a'
    zdProfileTitle = "总队概况"

    flfg = '//*[@id="webnav"]/li[3]/a'
    flfgTitle = "法律法规"

    zdSubmission = '//*[@id="webnav"]/li[4]/a'
    zdSubmissionTitle = "信息投稿"

    gzjb = '//*[@id="webnav"]/li[5]/a'
    gzjbTitle = "工作简报"

    zdUploadfile = '//*[@id="webnav"]/li[6]/a'
    zdUploadfileTitle = "文件上传"

    wjxz = '//*[@id="webnav"]/li[7]/a'
    wjxzTitle = "文件下载"

    zdnw = '//*[@id="webnav"]/li[8]/a'
    zdnwTitle = "总队内网"

    manage = '//*[@id="webnav"]/li[9]/a'
    manageTitle = "登录"

    duty = '/html/body/div/div[3]/div[2]/a[1]/span'
    dutyTitle = '值班安排'

    search = '//*[@id="search"]'
    searchTitle = '总队主站'

    #新闻栏
    news01 = "/html/body/div/div[5]/div[2]/div/ul/li[1]/span[1]/a"
    news02 = '/html/body/div/div[5]/div[2]/div/ul/li[2]/span[1]/a'
    news03 = '/html/body/div/div[5]/div[2]/div/ul/li[3]/span[1]/a'
    news04 = '/html/body/div/div[5]/div[2]/div/ul/li[4]/span[1]/a'
    news05 = '/html/body/div/div[5]/div[2]/div/ul/li[5]/span[1]/a'
    news06 = '/html/body/div/div[5]/div[2]/div/ul/li[6]/span[1]/a'

    #通知通报栏
    tongzhitongbao = '/html/body/div/div[6]/div[1]/div[1]/ul/li[1]'
    tongzhitongbao01 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[1]/span[1]/a'
    tongzhitongbao02 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[2]/span[1]/a'
    tongzhitongbao03 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[3]/span[1]/a'
    tongzhitongbao04 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[4]/span[1]/a'
    tongzhitongbao05 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[5]/span[1]/a'
    tongzhitongbao06 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[6]/span[1]/a'
    tongzhitongbao07 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[7]/span[1]/a'
    tongzhitongbao08 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[8]/span[1]/a'
    tongzhitongbao09 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[9]/span[1]/a'
    tongzhitongbao10 = '/html/body/div/div[6]/div[1]/div[1]/div[1]/ul/li[10]/span[1]/a'
    tongzhitongbao_more = '/html/body/div/div[6]/div[1]/div[1]/div[1]/a'
    tongzhitongbao_more_title = '通知通报'

    #工作动态栏
    gongzuodongtai = '/html/body/div/div[6]/div[1]/div[1]/ul/li[2]'
    gongzuodongtai01 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[1]/span[1]/a'
    gongzuodongtai02 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[2]/span[1]/a'
    gongzuodongtai03 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[3]/span[1]/a'
    gongzuodongtai04 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[4]/span[1]/a'
    gongzuodongtai05 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[5]/span[1]/a'
    gongzuodongtai06 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[6]/span[1]/a'
    gongzuodongtai07 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[7]/span[1]/a'
    gongzuodongtai08 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[8]/span[1]/a'
    gongzuodongtai09 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[9]/span[1]/a'
    gongzuodongtai10 = '/html/body/div/div[6]/div[1]/div[1]/div[2]/ul/li[10]/span[1]/a'
    gongzuodongtai_more = '/html/body/div/div[6]/div[1]/div[1]/div[2]/a'
    gongzuodongtai_more_title = '工作动态'

    #领导讲话栏
    lingdaojianghua = '/html/body/div/div[6]/div[1]/div[2]/ul/li[1]'
    lingdaojianghua01 = '/html/body/div/div[6]/div[1]/div[2]/div[1]/ul/li[1]/span[1]/a'
    lingdaojianghua02 = '/html/body/div/div[6]/div[1]/div[2]/div[1]/ul/li[2]/span[1]/a'
    lingdaojianghua03 = '/html/body/div/div[6]/div[1]/div[2]/div[1]/ul/li[3]/span[1]/a'
    lingdaojianghua04 = '/html/body/div/div[6]/div[1]/div[2]/div[1]/ul/li[4]/span[1]/a'
    lingdaojianghua05 = '/html/body/div/div[6]/div[1]/div[2]/div[1]/ul/li[5]/span[1]/a'
    lingdaojianghua06 = '/html/body/div/div[6]/div[1]/div[2]/div[1]/ul/li[6]/span[1]/a'
    lingdaojianghua_more = '/html/body/div/div[6]/div[1]/div[2]/div[1]/a'
    lingdaojianghua_more_title = '领导讲话'

    #重要文件栏
    zhongyaowenjian = '/html/body/div/div[6]/div[1]/div[2]/ul/li[2]'
    zhongyaowenjian01 = '/html/body/div/div[6]/div[1]/div[2]/div[2]/ul/li[1]/span[1]/a'
    zhongyaowenjian02 = '/html/body/div/div[6]/div[1]/div[2]/div[2]/ul/li[2]/span[1]/a'
    zhongyaowenjian03 = '/html/body/div/div[6]/div[1]/div[2]/div[2]/ul/li[3]/span[1]/a'
    zhongyaowenjian04 = '/html/body/div/div[6]/div[1]/div[2]/div[2]/ul/li[4]/span[1]/a'
    zhongyaowenjian05 = '/html/body/div/div[6]/div[1]/div[2]/div[2]/ul/li[5]/span[1]/a'
    zhongyaowenjian06 = '/html/body/div/div[6]/div[1]/div[2]/div[2]/ul/li[6]/span[1]/a'
    zhongyaowenjian_more = '/html/body/div/div[6]/div[1]/div[2]/div[2]/a'
    zhongyaowenjian_more_title = '重要文件'

    #调研工作栏
    diaoyangongzuo = '/html/body/div/div[6]/div[1]/div[3]/ul/li[1]'
    diaoyangongzuo01 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[1]/span[1]/a'
    diaoyangongzuo02 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[2]/span[1]/a'
    diaoyangongzuo03 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[3]/span[1]/a'
    diaoyangongzuo04 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[4]/span[1]/a'
    diaoyangongzuo05 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[5]/span[1]/a'
    diaoyangongzuo06 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[6]/span[1]/a'
    diaoyangongzuo07 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[7]/span[1]/a'
    diaoyangongzuo08 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[8]/span[1]/a'
    diaoyangongzuo09 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[9]/span[1]/a'
    diaoyangongzuo10 = '/html/body/div/div[6]/div[1]/div[3]/div[1]/ul/li[10]/span[1]/a'
    diaoyangongzuo_more = '/html/body/div/div[6]/div[1]/div[3]/div[1]/a'
    diaoyangongzuo_more_title = '调研工作'

    #社会聚焦栏
    shehuijujiao = '/html/body/div/div[6]/div[1]/div[3]/ul/li[2]'
    shehuijujiao01 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[1]/span[1]/a'
    shehuijujiao02 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[2]/span[1]/a'
    shehuijujiao03 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[3]/span[1]/a'
    shehuijujiao04 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[4]/span[1]/a'
    shehuijujiao05 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[5]/span[1]/a'
    shehuijujiao06 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[6]/span[1]/a'
    shehuijujiao07 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[7]/span[1]/a'
    shehuijujiao08 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[8]/span[1]/a'
    shehuijujiao09 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[9]/span[1]/a'
    shehuijujiao10 = '/html/body/div/div[6]/div[1]/div[3]/div[2]/ul/li[10]/span[1]/a'
    shehuijujiao_more = '/html/body/div/div[6]/div[1]/div[3]/div[2]/a'
    shehuijujiao_more_title = '社会聚焦'

    #专项工作栏
    zhuanxianggongzuo01 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[1]/a/div[2]'
    zhuanxianggongzuo02 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[2]/a/div[2]'
    zhuanxianggongzuo03 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[3]/a/div[2]'
    zhuanxianggongzuo04 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[4]/a/div[2]'
    zhuanxianggongzuo05 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[5]/a/div[2]'
    zhuanxianggongzuo06 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[6]/a/div[2]'
    zhuanxianggongzuo07 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[7]/a/div[2]'
    zhuanxianggongzuo08 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[8]/a/div[2]'
    zhuanxianggongzuo09 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[9]/a/div[2]'
    zhuanxianggongzuo10 = '/html/body/div/div[6]/div[2]/div[4]/div[2]/ul/li[10]/a/div[2]'

    def click_homepageBotton(self):
        self.click(self.homepageBotton)

    def click_zdProfile(self):
        self.click(self.zdProfile)

    def click_flfg(self):
        self.click(self.flfg)

    def click_zdSubmission(self):
        self.click(self.zdSubmission)

    def click_gzjb(self):
        self.click(self.gzjb)

    def click_zdUploadfile(self):
        self.click(self.zdUploadfile)

    def click_wjxz(self):
        self.click(self.wjxz)

    def click_zdnw(self):
        self.click(self.zdnw)

    def click_manage(self):
        self.click(self.manage)

    def click_duty(self):
        self.click(self.duty)

    def click_search(self):
        self.click(self.search)

    def click_news01(self):
        self.click(self.news01)

    def click_news02(self):
        self.click(self.news02)

    def click_news03(self):
        self.click(self.news03)

    def click_news04(self):
        self.click(self.news04)

    def click_news05(self):
        self.click(self.news05)

    def click_news06(self):
        self.click(self.news06)

    def click_tongzhitongbao(self):
        self.click(self.tongzhitongbao)

    def click_tongzhitongbao01(self):
        self.click(self.tongzhitongbao01)

    def click_tongzhitongbao02(self):
        self.click(self.tongzhitongbao02)

    def click_tongzhitongbao03(self):
        self.click(self.tongzhitongbao03)

    def click_tongzhitongbao04(self):
        self.click(self.tongzhitongbao04)

    def click_tongzhitongbao05(self):
        self.click(self.tongzhitongbao05)

    def click_tongzhitongbao06(self):
        self.click(self.tongzhitongbao06)

    def click_tongzhitongbao07(self):
        self.click(self.tongzhitongbao07)

    def click_tongzhitongbao08(self):
        self.click(self.tongzhitongbao08)

    def click_tongzhitongbao09(self):
        self.click(self.tongzhitongbao09)

    def click_tongzhitongbao10(self):
        self.click(self.tongzhitongbao10)

    def click_tongzhitongbao_more(self):
        self.click(self.tongzhitongbao_more)

    def click_gongzuodongtai(self):
        self.click(self.gongzuodongtai)

    def click_gongzuodongtai01(self):
        self.click(self.gongzuodongtai01)

    def click_gongzuodongtai02(self):
        self.click(self.gongzuodongtai02)

    def click_gongzuodongtai03(self):
        self.click(self.gongzuodongtai03)

    def click_gongzuodongtai04(self):
        self.click(self.gongzuodongtai04)

    def click_gongzuodongtai05(self):
        self.click(self.gongzuodongtai05)

    def click_gongzuodongtai06(self):
        self.click(self.gongzuodongtai06)

    def click_gongzuodongtai07(self):
        self.click(self.gongzuodongtai07)

    def click_gongzuodongtai08(self):
        self.click(self.gongzuodongtai08)

    def click_gongzuodongtai09(self):
        self.click(self.gongzuodongtai09)

    def click_gongzuodongtai10(self):
        self.click(self.gongzuodongtai10)

    def click_gongzuodongtai_more(self):
        self.click(self.gongzuodongtai_more)

    def click_lingdaojianghua(self):
        self.click(self.lingdaojianghua)

    def click_lingdaojianghua01(self):
        self.click(self.lingdaojianghua01)

    def click_lingdaojianghua02(self):
        self.click(self.lingdaojianghua02)

    def click_lingdaojianghua03(self):
        self.click(self.lingdaojianghua03)

    def click_lingdaojianghua04(self):
        self.click(self.lingdaojianghua04)

    def click_lingdaojianghua05(self):
        self.click(self.lingdaojianghua05)

    def click_lingdaojianghua06(self):
        self.click(self.lingdaojianghua06)

    def click_lingdaojianghua_more(self):
        self.click(self.lingdaojianghua_more)

    def click_zhongyaowenjian(self):
        self.click(self.zhongyaowenjian)

    def click_zhongyaowenjian01(self):
        self.click(self.zhongyaowenjian01)

    def click_zhongyaowenjian02(self):
        self.click(self.zhongyaowenjian02)

    def click_zhongyaowenjian03(self):
        self.click(self.zhongyaowenjian03)

    def click_zhongyaowenjian04(self):
        self.click(self.zhongyaowenjian04)

    def click_zhongyaowenjian05(self):
        self.click(self.zhongyaowenjian05)

    def click_zhongyaowenjian06(self):
        self.click(self.zhongyaowenjian06)

    def click_zhongyaowenjian_more(self):
        self.click(self.zhongyaowenjian_more)

    def click_diaoyangongzuo(self):
        self.click(self.diaoyangongzuo)

    def click_diaoyangongzuo01(self):
        self.click(self.diaoyangongzuo01)

    def click_diaoyangongzuo02(self):
        self.click(self.diaoyangongzuo02)

    def click_diaoyangongzuo03(self):
        self.click(self.diaoyangongzuo03)

    def click_diaoyangongzuo04(self):
        self.click(self.diaoyangongzuo04)

    def click_diaoyangongzuo05(self):
        self.click(self.diaoyangongzuo05)

    def click_diaoyangongzuo06(self):
        self.click(self.diaoyangongzuo06)

    def click_diaoyangongzuo07(self):
        self.click(self.diaoyangongzuo07)

    def click_diaoyangongzuo08(self):
        self.click(self.diaoyangongzuo08)

    def click_diaoyangongzuo09(self):
        self.click(self.diaoyangongzuo09)

    def click_diaoyangongzuo10(self):
        self.click(self.diaoyangongzuo10)

    def click_diaoyangongzuo_more(self):
        self.click(self.diaoyangongzuo_more)

    def click_shehuijujiao(self):
        self.click(self.shehuijujiao)

    def click_shehuijujiao01(self):
        self.click(self.shehuijujiao01)

    def click_shehuijujiao02(self):
        self.click(self.shehuijujiao02)

    def click_shehuijujiao03(self):
        self.click(self.shehuijujiao03)

    def click_shehuijujiao04(self):
        self.click(self.shehuijujiao04)

    def click_shehuijujiao05(self):
        self.click(self.shehuijujiao05)

    def click_shehuijujiao06(self):
        self.click(self.shehuijujiao06)

    def click_shehuijujiao07(self):
        self.click(self.shehuijujiao07)

    def click_shehuijujiao08(self):
        self.click(self.shehuijujiao08)

    def click_shehuijujiao09(self):
        self.click(self.shehuijujiao09)

    def click_shehuijujiao10(self):
        self.click(self.shehuijujiao10)

    def click_shehuijujiao_more(self):
        self.click(self.shehuijujiao_more)

    def click_zhuanxianggongzuo01(self):
        self.click(self.zhuanxianggongzuo01)

    def click_zhuanxianggongzuo02(self):
        self.click(self.zhuanxianggongzuo02)

    def click_zhuanxianggongzuo03(self):
        self.click(self.zhuanxianggongzuo03)

    def click_zhuanxianggongzuo04(self):
        self.click(self.zhuanxianggongzuo04)

    def click_zhuanxianggongzuo05(self):
        self.click(self.zhuanxianggongzuo05)

    def click_zhuanxianggongzuo06(self):
        self.click(self.zhuanxianggongzuo06)

    def click_zhuanxianggongzuo07(self):
        self.click(self.zhuanxianggongzuo07)

    def click_zhuanxianggongzuo08(self):
        self.click(self.zhuanxianggongzuo08)

    def click_zhuanxianggongzuo09(self):
        self.click(self.zhuanxianggongzuo09)

    def click_zhuanxianggongzuo10(self):
        self.click(self.zhuanxianggongzuo10)