# _*_ coding uft-8 _*_
# 开发团队: 裴和世昌团队
# 开发人员: 裴世昌
# 开发时间: 2019/9/21   23:03
# 文件名称: animal.py
# 开发工具: PyCharm


class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Dog(Animal):
    def bark(self):
        print('汪汪叫')

class XiaoTianQuan(Dog):
    def fly(self):
        print('我会飞')
    def bark(self):
        print('叫得跟神一样..')

        #super().bark()

        print('fjdklajfkdaf')

class Cat(Animal):
    def catch(self):
        print('抓老鼠')

wangcai = XiaoTianQuan()


wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
wangcai.fly()
