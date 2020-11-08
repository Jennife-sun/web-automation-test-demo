import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestBaiDu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get('https://www.baidu.com/')

    def test_sousuo(self):
        self.driver.find_element_by_id('kw').send_keys('帅哥',Keys.ENTER)
        time.sleep(3)
        contain = '帅哥'
        source = self.driver.page_source
        self.driver.get_screenshot_as_file('report/shuaige.png')
        self.assertIn(contain,source)

    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
