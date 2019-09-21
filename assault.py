# _*_ coding uft-8 _*_
# 开发团队: 裴和世昌团队
# 开发人员: 裴世昌
# 开发时间: 2019/9/21   21:36
# 文件名称: assault.py
# 开发工具: PyCharm


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print('[%s]突突突。。。。' % self.model)
        else:
            print('[%s]没有子弹了。。。' % self.model)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is not None:
            print('冲啊。。。。[%s]' % self.name)
            self.gun.add_bullet(50)
            self.gun.shoot()
        else:
            print('[%s]还没有枪' % self.name)


ak47 = Gun('AK47')
xusanduo = Soldier('许三多')

xusanduo.gun = ak47
xusanduo.fire()

