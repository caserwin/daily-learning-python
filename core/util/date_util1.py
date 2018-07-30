# coding=utf8

import re
from collections import OrderedDict
from dateutil.parser import parse
import datetime
import time


class DateType(object):
    YMD = '%Y-%m-%d'
    YMD_HMS = '%Y-%m-%d %H:%M:%S'


class DateParser(object):
    """
    日期型转为字符串的函数为: datetime.datetime.strftime()；
    字符串转为日期型的函数为: datetime.datetime.strptime()
    """

    def __init__(self):
        self.pattern = re.compile(
            r"((?:19|20)?\d{2})[-.]?((?:[0-1]?|1)[0-9])[-.]?((?:[0-3]?|[1-3])[0-9])?$"
        )

    def __cutDate(self, date, flags):
        y = date.year
        m = date.month if flags[1] else 1
        d = date.day if flags[2] else 1
        return datetime.date(y, m, d)

    def __mergeFlags(self, flags1, flags2):
        l = []
        length = min(len(flags1), len(flags2))
        for i in range(0, length):
            if flags1[i] and flags2[i]:
                l.append(True)
            else:
                l.append(False)
        return l

    def parse(self, strdate):
        m = self.pattern.match(strdate)
        flags = [False, False, False]
        if m:
            matches = list(m.groups())
            flags = list(map(lambda x: True if x != None else False, matches))
            results = list(map(lambda x: int(x) if x != None else 1, matches))
            if results[0] < 100:
                if results[0] > 9:
                    results[0] += 1900
                else:
                    results[0] += 2000

            return datetime.date(results[0], results[1], results[2]), flags
        else:
            return None

    def convert(self, strdate, format):
        date = self.parse(strdate)
        if date:
            date = date[0]
            return datetime.date.strftime(date, format)
        else:
            return None

    @classmethod
    def count_time(cls, start_time, date_format, end_time=datetime.datetime.now()):
        """
        1. 给定日期,计算和当前日期的差距
        """
        start_time = datetime.datetime.strptime(start_time, date_format)
        return (end_time - start_time).days

    @classmethod
    def find_min_date(cls, date_list, date_format):
        """
        1. 找到最小的日期
        """
        min_date = datetime.datetime.strptime(date_list[0], date_format)
        for date in date_list:
            date = datetime.datetime.strptime(date, date_format)
            if (min_date - date).days > 0:
                min_date = date
        return min_date.strftime(date_format)

    @classmethod
    def sort_date_dict(cls, date_dict, date_format, DESC=True):
        """
        1. 对日期进行排序
        2. 输入是字典类型。
        3. 默认降序方式
        """
        res_dic = sorted(date_dict.iteritems(),
                         key=lambda d: datetime.datetime.strptime(d[0], date_format), reverse=DESC)
        dic = OrderedDict()
        for res in res_dic:
            dic[res[0]] = res[1]
        return dic

    @classmethod
    def sort_date_list(cls, date_list, date_format, DESC=True):
        """
        1. 对日期进行排序
        2. 输入是列表类型。
        3. 默认降序方式
        """
        res_list = sorted(date_list, key=lambda date: datetime.datetime.strptime(date, date_format), reverse=DESC)
        return res_list

    @classmethod
    def is_valid_date(cls, str, date_format):
        """
        http://www.jb51.net/article/66014.htm
        判断是否是一个有效的日期字符串
        """
        try:
            time.strptime(str, date_format)
            return True
        except:
            return False


if __name__ == "__main__":
    print(DateParser().convert("19901", "%Y.%m"))

    print(DateParser().sort_date_dict({'2010-04-01': '122', '2010-04-03': '2342', '2010-10-02': 'wfwe'}, DateType.YMD))

    test_list1 = ['2010-04-01', '2010-04-03', '2010-04-02']
    test_list2 = ['2010-04-02 00:10:00', '2010-04-03 00:00:00', '2010-04-02 00:19:10']
    print(DateParser().sort_date_list(test_list1, DateType.YMD))
    print(DateParser().sort_date_list(test_list2, DateType.YMD_HMS))

    print(DateParser().find_min_date(test_list1, DateType.YMD))
    print(DateParser().count_time('2010-04-01', DateType.YMD))

    # 返回当前年、月、日
    print("年:" + str(datetime.datetime.now().year) + "月:" + str(datetime.datetime.now().month) + "日:" + str(datetime.datetime.now().day))

    # 两个日期的时间差
    delta = datetime.datetime(2011, 1, 7) - datetime.datetime(2008, 6, 24, 8, 15)
    print("天:" + str(delta.days) + "秒:" + str(delta.seconds))

    # 相对时间减法
    print("日期相减1天" + (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S"))
    print("日期相减1小时" + (datetime.datetime.now() + datetime.timedelta(hours=-1)).strftime("%Y-%m-%d %H:%M:%S"))
    print("日期相减1分钟" + (datetime.datetime.now() + datetime.timedelta(minutes=-1)).strftime("%Y-%m-%d %H:%M:%S"))
    print("日期相减1秒钟" + (datetime.datetime.now() + datetime.timedelta(seconds=-1)).strftime("%Y-%m-%d %H:%M:%S"))

    # 日期转字符串
    print(str(datetime.datetime(2011, 1, 7)))

    # TODO dateuitl 包学习
    """
    dateutil 几乎可以解析人类能够理解的所有日期格式
    """
    print(parse('2011-01-02'))
    print(parse('2011/01/02'))
    print(parse('20110102'))
    print(parse('201101'))
    print(parse('jan 31, 10:45 PM 1997'))
    print(parse('01/02/2011'))
    print(parse('01/02/2011', dayfirst=True))

    # 生成指定日期格式的时间,该日期时间为string
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(date_time)

    # 把指定格式的日期时间转为时间戳
    timestamp = time.mktime(time.strptime(date_time, '%Y-%m-%d %H:%M:%S'))
    print(timestamp)
    print(type(timestamp))

    # 将时间戳转为指定格式的时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)))

    # 判断字符串是否为指定格式的日期格式
    print(DateParser().is_valid_date('2010-04-01', DateType.YMD))
