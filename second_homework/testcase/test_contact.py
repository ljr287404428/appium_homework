# ！usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep

import pytest

from second_homework.page.app import App
from second_homework.page.base_page import BasePage


class TestContact:

    # 实例化App类对象
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_mian()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", BasePage().open_yaml(r"../page/add_contact.yaml"))
    def test_addcontact(self, name, gender, phonenum):
        result = self.main.goto_contactlist() \
            .add_member().add_member_manul().edit_contact(name, gender, phonenum) \
            .verify_toast()
        assert result == "添加成功"

    def test_delcontact(self):
        name = "hogwarts"
        ele = self.main.goto_contactlist().click_search()
        elements =ele.search_result(name)
        sleep(1)
        print(elements)
        beforenum = len(elements)
        sleep(3)
        if beforenum < 2:
            print("没有可删除的人员")
            return
        sleep(1)
        elements_1 = ele.del_contact(elements[1],name).search_result()
        afternum = len(elements_1)
        assert afternum == beforenum - 1

