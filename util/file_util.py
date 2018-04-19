# coding:utf-8
from os.path import join, getsize
import shutil
import os

"""
http://andylin02.iteye.com/blog/1071448
http://blog.mimvp.com/2015/07/python-to-get-directory-size/
"""


class FileUtil(object):
    @staticmethod
    def clear_all_files(path):
        """
        清空一个文件夹下所有文件
        """
        shutil.rmtree(path)
        os.mkdir(path)

    @staticmethod
    def get_dir_size(path):
        """
        循环遍历,得到一个文件夹下所有文件的总和大小
        """
        size = 0
        for root, dirs, files in os.walk(path):
            size += sum([getsize(join(root, name)) for name in files])
        return size

    @staticmethod
    def get_all_file_path(path):
        """
        循环遍历,得到一个文件夹第一层下的文件路径
        """
        import os
        file_name_list = os.listdir(path)
        return [path+os.sep+file_name for file_name in file_name_list]

    @staticmethod
    def get_all_file_name(path):
        """
        循环遍历,得到一个文件夹下第一层下的文件名
        """
        import os
        file_name_list = os.listdir(path)
        return file_name_list

    @staticmethod
    def write_file(file_path, context, method='a'):
        """
        写数据到一个文件
        :param file_path:
        :param method: 'a'表示默认为追加方式, 'wb'表示覆盖或者创建文件写入
        :param context:
        """
        file_path = unicode(file_path, "utf8")
        with open(file_path, method) as fo:
            fo.write(context)
        # 关闭打开的文件
        fo.close()

    @staticmethod
    def read_file(file_path):
        """
        读数据
        """
        line_list = []
        file_path = unicode(file_path, "utf8")
        with open(file_path, "r") as in_file:
            for line in in_file:
                line_list.append(line.strip())
        return line_list

if __name__ == '__main__':
    print(FileUtil.get_all_file_path('/Users/haizhi/xyd'))
