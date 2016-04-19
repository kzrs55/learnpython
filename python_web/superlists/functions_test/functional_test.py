# coding=utf-8
import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

__author__ = 'zjutK'


class NewVisitorTest(unittest.TestCase):
    def setUp(self):  # 测试之前
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)  # 等待三秒钟使得内容出现

    def tearDown(self):  # 测试之后
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # 名字以test_开头的都是测试
        self.browser.get('http://localhost:8000')
        # 网页的标题和头部都包含To-Do这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        # 文本框输入'Buy peacock feathers'
        inputbox.send_keys('Buy peacock feathers')
        # 按下更新,页面显示更新
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(rows.text == '1: Buy peacock feathers' for rows in rows),
                "New to-do item did not appear in table"
        )
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')  # warnings='ignore' 抛出异常
