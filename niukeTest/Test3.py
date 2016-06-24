# -*- coding: utf-8 -*-

class A(object):
    def __init__(self):
        self.requestType = {
            "method": "GET",
            "renderJs": "true",
            "formData": {},
            "headers": {
                "Cookie": {},
                "Referer": ""
            }
        }
        self.b = None


class B(A):
    def __init__(self, c, d, e):
        super(B, self).__init__("sdf", "sdafas")
        self.c = c
        self.d = d
        self.e = e

    def test(self):
        print self.a


if __name__ == '__main__':
    s = A.test()
    ss = A().test()

    print 'ssss'
    print 'dasfs'
