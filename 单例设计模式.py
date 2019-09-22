# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/22   10:02
# 文件名称: 单例设计模式.py
# 开发工具: PyCharm


class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回对象的引用
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        MusicPlayer.init_flag = True
        # 1.判断是否执行过初始化操作
        print('播放器初始化')


# 创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)

