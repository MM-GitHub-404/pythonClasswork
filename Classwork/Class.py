# @Author  : 茂茂
# @Time    : 2022/5/5 8:37

import math

'''
类文件
'''


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.__radius
        print(perimeter)
        return perimeter

    def get_area(self):
        area = math.pi * self.__radius * self.__radius
        print(area)
        return area


class Course:
    class_number = '101'
    class_name = 'python'
    class_teacher = '龙老师'

    def __init__(self, location='明实701'):
        self.__location = location

    def show_info(self):
        print('课程编号: ' + Course.class_number)
        print('课程名称: ' + Course.class_name)
        print('授课老师: ' + Course.class_teacher)
        print('授课教室: ' + self.__location)
