# _*_ coding uft-8 _*_
# 开发团队: 裴和世昌团队
# 开发人员: 裴世昌
# 开发时间: 2019/9/21   16:34
# 文件名称: 01.py
# 开发工具: PyCharm


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print('%s来了' % self.name)

    def __del__(self):
        print('%s去了' % self.name)

    def __str__(self):
        return '我是小猫[%s]' % self.name

    def eat(self):
        print('%s爱吃鱼' % self.name)




tom = Cat('Tom')
lazy_cat = Cat('Lazy_cat')

print(tom)

del tom



