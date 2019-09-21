# _*_ coding uft-8 _*_
# 开发团队: 裴和世昌团队
# 开发人员: 裴世昌
# 开发时间: 2019/9/21   20:17
# 文件名称: xmruning.py
# 开发工具: PyCharm


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):

        return '我的名字叫 %s 体重是 %.2f 公斤' % (self.name, self.weight)

    def run(self):
        print('%s爱跑步，跑步锻炼身体' %self.name)
        self.weight -= 0.5

    def eat(self):
        print('%s是吃货，吃完这顿在减肥' %self.weight)
        self.weight += 1

xiaoming = Person('小明', 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)


