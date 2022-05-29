# @Author  : 茂茂
# @Time    : 2022/3/21 9:05
import time
import tkinter.filedialog
import turtle

'''
工具类
将业务逻辑层中重复使用的方法移动至工具类中,避免产生函数依赖
'''


# 平瑞年
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


# 月份的天数
def getMonthDays(year, month):
    days = 31
    if month == 2:  # 确定2月天数
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:  # 4 6 9 11这些月份均为30天
        days = 30
    return days


# 星期
def getTotalDays(year, month):
    totalDays = 0
    for i in range(1, year):  # 计算从第一年到查询年份的前一年的总天数
        if leap_year(i):
            totalDays += 366
        else:
            totalDays += 365
    for i in range(1, month):  # 再计算查询年份从一月到查询月份的前一个月的天数相加，得到总天数
        totalDays += getMonthDays(year, i)
    return totalDays


# 生成万年历
def generateCalendar(year,month):
    # year = t1.get()  # 获取输入框的内容：年份
    # month = t2.get()  # 获取输入框的内容：月份
    year = int(year)  # input接受的数据默认为字符串，需要转换为int型
    month = int(month)
    count = 0  # 计数，每7个一换行
    day = []  # 存储万年历的列表
    day.append("日\t一\t二\t三\t四\t五\t六\n")
    for i in range((getTotalDays(year, month) % 7) + 1):  # 前面的空出来
        day.append('\t')  # end：可使print输出后不自动换行，接着输出数字
        count += 1
        if count == 7:  # 统一格式
            day.append('\n')
    for i in range(1, getMonthDays(year, month) + 1):  # 输出日期
        day.append(str(i))
        count += 1
        if count % 7 == 0:  # 每7个一换行,不换行则需要\t
            day.append('\n')
        else:
            day.append('\t')
    if count % 7 != 0:  # 如果最后一天不为周六，则将空日期填满（原因：lable默认居中显示）
        for i in range(7 - count % 7 - 1):
            day.append('\t')
        day.append('     ')
    w.config(text="".join(day))  # 更改lable显示内容


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


def drawFilledRectangle(pen, x, y, w, h, colorP="black", colorF="green"):
    """
    绘制柱体

    """
    pen.pencolor(colorP)
    pen.fillcolor(colorF)
    pen.up()
    pen.goto(x, y)
    pen.down()
    # 单个绘制柱体
    pen.begin_fill()
    pen.goto(x + w, y)
    pen.goto(x + w, y + h)
    pen.goto(x, y + h)
    pen.goto(x, y)
    pen.end_fill()


def displayText(pen, multiple, languages, heights):
    """
    绘制柱体数据参数

    :param pen:           乌龟参数
    :param multiple:    倍数柱体高度参数
    :param languages:   柱体数据参数列表
    :param heights:     柱体高度列表
    """
    pen.pencolor("black")
    pen.up()
    # 由于使用的是绝对坐标, 所以需要用基准倍数multiple调整直方图大小
    for i in range(10):
        # 绘制频数参数
        pen.goto((-362 + 76 * i), heights[i] * multiple / 9)
        pen.write(str(heights[i]), align="center", font=("Arial", 10, "normal"))
        # 绘制标签参数
        pen.goto((-362 + 76 * i), -30)
        pen.write(languages[i], align="center", font=("Arial", 10, "normal"))
