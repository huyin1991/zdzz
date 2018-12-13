#!/usr/bin/env python  
# encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
import unittest, time, os

def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 邮箱相关参数
    smtpserver = "smtp.exmail.qq.com"
    sender = 'huyin@gakm.net'    #发送人的邮箱
    recevier = '363468616@qq.com'  #接收人的邮箱
    username = 'huyin@gakm.net'  #发送人的邮箱账号
    password = 'password'        #发送人的邮箱密码

    # 创建实例
    msg = MIMEMultipart()
    msg['Subject'] = Header('自动化测试报告', 'utf-8')  #创建邮件标题

    msg.attach(MIMEText('自动化测试已完成，请查收附件内的测试报告！', 'plain', 'utf-8')) #邮件正文内容

    #发送html附件
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file["Content-Type"] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment;filename=%s' % filename_now
    msg.attach(msg_file)

    # 发送邮件，并做异常处理
    #msg['from'] = sender
    #msg['to'] = recevier
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, recevier, msg.as_string())
        smtp.quit()
        print('邮件发送成功!')
    except smtplib.SMTPException:
        print("邮件发送失败！")

#获取最新的报告
def new_report(testreport):
    #方式1
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

    #方式2
    #dirs = os.listdir(testreport)
    #dirs.sort()
    #newreportname = dirs[-1]
    #print('最新报告的名称为：{0}'.format(newreportname))
    #file_new = os.path.join(testreport, newreportname)
    #return file_new

if __name__ == '__main__':
    test_dir = os.path.join(os.getcwd(), 'test_case')  #获取test_case路径
    test_report = os.path.join(os.getcwd(), 'report')   #获取report路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  #获取所有test开头的case
    now = time.strftime("%Y-%m-%d %H-%M-%S")   #获取当前时间
    filename = test_report + '\\' + now + 'result.html'  #生成报告名称
    filename_now = now + 'result.html'
    #生成html测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
        title='浙江省治安监督管理信息网自动化测试报告',
        description='用例执行人员: huyin  ')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)