# @Author  : 茂茂
# @Time    : 2022/3/10 21:46

import math
import turtle
import jieba
import wordcloud
from matplotlib.image import imread
import Utils
import os
import datetime
import traceback
import time

'''
业务逻辑层
'''


def snowflakeCurve(length, stairs):
    """
    绘制完整雪花曲线

    @param length:  雪花每条直线的长
    @param stairs:  需要绘制的阶数
    """

    # 定义内部类方便调用
    def drawSnowflakes(pen, length, stairs):
        """
        绘制雪花曲线

        @param pen:     海龟画笔
        @param length:  雪花每条直线的长
        @param stairs:  需要绘制的阶数
        """
        # 绘制一阶雪花线段
        if stairs <= 1:
            pen.forward(length)
            pen.left(60)
            pen.forward(length)
            pen.right(120)
            pen.forward(length)
            pen.left(60)
            pen.forward(length)
        # 依照雪花转向规律,递归绘制n-1阶雪花线段
        else:
            for i in range(4):
                if i % 2 == 0:
                    drawSnowflakes(pen, length, stairs - 1)
                    pen.left(60)
                else:
                    drawSnowflakes(pen, length, stairs - 1)
                    pen.right(120)
            # 调整方向,保持方向起始一致性
            pen.left(120)

    # 设置画布尺寸
    turtle.setup(500, 500)
    pen = turtle.Turtle()
    # 隐藏画笔形状
    pen.hideturtle()
    # 合龙雪花线段为雪花
    for i in range(3):
        drawSnowflakes(pen, length, stairs)
        pen.right(120)
    # 默认完成绘制3秒后清空画布返回主程序
    time.sleep(3)
    pen.reset()


def strangeTriangle(length, stairs):
    # 设置画布尺寸
    turtle.setup(1000, 800)
    pen = turtle.Turtle()
    # 隐藏画笔形状
    pen.hideturtle()
    # 移动画笔到指定位置开始
    pen.penup()
    pen.goto(-400, -300)
    pen.pendown()

    Utils.drawTriangle(pen, length, stairs)
    # 默认完成绘制3秒后清空画布返回主程序
    time.sleep(3)
    pen.reset()


def transportationCoal(total, cartLoad, numberOfCarts, trolleyLoad):
    """
    计算第五大题第2小题运煤问题

    :param total:         煤的总重量
    :param cartLoad:      大货车运力
    :param numberOfCarts: 大车已运过几次
    :param trolleyLoad:   小货车运力
    :return:              小货车还需运输的次数
    """
    remaining = total - (cartLoad * numberOfCarts)
    if remaining <= 0:
        return 0
    calculationResults = remaining / trolleyLoad
    # 向上取整
    return math.ceil(calculationResults)


def calculateRound(radius):
    """
    计算给定半径的圆的面积

    :param radius: 需计算圆面积的半径
    :return:       包含圆面积和圆直径的字典
    """
    round_list = {}
    round_list['直径'] = radius * 2
    round_list['面积'] = math.pi * radius * radius
    return round_list


def outputEvenNumbers(upperRange, lowerRange=0):
    """
    输出给定范围内的偶数

    :param upperRange: 范围上限(包括本身)
    :param lowerRange: 范围下限(包括本身,默认为0)
    :return:           包含指定范围内所有偶数的列表
    """
    return Utils.outputEvenNumbers(upperRange, lowerRange)


def judgePositiveAndNegative(parameter):
    """
    判断数字的正负

    :param parameter: 需要判断的数字
    :return:          判断结果
    """
    if parameter > 0:
        return '正数'
    elif parameter < 0:
        return '负数'
    else:
        return '0既不是整数也不是负数'


def findPrimeNumbers(upperLimit):
    """
    找出指定范围内的所有质数

    :param upperLimit: 指定范围(需大于1,默认值为100,)
    :return:           包含指定范围内所有质数的列表
    """
    primeNumberList = []
    # 双层循环判断
    while upperLimit > 1:
        # 定义判断条件,循环判断后重置
        judge = 'true'
        i = upperLimit - 1
        while i > 1:
            if (upperLimit % i) == 0:
                judge = 'false'
                break
            i -= 1
        if (judge == 'true'):
            primeNumberList.append(upperLimit)
        upperLimit -= 1

    return primeNumberList


def calculateLowercase(string):
    """
    计算字符串中小写字母的数量

    :param string: 需要计算的字符串
    :return:       字符串中包含的小写字母数量
    """
    return Utils.isLowerCaseLetters(string)


def calculateLowercaseFile():
    """
    计算文本文档中小写字母总数

    :return: 返回文本中小写字母总数,未选择文件返回-1,非txt格式文件返回-2
    """
    # 打开文件资源管理器选择文件并获取文件完整路径
    urlFile = Utils.selectFile()
    if '' == urlFile:
        return -1
    else:
        stringFile = Utils.readTxtFile(urlFile)
        return Utils.isLowerCaseLetters(stringFile)


def customizeReplace(originalString, oldCharacter, newCharacter):
    """
    批量替换字符串中的某个字符
    可以在controller中直接使用replace函数,但是在service层单独定义函数能提高可维护性与可读性

    :param originalString:  原字符串
    :param oldCharacter:    被替换的字符
    :param newCharacter:    用于替换的字符
    :return:                替换后的字符串
    """
    return originalString.replace(oldCharacter, newCharacter)


def customizeReplaceFile(oldCharacter, newCharacter):
    """
    将文本文档中某个字符批量替换输出到新文件中

    :param oldCharacter: 被替换的字符
    :param newCharacter: 用于替换的字符
    :return:             替换成功返回新文件路径,未选择文件返回-1
    """
    # 打开文件资源管理器选择文件并获取文件完整路径
    urlFile = Utils.selectFile()
    if '' == urlFile:
        return '-1'
    else:
        # 读取指定的文件
        stringFile = Utils.readTxtFile(urlFile)
        # os.path.splitext将完整文件路径与文件名分割
        newFileURL = os.path.splitext(urlFile)[0] + '(替换后)' + os.path.splitext(urlFile)[1]
        # 防止写入过程中程序意外终止导致原文件损坏,采取写入新文件方式
        with open(newFileURL, 'w', encoding='utf-8') as file:
            file.write(stringFile.replace(oldCharacter, newCharacter))
        return newFileURL


def mergeList(totalList):
    """
    合并若干列表并降序排序

    :param totalList: 需要合并,排序的若干列表
    :return:          返回降序排序后的新列表
    """
    newList = []
    for i in totalList:
        newList += i
    newList.sort(reverse=True)
    return newList


def tupleExpansion(oldTuple, string):
    """
    元组扩展

    :param oldTuple: 给定的元组
    :param string:   需要向元组中最后一个列表类型元素添加的字符
    :return:         返回添加新字符后的元组
    """
    newList = list(oldTuple)
    newList[len(newList) - 1].append(string)
    newTuple = tuple(newList)
    return newTuple


def statisticsCharacters(string):
    """
    计算字符串中每个不同字符出现的次数

    :param string: 给定需要计算的字符串
    :return:       返回包含每个字符出现次数的字典
    """
    return Utils.statisticsCharacters(string)


def statisticsCharactersFile():
    """
    计算文件中每个不同字符出现的次数

    :return: 计算成功返回包含每个字符出现次数的字典,未选择文件返回-1
    """
    # 打开文件资源管理器选择文件并获取文件完整路径
    urlFile = Utils.selectFile()
    if '' == urlFile:
        return '-1'
    else:
        # 读取指定的文件,返回字符串格式
        return Utils.statisticsCharacters(Utils.readTxtFile(urlFile))


def listDeduplication(oldList):
    """
    删除列表中重复的元素

    :param oldList: 需要删除重复元素的列表
    :return:        返回删除后的列表
    """
    newList = []
    for i in oldList:
        if i not in newList:
            newList.append(i)
    return newList


def backupFile():
    """
    备份文件

    :return: 返回新文件地址,未选择文件返回-1
    """
    # 打开文件资源管理器选择文件并获取文件完整路径
    urlFile = Utils.selectFile()
    if '' == urlFile:
        return '-1'
    else:
        # 二进制读取指定的文件,适用大多数类型文件
        fileBytes = open(urlFile, 'rb+').read()
        # 防止写入过程中程序意外终止导致原文件损坏,采取写入新文件方式备份文件
        newFileURL = os.path.splitext(urlFile)[0] + '(副本)' + os.path.splitext(urlFile)[1]
        # 二进制写入
        with open(newFileURL, 'wb') as file:
            file.write(fileBytes)
        return newFileURL


def RemoveFileComments():
    """
    去除文件中的非空首字符即#的行注释

    :return: 返回新文件地址,未选择文件返回-1
    """
    # 打开文件资源管理器选择文件并获取文件完整路径
    fileURL = Utils.selectFile()
    if '' == fileURL:
        return '-1'
    else:
        newFileURL = os.path.splitext(fileURL)[0] + '(去注释)' + os.path.splitext(fileURL)[1]
        # 读取文件并按行装入列表
        text = Utils.readTxtFile(fileURL).split("\n")
        # 将首符号为非"#"的行与空白行写入新文件
        # 循环内写入文件需要手动打开文件,减少IO次数
        file = open(newFileURL, 'a+', encoding='utf-8')
        try:
            for row in text:
                if row == '':
                    file.write(row + '\n')
                # 空格排除判断,遇"#"则不写入本行,否则写入新文件("#"ASCII为35,空格ASCII为32)
                for byte in row:
                    if ord(byte) == 35:
                        break
                    elif ord(byte) != 32:
                        file.write(row + '\n')
                        break
            file.flush()
        # 手动打开文件后即使发生异常也要关闭流
        finally:
            if file != None:
                file.close()
        return newFileURL


def SortingDigitalFiles():
    """
    将文件中的数值进行排序

    :return: 返回新文件地址,未选择文件返回-1
    """
    # 打开文件资源管理器选择文件并获取文件完整路径
    fileURL = Utils.selectFile()
    if '' == fileURL:
        return '-1'
    else:
        newFileURL = os.path.splitext(fileURL)[0] + '(排序后)' + os.path.splitext(fileURL)[1]

        # 读取文件并按行装入列表
        text = Utils.readTxtFile(fileURL).split("\n")
        newText = []
        # 将首符号为非"#"的行与空白行写入新文件
        for row in text:
            # 只写入int和float类型
            try:
                newText.append(int(row))
            except ValueError:
                try:
                    newText.append(float(row))
                except ValueError:
                    continue
        # 列表内进行排序后直接输出到新文件
        newText.sort()
        # 循环内写入文件需要手动打开文件,减少IO次数
        file = open(newFileURL, 'w+', encoding='utf-8')
        try:
            for newRow in newText:
                file.write(str(newRow) + '\n')
            file.flush()
        # 手动打开文件后即使发生异常也要关闭流
        finally:
            if None != file:
                file.close()
    return newFileURL


def calculateEvenSum(upperRange, lowerRange=0):
    """
    计算给定范围内的偶数和

    :param upperRange: 范围上限(包括本身)
    :param lowerRange: 范围下限(包括本身,默认为0)
    :return:           范围内的偶数和
    """
    # 获取范围内的所有偶数
    evenList = Utils.outputEvenNumbers(upperRange, lowerRange)
    sum = 0
    for i in evenList:
        sum += i
    return sum


def rangeMultiply(upperRange, lowerRange=3):
    """
    计算给定整数范围内的累乘

    :param upperRange: 范围上限(包括本身)
    :param lowerRange: 范围下限(包括本身,默认为3)
    :return:           范围内的累乘
    """
    temp = lowerRange + 1
    while upperRange >= temp:
        lowerRange *= temp
        temp += 1
    return lowerRange


def judgmentPalindrome(string):
    """
    计算给定变量是否为回文数

    :param string: 需要判断的变量
    :return:       是回文数返回True,否则返回False
    """
    if str(string) == str(string)[::-1]:
        return True
    return False


def reasonableTriangle(sideList):
    """
    判断三条边是否能构成一个三角形

    :param sideList: 需要判断的三条边长度列表
    :return:       能够构成一个三角形返回True,否则返回False
    """
    sideList.sort()
    if (sideList[0] + sideList[1]) > sideList[2]:
        return True
    return False


def LCM(first, second):
    """
    计算两个正整数的最小公倍数

    :param first:  第一个数
    :param second: 第二个数
    :return:    计算成功返回计算出的结果,否则返回False
    """
    if first == second:
        return first
    # 设置乘数变量
    f = 2
    s = 2
    # 临时公倍数变量
    tempFirst = first
    tempSecond = second
    # 设置阈值乘数超过一定数量级停止计算,此处设置为一亿,可计算两个千万级别的正整数
    stopValve = 100000000
    while True:
        if (f > stopValve) and (s > stopValve):
            break
        elif tempFirst < tempSecond:
            tempFirst = first * f
            if tempFirst == tempSecond:
                return tempFirst
            f += 1
        elif tempFirst > tempSecond:
            tempSecond = second * s
            if tempFirst == tempSecond:
                return tempSecond
            s += 1
    return False


def generateWordcloud():
    """
    绘制词云
    """
    # 选择文件
    fileStrings = open(Utils.selectFile(), encoding='utf-8')
    strings = str(fileStrings)
    # 设置形状
    shape = imread(Utils.selectFile(), 1)
    # 设置词云参数
    wc = wordcloud.WordCloud(mask=shape, background_color='white')
    wc.generate(strings)
    wcUrl = 'wc.jpg'
    wc.to_file(wcUrl)
    return wcUrl


def drawBarChart(multiple=5):
    """
    绘制文本中词语出现次数排名前十的条形图

    :param multiple: 条形图高度基准参数,默认为5倍频数
    """
    # 分词
    strings = jieba.lcut_for_search(Utils.readTxtFile(Utils.selectFile()))
    strSet = set(strings)
    # 统计词语出现频率
    statistics = {}
    for s in strSet:
        statistics[s] = strings.count(s)
    # 获取用于绘制条形图的参数
    languages = []
    heights = []
    for i in range(10):
        maxKey = None
        maxValue = -1
        for key in statistics:
            # 设置排除掉jieba库分词不当得到的词语
            if (statistics[key] >= maxValue) and (key not in ('\n', '\t', ' ')):
                maxKey = key
                maxValue = statistics[key]
        languages.append(maxKey)
        heights.append(maxValue)
        del statistics[maxKey]
    # 使用乌龟绘制频率直方图
    t = turtle.Turtle()
    # 设置绘制速度最快
    t.speed(0)
    t.hideturtle()
    for i in range(10):
        # drawFilledRectangle和displayText方法是使用别人写好的,简单调了一下参数
        # 没有注释地方说明我也不懂是如何实现的
        Utils.drawFilledRectangle(t, -400 + (76 * i), 0, 76, heights[i] * multiple / 9, "black", "light blue")
    Utils.displayText(t, multiple, languages, heights)


def printLog():
    """
    打印异常信息到日志

    """
    print("\n请联系管理员! 电话:18888888888\n            微信:123456")
    with open('log.txt', 'a+', encoding='utf-8') as file:
        # 打印异常时间及异常追溯信息
        file.write(str(datetime.datetime.now()) + '\n' + traceback.format_exc() + '\n')
