# -*- coding: utf-8 -*-

import re

email_regex = r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.(?:com|cn|net)'
url_regex = r"\"?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\"?"
ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ip_port_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
date_regex_standard = r"\d{1,4}[./-]\d{1,2}[./-]\d{1,2}.\d{1,2}[./: -]\d{1,2}[./: -]\d{1,2}"


class LogText(object):
    def __init__(self, text):
        self._text = text

    def get_log(self):
        return self._text


class EmailWrapper(object):
    def __init__(self, log_text):
        self.log_text = log_text
        self.wrap_log = None

    def get_log(self):
        """
        整体匹配即可,匹配邮箱
        """
        return re.sub(email_regex, '$email$', self.log_text.get_log())


class UrlWrapper(object):
    def __init__(self, log_text):
        self.log_text = log_text

    def get_log(self):
        """
        整体匹配即可,用于匹配url
        """
        return re.sub(url_regex, '$url$', self.log_text.get_log())


class DataStandardWrapper(object):
    def __init__(self, log_text):
        self.log_text = log_text

    def get_log(self):
        """
        匹配2016*09*25*03*16*20形式日期,其中*代表空格、'/'、'-'、':'、'.'等符号。
        """
        return re.sub(date_regex_standard, '$date$', self.log_text.get_log())


class IpWrapper(object):
    def __init__(self, log_text):
        self.log_text = log_text

    def get_log(self):
        """
        整体匹配即可,先匹配ip+端口号,再匹配ip
        """
        return re.sub(ip_regex, '$ip$', re.sub(ip_port_regex, '$ip+port$', self.log_text.get_log()))


if __name__ == "__main__":
    log_text = LogText('我的163邮箱是erwin@163.com，经常在http://www.google.com上搜索问题。2016-07-14 '
                       '09:21:23是我的生日。http://www.baidu.com')

    log_text_wrap = UrlWrapper(EmailWrapper(log_text))
    print(log_text_wrap.get_log())

    log_text_wrap = DataStandardWrapper(EmailWrapper(UrlWrapper(log_text)))
    print(log_text_wrap.get_log())