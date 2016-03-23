#coding=utf-8
__author__ = 'zjutK'
formats={
    'ymd':'{d.year}-{d.month}-{d.day}',
    'mdy':'{d.month}/{d.day}/{d.year}',
    'dmy':'{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def __format__(self, code):
        if code=='':
            code='ymd'
        fmt=formats[code]
        return fmt.format(d=self)


print(format(Date(1992,7,1),'mdy'))
