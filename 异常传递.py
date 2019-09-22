# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/22   11:30
# 文件名称: 异常传递.py
# 开发工具: PyCharm


def demo1():
    return int(input('输入整数：'))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print('未知错误 %s' % result)
