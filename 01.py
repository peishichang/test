# _*_ coding uft-8 _*_
# 开发团队: 裴和世昌团队
# 开发人员: 裴世昌
# 开发时间: 2019/9/21   16:34
# 文件名称: 01.py
# 开发工具: PyCharm
class Cat:
    def eat(self):
        print('%s 爱吃鱼' % self.name)
    def drink(self):
        print('%s 爱喝水' % self.name)


tom = Cat()
lazy_cat = Cat()

tom.name = 'Tom'
lazy_cat.name = 'LazyCat'
tom.eat()
tom.drink()
lazy_cat.eat()
lazy_cat.drink()


