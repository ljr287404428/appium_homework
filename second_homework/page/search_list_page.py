# -*- coding:utf-8 -*-
# @Time   : 2020/12/1 22:39
# @Autor  : LL
# @File  :  search_list_page.py
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from second_homework.page.base_page import BasePage


class SearchListPage(BasePage):

    # 定位搜索输入框并填写需要搜索的姓名，查找搜索的结果
    def search_result(self, name):
        element = self.wait_element((MobileBy.ID, "com.tencent.wework:id/gpg"))
        element.clear()
        self.send_keys(element, name)
        sleep(2)
        elements = self.wait_all_elemenet((MobileBy.XPATH, f"//*[contains(@text,'{name}')]"))
        return elements


    # 定义整个删除的流程方法
    def del_contact(self, element, name):
        # elements = self.search_result(name)
        # # 判断查到list长度，如果为1，则没有符合条件的姓名
        # if len(elements) == 1:
        #     print("没有符合条件的删除对象，请查证后重新输入")
        #     return
        # # 如果list大于1时，则需要需求进行判断
        # else:
        #     for index in range(1, len(elements)):

        # 点击该元素
        element.click()
        # 定位个人信息页面中右上角中的三个点
        # wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/i6d"))).click()
        ele1 = self.wait_element((MobileBy.ID, "com.tencent.wework:id/i6d"))
        self.click_element(ele1)
        # 定位编辑成员按钮并点击
        # wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/b_x"))).click()
        ele2 = self.wait_element((MobileBy.ID, "com.tencent.wework:id/b_x"))
        self.click_element(ele2)
        # 定位删除按钮
        # wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/elh"))).click()
        ele3 = self.wait_element((MobileBy.ID, "com.tencent.wework:id/elh"))
        self.click_element(ele3)
        # 点击弹窗中的确定按钮
        # wait.until(ec.element_to_be_clickable((MobileBy.XPATH, "//*[@class='android.widget.LinearLayout']"
        # "//android.widget.TextView[2]"))).click()
        ele4 = self.wait_element((MobileBy.XPATH, "//*[@class='android.widget.LinearLayout']"
                                                  "//android.widget.TextView[2]"))
        self.click_element(ele4)
        sleep(1)
        return self
