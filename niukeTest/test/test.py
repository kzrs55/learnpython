# -*- coding: utf-8 -*-

class Solution:
    def Fibonacci(self, n):
        # write code here
        a = [0,1,1]
        if n < 3 :
            return a[n]
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)

if __name__ == '__main__':
    ss = raw_input("ss:")
    print Solution().Fibonacci(ss)