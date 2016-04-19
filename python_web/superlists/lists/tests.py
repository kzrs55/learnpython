from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page


# Create your tests here.


# class SmokeTest(TestCase):
# def test_bad_math(self):
#     self.assertEqual(1+1,3) #测试代码,运转错误

class HomePageTest(TestCase):
    def test_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)  # 解析网站跟路径,解析网站是否能够找到名为home_page的函数

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # 创建HttpRequest对象
        response = home_page(request)  # 讲这个对象传给home_page视图
        self.assertTrue(response.content.startswith(b'<html>'))  # 希望开头是...
        self.assertIn(b'<title>To-Do lists</title>', response.content)  # 希望有一个<title>标签,其内容包含单词..
        self.assertTrue(response.content.endswith(b'</html>'))  # 断言希望结尾是...

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
                'home.html',
                {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(),expected_html)
