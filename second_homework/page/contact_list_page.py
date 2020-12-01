#！usr/bin/python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from second_homework.page.base_page import BasePage
# from second_homework.page.menber_invite_page import MenberInviteMenuPage
from second_homework.page.search_list_page import SearchListPage


class ContactListPage(BasePage):

    def add_member(self):
        '''
        点击添加成员
        :return:
        '''
        # 点击【添加成员】
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        self.find_by_scroll("添加成员").click()
        from second_homework.page.menber_invite_page import MenberInviteMenuPage
        return MenberInviteMenuPage(self.driver)

    #点击搜索，返回搜索页面的结果
    def click_search(self):
        element = self.wait_element((MobileBy.XPATH,"//android.widget.RelativeLayout/android.widget"
                                          ".LinearLayout[2]/android.widget."
                                          "RelativeLayout[1]/android.widget.TextView"))
        self.click_element(element)
        return SearchListPage(self.driver)