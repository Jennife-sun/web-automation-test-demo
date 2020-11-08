import unittest           #导入unittest测试模块，Python自动带的单元测试模块
from selenium import webdriver
from log import Log

l = Log('../report/test.log')
class TestDemo(unittest.TestCase):                  #创建一个测试类，继承自unittest下面的TestCase类
    def setUp(self) -> None:        #前置方法，在测试用例执行之前执行一遍,固定写法
        #打开浏览器，窗口最大话，打开页面，智能等待
        self.driver = webdriver.Chrome()                                #self.driver类变量
        self.driver.maximize_window()
        self.driver.get('file:///E:/%E4%B8%8A%E8%AF%BE%E8%B5%84%E6%96%99/selenium/demo.html')
        self.driver.implicitly_wait(8)

    def test_input(self):                        #方法名称必须以test开头，这就是一条测试用例
        value = self.driver.find_element_by_id('user').get_attribute('value')
        exp = '请输入内容'
        self.assertEqual(exp, value)    #unittest自带的断言方法，对测试结果进行判断校验，
        # assertEqual判断实际结果与预期结果是否相同,括号前面的表示预期结果，后面表示获取到的结果

    def test_link(self):          #两个测试用例之间执行顺序按照test_名字首字母的英文字母顺序排序
        self.driver.find_element_by_link_text('链接').click()
        title = self.driver.title
        exp = '新窗口'
        try:
            self.assertEqual(exp,title)
            l.info('点击链接跳转成功')
        except AssertionError:
            l.error('点击链接跳转失败，期望结果是:'+exp+",实际结果是："+title)



    def tearDown(self) -> None:         #后置方法，在测试用例执行之后执行一遍，固定写法
        #关闭浏览器，退出驱动程序
        self.driver.quit()




if __name__ == '__main__':      #执行方法
    unittest.main()
