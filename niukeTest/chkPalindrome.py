#coding=utf-8
__author__ = 'zjutK'
'''
对于一个链表，请设计一个时间复杂度为O(n),额外空间复杂度为O(1)的算法，判断其是否为回文结构。
给定一个链表的头指针A，请返回一个bool值，代表其是否为回文结构。保证链表长度小于等于900。
测试样例：
1->2->2->1
返回：true
'''
class PalindromeList:
    def chkPalindrome(self, A):
        ss=A.split('->')
        sk=ss[:]
        sk.reverse()
        if sk==ss:
            return True
        else:
            return False
if __name__ == '__main__':
    print(PalindromeList().chkPalindrome('1->2->2->1'))