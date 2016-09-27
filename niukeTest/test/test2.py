# -*- coding: utf-8 -*-

class Filter(object):
    def filter(self, ss):
        count = 0
        for i in ss:
            if ss.index(i) == 0:
                rep = i
            if i == rep:
                count +=1


    def recursion(self, ss, boolean=True):
        if boolean == False:
            return ss
        elif ss == filter(ss):
            return self.recursion(ss, False)
        else:
            ss = filter(ss)
            return self.recursion(ss, True)
