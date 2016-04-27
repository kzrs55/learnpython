#coding=utf-8
__author__ = 'zjutK'
#为线程设置超时循环

class IOTask:
    def terminate(self):
        self._running=False
    def run(self,sock):
        #sock is socket
        sock.settimeout(5)
        while self._running:
            try:
                data=sock.recv(1892)
                break
            except sock.timeout:
                continue
        return
