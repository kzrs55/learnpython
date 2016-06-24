class BaseAdder(object):
    def add(self, a, b):
        return a + b

class NonReturningAdder(BaseAdder):
    def add(self, a, b):
        super(NonReturningAdder, self).add(a, b)

class ReturningAdder(BaseAdder):
    def add(self, a, b):
        return super(ReturningAdder, self).add(a, b)


if __name__ == '__main__':
    a = NonReturningAdder()
    b = ReturningAdder()
    print a.add(3, 5)
    print b.add(3, 5)
    from niukeTest.Test2 import dict
    print dict