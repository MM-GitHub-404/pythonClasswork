# @Author  : 茂茂
# @Time    : 2022/3/21 9:05

import tkinter.filedialog

'''
工具类
将业务逻辑层中重复使用的方法移动至工具类中,避免产生函数依赖
'''


def isLowerCaseLetters(string):
    """
    判断字符是否为小写字母

    :param string: 需要判断的字符串
    :return:       返回字符串中小写字母总数
    """
    num = 0
    for i in range(len(string)):
        # 通过字符的ascii码来筛选小写字母
        if 97 <= ord(string[i]) <= 122:
            num += 1
    return num


def selectFile():
    """
    打开文件资源管理器选择文件并获取文件完整路径

    :return: 返回文件完整路径
    """
    urlFile = tkinter.filedialog.askopenfilename()
    return urlFile


def readTxtFile(urlFile):
    """
    读取指定绝对路径下的文件

    :param urlFile: 需要读取的文件地址
    :return: 返回字符串类型的文本文件的所有字符
    """
    # 此处捕捉异常目的是为了保证在不同编码格式下都能读取文件
    # 实际出现异常仍然交由controller层负责处理
    try:
        with open(urlFile, 'r+', encoding='utf-8') as file:
            stringFile = file.read()
    except UnicodeDecodeError:
        with open(urlFile, 'r+', encoding='ANSI') as file:
            stringFile = file.read()
    return stringFile


def statisticsCharacters(string):
    """
    计算字符串中每个不同字符出现的次数

    :param string: 给定需要计算的字符串
    :return:       返回包含每个字符出现次数的字典
    """
    # 将字符串添加到不重复的set集合中
    setString = set(string)
    statistics = {}
    for s in setString:
        statistics[s] = string.count(s)
    return statistics


def outputEvenNumbers(upperRange, lowerRange=0):
    """
    输出给定范围内的偶数

    :param upperRange: 范围上限(包括本身)
    :param lowerRange: 范围下限(包括本身,默认为0)
    :return:           包含指定范围内所有偶数的列表
    """
    evenList = []
    i = lowerRange
    while i <= upperRange:
        if ((i % 2) == 0) and (i != 0):
            evenList.append(i)
        i += 1
    return evenList
