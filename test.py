import os
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.ios import XCUITestOptions
import shutil

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 检查或创建 img 文件夹
        cls.img_dir = os.path.join(os.getcwd(), 'img')
        if not os.path.exists(cls.img_dir):
            os.makedirs(cls.img_dir)
        else:
            # 清空 img 文件夹
            shutil.rmtree(cls.img_dir)
            os.makedirs(cls.img_dir)

        # 设置 capabilities 选项
        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.automation_name = 'XCUITest'
        options.device_name = 'iPhone 14'
        options.platform_version = '16.2'
        options.bundle_id = 'com.apple.Preferences'

        # 启动 Appium driver
        cls.driver = webdriver.Remote(command_executor=appium_server_url, options=options)

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def test_navigate_to_about(self):
        # 1. 点击 "设置" 主菜单项
        settings_item = self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="设置"]')
        self.assertTrue(settings_item.is_displayed(), "'设置' menu item not found")
        settings_item.click()
        print("Successfully clicked '设置' menu item.")

        # 2. 点击 "通用" 菜单项
        general_item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '通用')
        self.assertTrue(general_item.is_displayed(), "'通用' menu item was not found.")
        general_item.click()
        print("Successfully clicked '通用' menu item.")

        # 3. 点击 "关于本机" 菜单项
        about_item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '关于本机')
        self.assertTrue(about_item.is_displayed(), "'关于本机' menu item was not found.")
        about_item.click()
        print("Successfully clicked '关于本机' menu item.")

        # 截图并保存到 img 文件夹
        screenshot_path = os.path.join(self.img_dir, 'about_page.png')
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")


if __name__ == '__main__':
    unittest.main()
