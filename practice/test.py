# coding=utf-8
__author__ = 'zjutK'


class StaticMethod:
    name='test'
    @staticmethod
    def foo():
        print("This is static method foo().")


class ClassMethod:
    @classmethod
    def bar(cls):
        print("This is class method bar().")
        print("bar() is part of class:", cls.__name__,cls.name)


if __name__ == "__main__":
    static_foo = StaticMethod()  # 实例化
    static_foo.foo()  # 实例调用静态方法
    StaticMethod.foo()  # 通过类来调用静态方法
    print("********")
    class_bar = ClassMethod()
    class_bar.bar()
    ClassMethod.bar()
