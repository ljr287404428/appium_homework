#！usr/bin/python3
# -*- coding: utf-8 -*-
# from second_homework.page.menber_invite_page import MenberInviteMenuPage
from appium.webdriver.common.mobileby import MobileBy

from second_homework.page.base_page import BasePage
from second_homework.page.menber_invite_page import MenberInviteMenuPage


class ContactAddPage(BasePage):

    def edit_contact(self,name,gender,phonenum):
        '''
        编辑成员信息
        :return:
        '''

        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        return MenberInviteMenuPage(self.driver)