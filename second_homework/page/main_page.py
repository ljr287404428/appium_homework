#！usr/bin/python3
# -*- coding: utf-8 -*-

#定义主界面类
from appium.webdriver.common.mobileby import MobileBy

from second_homework.page.base_page import BasePage
from second_homework.page.contact_list_page import ContactListPage


class MainPage(BasePage):

    _by = MobileBy.XPATH
    _local = "//*[@text='通讯录']"

    def goto_contactlist(self):
        '''
        进入到通讯录界面
        :return:
        '''
        # 点击【通讯录】
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find(self._by,self._local).click()
        return ContactListPage(self.driver)