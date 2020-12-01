#！usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from selenium.webdriver.support import expected_conditions as ec
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/myapp.log',
                        filemode='w'
                        )

    def __init__(self,driver:webdriver = None):
        self.driver = driver

    #定义find方法，
    def find(self, by, locator):
        logging.info("find:")
        logging.info(by)
        logging.info(locator)

        return self.driver.find_element(by, locator)

    #定义滑动的方法
    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')
    #定义获取toast提示的方法
    def get_toast_text(self):
        logging.info("get toast:")
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    #定义打开yaml文件的方法
    def open_yaml(self,file_path):
        logging.info("open yaml:")
        logging.info(file_path)
        with open(file_path,encoding="utf-8") as f:
            return yaml.load(f)

    #初始化显式等待wait方法
    def init_wite(self):
        wait = WebDriverWait(self.driver, 10)
        return wait

    #利用显示等待定位单个元素的方法
    def wait_element(self,*value):
        wait = self.init_wite()
        element = wait.until(ec.presence_of_element_located(*value))
        return element

    #利用显式等待方式定位多个元素的方法
    def wait_all_elemenet(self,*value):
        wait = self.init_wite()
        elements = wait.until(ec.presence_of_all_elements_located(*value))
        return elements

    #点击元素的方法
    def click_element(self,element):
        element.click()

    #填写内容的方法
    def send_keys(self,element,value):
        element.send_keys(value)
