#coding:utf-8

from pythonTechnologys.advancedTechnology.modules.unittest.Widget import Widget  # 导入测试类模块Widget
import unittest  # 导入unittest模块


class WidgetTestCase(unittest.TestCase):
    # 让所有执行测试的类都继承于TestCase类，可以将TestCase看成是对特定类进行测试的方法的集合

    # 在setUp()方法中进行测试前的初始化工作。
    def setUp(self):
        self.widget = Widget()

        # 并在tearDown()方法中执行测试后的清除工作，setUp()和tearDown()都是TestCase类中定义的方法。

    def tearDown(self):
        self.widget = None

    # 测试Widget类中getSize方法
    def testgetSize(self):
        print("Test GetSize")
        # 对Widget类中getSize()方法的返回值和预期值进行比较，确保两者是相等的，
        # assertEqual()也是TestCase类中定义的方法。
        self.assertEqual(self.widget.getSize(), (40, 40))

        # 测试Widget类中reSize方法

    def testreSize(self):
        print("Test Resize")
        # 对Widget类中reSize()方法的返回值和预期值进行比较，确保两者是相等的。
        # assertEqual()也是TestCase类中定义的方法。
        self.assertEqual(self.widget.reSize(50, 100), (50, 100))


        # 提供名为suite()的全局方法，PyUnit在执行测试的过程调用suit()方法来确定有多少个测试用例需要被执行，


# 可以将TestSuite看成是包含所有测试用例的一个容器。
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testgetSize"))  # 往此添加需要测试的方法testgetSize()
    suite.addTest(WidgetTestCase("testreSize"))  # 往此添加需要测试的方法testreSize()
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest='suite')  # 在主函数中调用全局方法.







