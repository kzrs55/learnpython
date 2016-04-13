from django.core.urlresolvers import resolve
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
