#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
from PIL import Image
from time import sleep
import pytesseract

class Apply():
    def __init__(self, NetID, pwd):
        self.NetID = NetID
        self.pwd = pwd
        try:
            self.main()
        except:
            self.__del__()

    def __del__(self):
        self.driver.quit()

    def getCaptcha(self, filePath = 'captcha'):
        # 识别
        text = pytesseract.image_to_string(filePath + '.png', config='--psm 7')
        text = text.replace(' ', '')[0:-2]
        return text[0:4]

    def login(self, captcha):
        self.driver.find_element_by_id('username').send_keys(self.NetID)
        self.driver.find_element_by_id('password').send_keys(self.pwd)
        self.driver.find_element_by_id('captcha').send_keys(captcha)
        self.driver.find_element_by_name('submit').click()

    def waituntil(self, by, value, time = 5):
        while time:
            elements = self.driver.find_elements(by, value)
            if len(elements):
                return True
            else:
                time -= 1
                sleep(1)
        return False

    def main(self):
        # 100% 缩放情况下使用
        self.driver = webdriver.Firefox()
        self.driver.get(r'http://jksb.sysu.edu.cn/infoplus/form/XNYQSB/start')
        self.driver.set_window_size(900, 900)
        self.waituntil('id', 'username')
        x = 436
        y = 407
        dx = 90
        dy = 32
        while True:
            self.driver.save_screenshot('printscreen.png')
            rangle = (x, y, x + dx, y + dy)
            i = Image.open("../../../../PycharmProjects/apply/printscreen.png")  # 打开截图
            i.crop(rangle).save('captcha.png') # 保存我们接下来的验证码图片 进行打码
            captcha = self.getCaptcha()
            print('captcha is %s' % captcha)
            self.login(captcha) # 尝试登陆
            if not self.waituntil('xpath', "//*[text()='验证码不正确 ']"):
                break
            y = 454

        self.driver.maximize_window()

        self.waituntil('xpath', '//nobr[text()="下一步"]')
        self.driver.find_element_by_xpath("//nobr[text()='下一步']").click() # 进入表单

        self.driver.find_element_by_class_name('command_button_content').click() # 提交
        self.waituntil('xpath', '//*[@class="dialog_footer"]/button')
        self.driver.find_element_by_xpath('//*[@class="dialog_footer"]/button').click()

        try:
            # 如果有未打钩的情况下需要再执行多一步
            self.driver.find_element_by_id('V1_CTRL82').click()
            self.waituntil('xpath', '//*[@class="dialog_footer"]/button')
            self.driver.find_element_by_xpath('//*[@class="dialog_footer"]/button').click()
        except:
            pass

if __name__ == '__main__':
    apply = Apply('你的NetID', '密码')