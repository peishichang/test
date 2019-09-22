# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/22   10:49
# 文件名称: 异常.py
# 开发工具: PyCharm

try:
    # 提示用户输入一个整数
    num = int(input('请输入一个整数：'))
    # 使用8除以用户输入的整数并输出
    result = 8/num
    print(result)
except ZeroDivisionError:
    print('除0错误')
except ValueError:
    print('请输入一个正确的整数')
except Exception as result:
    print('未知错误 %s' % result)