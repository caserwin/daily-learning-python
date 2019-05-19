# coding:utf-8


def open_txt(in_path):
    """
    参考:
    http://www.oschina.net/question/103060_127909
    http://windkeepblow.blog.163.com/blog/static/1914883312013988185783/
    :param in_path:
    :return:
    """
    context = ''
    # in_path = unicode(in_path, "utf8")
    with open(in_path, "rb") as in_file:
        for line in in_file:
            context += line.decode("unicode_escape")
    print(context)


if __name__ == '__main__':
    open_txt('conf/json_test.txt')
