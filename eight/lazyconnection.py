#coding=utf-8
from _socket import AF_INET, SOCK_STREAM

__author__ = 'zjutK'
class lazyconnection:
    def __init__(self,adddress,family=AF_INET,type=SOCK_STREAM):
        self.address=adddress
        self.family=family
        self.type=type
        self.sock=None


