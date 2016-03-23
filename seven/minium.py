#coding=utf-8
__author__ = 'zjutK'
def minium(*values,clip=None):
    m=min(values)
    if clip is not None:
        m=clip if clip>m else m

    print(m)
#clip为none的时候返回最小值，如果有clip则返回value与clip中的大的值
minium(1,5,2,-5,10,clip=1)

L1=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
