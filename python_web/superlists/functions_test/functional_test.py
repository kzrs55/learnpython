# coding=utf-8
import unittest

from selenium import webdriver

__author__ = 'zjutK'


class NewVisitorTest(unittest.TestCase):
    def setUp(self):  # 测试之前
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30) # 等待三秒钟使得内容出现

    def tearDown(self):  # 测试之后
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # 名字以test_开头的都是测试
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome', self.browser.title)
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')  # warnings='ignore' 抛出异常
