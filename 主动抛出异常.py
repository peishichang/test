# _*_ coding uft-8 _*_
# 开发人员: 裴世昌
# 开发时间: 2019/9/22   11:42
# 文件名称: 主动抛出异常.py
# 开发工具: PyCharm


def input_password():
    # 1.提示用户输入密码
    pwd = input('请输入密码：')
    # 2 判断密码长度 >=8 ,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3 如果 <8 主动抛出异常
    ex = Exception('密码长度不够')
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
