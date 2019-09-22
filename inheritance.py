# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/21   23:49
# 文件名称: inheritance.py
# 开发工具: PyCharm


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print('%s 蹦蹦跳跳地玩耍...' % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print('%s 飞到天上玩耍...' % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self,dog):
        print('%s和%s快乐地玩耍...' % (self.name, dog.name))

        dog.game()


# wangcai = Dog('旺财')
wangcai = XiaoTianDog('飞天旺财')

xiaoming = Person('小明')

xiaoming.game_with_dog(wangcai)

