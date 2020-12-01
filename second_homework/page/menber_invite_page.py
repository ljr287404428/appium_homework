#！usr/bin/python3
# -*- coding: utf-8 -*-
# from second_homework.page.contact_add_page import ContactAddPage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from second_homework.page.base_page import BasePage


class MenberInviteMenuPage(BasePage):

    def add_member_manul(self):
        '''
        点击手动输入添加方法
        :return:
        '''
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from second_homework.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def verify_toast(self):
        '''
        在这个界面获取toast提示
        :return:
        '''
        # toast 提示进行断言
        # result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()

        return result