from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from first_homework.base import Base


class Test_workWX:

    def setup(self):
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

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("name,gender,phonenum", Base().open_yaml())
    def test_contact(self, name, gender, phonenum):
        # 点击【通讯录】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # toast 提示进行断言
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"

    def test_del_contact(self):
        name = "hogwarts"
        # 显性等待，初始化webdriver
        wait = WebDriverWait(self.driver, 10)
        # 定位通讯录并点击
        wait.until(ec.element_to_be_clickable((MobileBy.XPATH, "//*[@text='通讯录']"))).click()
        # 查找搜索按钮，并点击
        wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/i6n"))).click()
        # 定位搜索框，并输入需要查询的姓名
        wait.until(ec.presence_of_element_located((MobileBy.ID, "com.tencent.wework:id/gpg"))).send_keys(name)
        sleep(3)
        # 使用XPATH定位，定位筛选符合条件的所有元素
        search_list = wait.until(
            ec.presence_of_all_elements_located((MobileBy.XPATH, "//*[contains(@text,'%s')]" % name)))
        # 判断查到list长度，如果为1，则没有符合条件的姓名
        print(len(search_list))
        sleep(1)
        if len(search_list) == 1:
            raise Exception("没有符合条件的删除对象，请查证后重新输入")
        # 如果list大于1时，则需要需求进行判断
        else:
            sleep(1)
            for index in range(1, len(search_list)):
                sleep(1)
                # 点击该元素
                search_list[1].click()
                # 定位个人信息页面中右上角中的三个点
                wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/i6d"))).click()
                # 定位编辑成员按钮并点击
                wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/b_x"))).click()
                # 定位删除按钮
                wait.until(ec.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/elh"))).click()
                # 点击弹窗中的确定按钮
                wait.until(ec.element_to_be_clickable((MobileBy.XPATH, "//*[@class='android.widget.LinearLayout']"
                                                                       "//android.widget.TextView[2]"))).click()
        sleep(1)
        # 使用XPATH定位，定位筛选符合条件的所有元素
        search_list_1 = wait.until(
            ec.presence_of_all_elements_located((MobileBy.XPATH, "//*[contains(@text,'%s')]" % name)))
        assert len(search_list_1) == 1
