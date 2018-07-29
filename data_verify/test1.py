# coding: utf-8
def read_file(file_path):
    """
    读数据
    """
    line_list = set([])
    file_path = unicode(file_path, "utf8")
    with open(file_path, "r") as in_file:
        for line in in_file:
            line_list.add(line.strip())
    return line_list


ls_1 = read_file('./data1/1.txt')
ls_2 = read_file('./data1/2.txt')
ls_841 = read_file('./data1/841.txt')

# print len(ls_1)
print(len(ls_2))

print(len(ls_841 & ls_2))
print(len(ls_841.intersection(ls_2)))
