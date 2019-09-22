# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/22   9:38
# 文件名称: gameclass.py
# 开发工具: PyCharm


class Game(object):
    top_score = 0

    def __init__(self,name):
        self.name = name

    @staticmethod
    def show_help():
        print('帮助文件')

    @classmethod
    def show_top_score(cls):
        print('最高分%d' % cls.top_score)

    def star_game(self):
        print('%s开始游戏了' % self.name)


Game.show_help()

Game.show_top_score()

game = Game('小明')

game.star_game()
