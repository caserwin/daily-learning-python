# -*- coding: utf-8 -*-
import time


class TimeParser(object):
    def __init__(self):
        pass

    def parse_time(self, time_str):
        """解析时间字符串, 返回绝对时间戳
        :param time_str: 支持 Unix 时间戳, '%Y-%m-%d %H:%M:%S', '1m', '2h', '-3d', 'now' 几种格式
        """

        is_unix_ts, timestamp = self._check_unix_ts(time_str)
        if is_unix_ts:
            return True, timestamp

        is_absolute_time, timestamp = self._parse_absolute_time(time_str)
        if is_absolute_time:
            return True, timestamp

        is_valid_time, timestamp = self._parse_relative_time(time_str)
        if is_valid_time:
            return True, timestamp
        else:
            return False, None

    @staticmethod
    def _parse_relative_time(relative_time):
        """解析相对时间, 返回绝对时间"""

        now = int(time.time())
        absolute_timestamp = now

        try:
            if relative_time == 'now':
                absolute_timestamp = now
            elif 'm' in relative_time:
                absolute_timestamp = now + int(relative_time[:-1]) * 60
            elif 'h' in relative_time:
                absolute_timestamp = now + int(relative_time[:-1]) * 60 * 60
            elif 'd' in relative_time:
                absolute_timestamp = now + int(relative_time[:-1]) * 60 * 60 * 24
        except ValueError:
            return False, None
        else:
            return True, absolute_timestamp

    @staticmethod
    def _parse_absolute_time(absolute_time):
        try:
            time_stamp = time.mktime(time.strptime(absolute_time, "%Y-%m-%d %H:%M:%S"))
        except (ValueError, TypeError):
            return False, None
        else:
            return True, time_stamp

    @staticmethod
    def _check_unix_ts(time_str):
        try:
            ts = int(time_str)
            if 10 ** 9 <= ts < 10 ** 10:
                return True, ts
            else:
                raise ValueError
        except (ValueError, TypeError):
            return False, None


if __name__ == '__main__':
    pp = TimeParser()
    print(pp.parse_time("-1d"))
    print(pp.parse_time("1492500129"))