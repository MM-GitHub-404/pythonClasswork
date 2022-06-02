import tkinter


def leapYear(year):
    """
    判断是否是闰年
    @param year: 需要判断是否是闰年的年份
    @return:     是闰年返回True,否则返回False
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def getMonthDays(year, month):
    """
    获取某个月份的天数
    @param year:  某年
    @param month: 某月
    @return:      返回此月天数
    """
    days = 31
    if month == 2:
        if leapYear(year):
            days = 29
        else:
            days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    return days


# 星期
def getTotalDays(year, month):
    """
    计算公元元年到某个月份的总天数
    @param year:  某年
    @param month: 某月
    @return:      返回公元元年到此月份的总天数
    """
    totalDays = 0
    # 计算从第一年到查询年份的前一年的总天数
    for i in range(1, year):
        if leapYear(i):
            totalDays += 366
        else:
            totalDays += 365
    # 计算查询年份从一月到查询月份的前一个月的天数相加，得到总天数
    for i in range(1, month):
        totalDays += getMonthDays(year, i)
    return totalDays


# 生成万年历
def generateCalendar():
    # 获取输入框的内容
    year = t1.get()
    month = t2.get()
    # input接受的数据默认为字符串，需要转换为int型
    year = int(year)
    month = int(month)
    # 计数，每7个一换行
    count = 0
    # 存储万年历的列表
    day = []
    day.append("日\t一\t二\t三\t四\t五\t六\n")
    # 前面的空出来
    for i in range((getTotalDays(year, month) % 7) + 1):
        # end：可使print输出后不自动换行，接着输出数字
        day.append('\t')
        count += 1
        # 统一格式
        if count == 7:
            day.append('\n')
    # 输出日期
    for i in range(1, getMonthDays(year, month) + 1):
        day.append(str(i))
        count += 1
        # 每7个一换行,不换行则需要\t
        if count % 7 == 0:
            day.append('\n')
        else:
            day.append('\t')
    # 如果最后一天不为周六，则将空日期填满（原因:lable默认居中显示）
    if count % 7 != 0:
        for i in range(7 - count % 7 - 1):
            day.append('\t')
        day.append('     ')
    # 更改lable显示内容
    w.config(text="".join(day))


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('万年历')
    window.minsize(600, 350)
    window.maxsize(600, 350)
    # 标签、输入框、按钮
    show = tkinter.Label(text='', anchor='se', font=('黑体', 30), fg='black')  # 显示框
    l1 = tkinter.Label(window, text="请输入年份：")  # 年份
    l1.pack()
    t1 = tkinter.StringVar()
    t1.set('2022')
    entry_year = tkinter.Entry(window, textvariable=t1).pack()
    l2 = tkinter.Label(window, text="请输入月份：")  # 月份
    l2.pack()
    t2 = tkinter.StringVar()
    t2.set('6')
    entry_mon = tkinter.Entry(window, textvariable=t2).pack()
    b = tkinter.Button(text='查看万年历', command=generateCalendar)
    b.pack()
    # 万年历结果显示在lable中
    w = tkinter.Label(window, text="")
    w.pack()
    # 显示窗口
    window.mainloop()
