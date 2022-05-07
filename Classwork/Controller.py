# @Author  : 茂茂
# @Time    : 2022/3/10 21:48

import sys
import ServiceImpl

'''
控制层
异常处理本应该放在业务逻辑层,但由于控制台接收参数的参数中也需要处理,综合考虑集中放在控制层处理
'''


class User(object):
    """用户类"""

    # 设置堆栈大小,缓解递归过深
    # sys.setrecursionlimit(10000)

    def __init__(self, name='临时访客'):
        self.name = name
        print('欢迎' + self.name)

    def transfer(self):
        """
        负责调用可执行的函数,检验参数合法性

        """
        while True:
            try:
                print("请选择进入程序(输入序号):\t1-运煤计算器\t\t\t2-圆计算器\t\t\t3-查找偶数\t\t4-判断正负\t\t\t5-查找质数\t\t6-计算小写字母")
                print("\t\t\t\t\t\t7-替换字符\t\t\t8-合并列表\t\t\t9-扩展指定元组\t10-计算字符重现次数\t11-列表去重\t\t12-备份文件")
                print("\t\t\t\t\t\t13-去除文件中的行注释\t14-将文件中的数值排序\t15-计算偶数和\t\t16-计算累乘\t\t\t17-判断回文数\t\t18-构建三角形")
                print("\t\t\t\t\t\t19-计算公倍数")
                print("\t\t\t\t\t\t0-退出程序")
                serial = input("请选择: ")
                if '0' == serial:
                    print('已退出')
                    sys.exit()
                elif '1' == serial:
                    def builtInput():
                        # 捕捉用户输入不可转float类型的值,无需回退至主界面,增强友好性
                        try:
                            a = float(input('请输入煤的总重量: '))
                            b = float(input('请输入大货车运力: '))
                            if b <= 0:
                                raise ZeroDivisionError('错误: 小货车运力不能为零\n')
                            c = float(input('请输入大车已运过几次: '))
                            d = float(input('小货车运力: '))
                            print('小货车还需运输: ' + str(ServiceImpl.transportationCoal(a, b, c, d)) + '次\n')
                            return
                        # 抛出异常则递归调用,使函数得到正确执行
                        except ValueError:
                            print('错误: 请输入数字\n')
                            builtInput()
                        except ZeroDivisionError as e:
                            print(e)
                            builtInput()

                    builtInput()
                elif '2' == serial:
                    def builtInput():
                        try:
                            a = float(input('请输入需计算圆面积的半径: '))
                            if a > 0:
                                print('结果 == ' + str(ServiceImpl.calculateRound(a))[1:-2:] + '\n')
                                return
                            else:
                                raise LessZeroException('错误: 半径需为正数\n')
                        except LessZeroException as e:
                            print(e)
                            builtInput()
                        except ValueError:
                            print('错误: 请输入数字\n')
                            builtInput()

                    builtInput()
                elif '3' == serial:
                    def builtInput():
                        try:
                            a = int(input('请输入需查找偶数的下限: '))
                            b = int(input('请输入需查找偶数的上限: '))
                            if a >= b:
                                print('错误: 上限不能小于或者等于下限\n')
                                builtInput()
                            print(str(a) + '到' + str(b) + '范围内的偶数: ', end='')
                            print(ServiceImpl.outputEvenNumbers(b, a))
                            print('\n')
                            return
                        except ValueError:
                            print('错误: 请输入整数\n')
                            builtInput()

                    builtInput()
                elif '4' == serial:
                    def builtInput():
                        try:
                            a = float(input('请输入需要判断的数字: '))
                            print(ServiceImpl.judgePositiveAndNegative(a) + '\n')
                            return
                        except ValueError:
                            print('错误: 请输入数字\n')
                            builtInput()

                    builtInput()
                elif '5' == serial:
                    def builtInput():
                        try:
                            a = int(input('请输入需要查找的范围: '))
                            print('2到' + str(a) + '的质数: ', end='')
                            print(ServiceImpl.findPrimeNumbers(a))
                            print('\n')
                            return
                        except ValueError:
                            print('错误: 请输入大于2的正整数\n')
                            builtInput()

                    builtInput()
                elif '6' == serial:
                    def builtInput():
                        s = input('输入c计算输入控制台的文本   输入f计算本机文件中的文本\n请输入: ')
                        if 'c' == s:
                            string = input('请输入需要筛选小写字母的字符串: ')
                            print('字符串中有小写字母: ', end='')
                            print(ServiceImpl.calculateLowercase(string), end='个')
                            print('\n')
                        elif 'f' == s:
                            while True:
                                try:
                                    num = ServiceImpl.calculateLowercaseFile()
                                    if num > 0:
                                        print('文件中小写字母总数: ' + str(num) + '个\n')
                                        break
                                    elif -1 == num:
                                        judge = input('输入1重新选择文件,否则输入输入任意字符退出程序6: ')
                                        if '1' != judge:
                                            break
                                except UnicodeDecodeError:
                                    print('错误: 只能识别文本类型文件\n')
                        else:
                            print('错误: 没有这个选项\n')
                            builtInput()

                    builtInput()
                elif '7' == serial:
                    def builtInput():
                        s = input('输入替换输入控制台中的指定字符   输入f替换本机文件中的指定字符\n请输入: ')
                        if 'c' == s:
                            a = input('请输入替换前的字符串: ')
                            b = input('请输入需要被替换的字符串: ')
                            c = input('请输入用于替换的字符串: ')
                            print('替换后的新字符串: ', end='')
                            print(ServiceImpl.customizeReplace(a, b, c))
                            print('\n')
                        elif 'f' == s:
                            # 通过循环保证不会因误触取消而无法选择文件
                            while True:
                                a = input('请输入需要被替换的字符串: ')
                                b = input('请输入用于替换的字符串: ')
                                try:
                                    info = ServiceImpl.customizeReplaceFile(a, b)
                                except UnicodeDecodeError:
                                    info = 'error'
                                    print('错误: 只能识别文本类型文件\n')
                                if '-1' == info:
                                    judge = input('输入1重新选择文件,否则输入输入任意字符退出程序7: ')
                                    if '1' != judge:
                                        break
                                elif 'error' != info:
                                    print('替换成功!新文件路径: ' + info + '\n')
                                    break

                        else:
                            print('错误: 没有这个选项\n')
                            builtInput()

                    builtInput()
                elif '8' == serial:
                    def builtInput():
                        try:
                            a = int(input('请输入需要合并列表的个数: '))
                            i = 0
                            totalList = []
                            while i < a:
                                # 利用循环拦截非数值数据的输入
                                lock = True
                                while lock:
                                    strings = input(f"请输入第{i + 1}个列表(只能输入数字,且要用单个空格分隔): ")
                                    # 判断字符是否为数字,小数点或负号
                                    for sIndex in range(len(strings)):
                                        if (48 > ord(strings[sIndex]) or ord(strings[sIndex]) > 57) and (
                                                ord(strings[sIndex]) not in (32, 45, 46)):
                                            print('未按要求输入,请重新输入!\n')
                                            break
                                    # 判断是否单独输入小数点或负号
                                    else:
                                        temp = strings.split()
                                        for last in temp:
                                            if last in ('.', '-'):
                                                print('请输入数字!\n')
                                                break
                                        else:
                                            # 将str类型的列表元素转换成数值型元素
                                            stringsList = []
                                            for t in temp:
                                                stringsList.append(float(t))
                                            lock = False
                                totalList.append(stringsList)
                                i += 1
                            print(ServiceImpl.mergeList(totalList))
                            print('\n')
                            return
                        except ValueError:
                            print('请输入正整数!\n')
                            builtInput()

                    builtInput()
                elif '9' == serial:
                    def builtInput():
                        oldtuple = ('p', 'y', 't', ['o', 'n'])
                        string = input('请输入要添加的字符: ')
                        print(ServiceImpl.tupleExpansion(oldtuple, string))
                        print('\n')
                        return

                    builtInput()
                elif '10' == serial:
                    def builtInput():
                        s = input('输入c计算从控制台接收的字符串中的字符出现的次数   输入f计算本机文件中字符出现的次数\n请输入: ')
                        if 'c' == s:
                            string = input('请输入需要计算的字符串: ')
                            print(ServiceImpl.statisticsCharacters(string))
                            print('\n')
                        elif 'f' == s:
                            # 通过循环保证不会因误触取消而无法选择文件
                            while True:
                                try:
                                    info = ServiceImpl.statisticsCharactersFile()
                                except UnicodeDecodeError:
                                    info = 'error'
                                    print('错误: 只能识别文本类型文件\n')
                                if '-1' == info:
                                    judge = input('输入1重新选择文件,否则输入输入任意字符退出程序10: ')
                                    if '1' != judge:
                                        break
                                elif 'error' != info:
                                    print(info)
                                    print()
                                    break
                        else:
                            print('错误: 没有这个选项\n')
                            builtInput()

                    builtInput()
                elif '11' == serial:
                    def builtInput():
                        strings = input("请输入需要去重列表(要用单个空格进行分隔): ")
                        oldList = strings.split()
                        print(ServiceImpl.listDeduplication(oldList))
                        print('\n')
                        return

                    builtInput()
                elif '12' == serial:
                    def builtInput():
                        while True:
                            info = ServiceImpl.backupFile()
                            if '-1' == info:
                                judge = input('输入1重新选择文件,否则输入输入任意字符退出程序13: ')
                                if '1' != judge:
                                    break
                            else:
                                print('新文件地址: ' + info)
                                print()
                                break

                    builtInput()
                elif '13' == serial:
                    def builtInput():
                        while True:
                            try:
                                info = ServiceImpl.RemoveFileComments()
                            except UnicodeDecodeError:
                                info = 'error'
                                print('错误: 只能识别文本类型文件\n')
                            if '-1' == info:
                                judge = input('输入1重新选择文件,否则输入输入任意字符退出程序13: ')
                                if '1' != judge:
                                    break
                            elif 'error' != info:
                                print('新文件地址: ' + info)
                                print()
                                break

                    builtInput()
                elif '14' == serial:
                    def builtInput():
                        while True:
                            try:
                                info = ServiceImpl.SortingDigitalFiles()
                            except UnicodeDecodeError:
                                info = 'error'
                                print('错误: 只能识别文本类型文件\n')
                            if '-1' == info:
                                judge = input('输入1重新选择文件,否则输入输入任意字符退出程序13: ')
                                if '1' != judge:
                                    break
                            elif 'error' != info:
                                print('新文件地址: ' + info)
                                print()
                                break

                    builtInput()
                elif '15' == serial:
                    def builtInput():
                        try:
                            a = int(input('请输入需计算偶数和的下限: '))
                            b = int(input('请输入需计算偶数和的上限: '))
                            if a >= b:
                                print('错误: 上限不能小于或者等于下限\n')
                                builtInput()
                            print(str(a) + '到' + str(b) + '内的所有的偶数和: ', end='')
                            print(ServiceImpl.calculateEvenSum(b, a))
                            print('\n')
                            return
                        except ValueError:
                            print('错误: 请输入整数\n')
                            builtInput()

                    builtInput()
                elif '16' == serial:
                    def builtInput():
                        try:
                            a = int(input('请输入需计算累乘的下限: '))
                            b = int(input('请输入需计算累乘的上限: '))
                            if a >= b:
                                print('错误: 上限不能小于或者等于下限\n')
                                builtInput()
                            print(str(a) + '到' + str(b) + '内的累乘: ', end='')
                            print(ServiceImpl.rangeMultiply(b, a))
                            print('\n')
                            return
                        except ValueError:
                            print('错误: 请输入整数\n')
                            builtInput()

                    builtInput()
                elif '17' == serial:
                    def builtInput():
                        string = input('输入需要判断是否为回文数的数据: ')
                        if ServiceImpl.judgmentPalindrome(string):
                            print(str(string) + ' 是回文数')
                        else:
                            print(str(string) + ' 不是回文数')
                        print('\n')
                        return

                    builtInput()
                elif '18' == serial:
                    def builtInput():
                        try:
                            i = 1
                            sideList = []
                            while i <= 3:
                                a = float(input('请输入三角形的第' + str(i) + '条边的长度: '))
                                if a <= 0:
                                    raise LessZeroException('错误: 长度不能小于等于零!')
                                sideList.append(a)
                                i += 1
                            if ServiceImpl.reasonableTriangle(sideList):
                                print('判断结果: 这三条边 可以 构成三角形')
                            else:
                                raise NoTriangularException('判断结果: 这三条边 不可以 构成三角形!\n')
                            return
                        except NoTriangularException as e:
                            print(e)
                            builtInput()
                        except LessZeroException as e:
                            print(e)
                            builtInput()

                    builtInput()
                elif '19' == serial:
                    def builtInput():
                        try:
                            first = int(input('请输入第一个数: '))
                            second = int(input('请输入第二个数: '))
                            if (first <= 0) or (second <= 0):
                                raise LessZeroException
                            info = ServiceImpl.LCM(first, second)
                            if info == False:
                                raise ValueLargeException('整数较大,超出计算范围,请重新选择')
                            else:
                                print(str(first) + '和' + str(second) + '的最小公倍数是: ' + str(info))
                            print('\n')
                            return
                        except ValueLargeException as e:
                            print(e)
                            builtInput()
                        except (LessZeroException, ValueError):
                            print('错误: 请输入正整数!')
                            builtInput()

                    builtInput()
                elif serial == '20':
                    ServiceImpl.generateWordcloud()
                elif serial == '21':
                    ServiceImpl.drawBarChart()
                else:
                    print('错误: 您输入的程序序号不存在\n')

            # AOP思想,类似将打印日志织入到所有方法中
            except Exception:
                ServiceImpl.printLog()
                print('错误: 未知错误!\n')


class LessZeroException(Exception):
    """定义值小于零时抛出的异常"""
    pass


class ValueLargeException(Exception):
    """定义数值过大时抛出的异常"""
    pass


class NoTriangularException(Exception):
    """定义计算结果不能构成三角形时抛出的异常"""
    pass
