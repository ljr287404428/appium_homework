# ！usr/bin/python3
# -*- coding: utf-8 -*-
from appium import webdriver
from second_homework.page.base_page import BasePage
from second_homework.page.main_page import MainPage


# app.py 存放app相关的操作，启动app, 关闭app, 启动app, 进入到主页
class App(BasePage):

    def start(self):
        if self.driver == None:
            capabilities = {
                "platformName": "android",
                "platformVersion": "6.0.1",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
            self.driver.implicitly_wait(50)
        else:
            # 启动app, 启动的页面是desirecaps 里面设置的activity
            self.driver.launch_app()
        # 返回的是当前页
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        pass

    def goto_mian(self):
        return MainPage(self.driver)
