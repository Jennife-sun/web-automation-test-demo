import unittest
import HTMLTestRunner


testsuit = unittest.TestSuite()            #实体化unittest模块下面的测试集这个（功能）类，用一个变量testsuit装它
#cases = [TestBaiDu('test_sousuo'),TestDemo('test_input'),TestDemo('test_link')]    #用一个列表cases去统一装
# 其他测试用例，引用别的模块里的测试用例就是类名（'函数'），这是一个一个获取
cases = unittest.defaultTestLoader.discover('.','test_*.py')   #这是批量的获取指定目录下面所有的测试用例
testsuit.addTests(cases)        #这里是把这些测试用例加入到测试集，也就是调用TestSuite()类里的函数addTests()
# runner = unittest.TextTestRunner()     #实体化一个运行器
htmi_file = open('../report/test_result.html','wb')     #吧测试结果生成一个HTML报告
runner = HTMLTestRunner.HTMLTestRunner(stream=htmi_file,title='测试演示报告',description='自动化测试演示报告')
runner.run(testsuit)       #执行测试集    也就是调用TextTestRunner()这个类里的run()函数




