#coding=utf-8
__author__ = 'zjutK'
'''
'16/5/16下午3:12'

'''

class Trunk(object):
    def __str__(self):
        pass

    def subtree(self):
        pass


class Composite(Trunk):
    def __init__(self,left=None,right=None,length=None):
        self.left=left
        self.right=right
        self.length=length

    def __str__(self):
        if self.length:
            return "("+self.length.__str__()+","+self.length.__str__()+"):"+str(self.length)
        else:
            return "("+self.left.__str__()+","+self.right.__str__()+")"
        def subtree(self):
            return Composite(self.left,self.right)

class Leaf(Trunk):
    def __init__(self,name,length=None):
        self.name=name
        self.length=length
        self.left=None
        self.right=None

    def __str__(self):
        return self.name+": "+str(self.length)

    def subtree(self):
        return Leaf(self.name,self.length)
if __name__ == '__main__':
    t1=Leaf("A",0.71399)
    print(t1)

    t2=Composite(Leaf("B",-0.00804),Leaf("C",0.07470))
    print(t2)

    t3 = Composite(Leaf('A', 0.71399),Composite(Leaf('B', -0.00804), Leaf('C', 0.07470), 0.1533), 0.0666)
    print(t3)

    t4=t3.right.right.subtree()
    print(t4)

    t5=t3.left.subtree()
    print(t5)