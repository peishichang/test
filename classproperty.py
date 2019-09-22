# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/22   8:56
# 文件名称: classproperty.py
# 开发工具: PyCharm


class Tool(object):
    count = 0
    @classmethod
    def show_tool_count(cls):
        print(cls.count)

    @staticmethod
    def drop():
        print('工具掉了')

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool('axe')
tool2 = Tool('hammer')
tool3 = Tool('bucket')

Tool.drop()
