# coding:utf-8
import pyhdfs
import os


class HDFSService(object):
    def __init__(self):
        self.client = pyhdfs.HdfsClient(hosts='localhost:50070')
        self.sep = os.path.sep

    def file_if_exist(self, hdfs_path):
        return self.client.exists(hdfs_path)

    def upload_to_hdfs(self, local_path, hdfs_path):
        """
        如果hdfs上目录不存则自动创建
        :param local_path:
        :param hdfs_path:
        :return:
        """
        self.client.copy_from_local(local_path, hdfs_path)

    def download_from_hdfs(self, hdfs_path, local_path):
        self.client.copy_to_local(hdfs_path, local_path)

    def delete_from_hdfs(self, hdfs_path):
        self.client.delete(hdfs_path)

    def get_all_file_path(self, hdfs_path):
        file_name_ls = self.client.listdir(hdfs_path)
        return map(lambda file_name: hdfs_path + self.sep + file_name, file_name_ls)


if __name__ == '__main__':
    print(HDFSService().file_if_exist('/cisco/json-2018-01-13'))
    print(HDFSService().download_from_hdfs('/cisco/json-2018-01-13', '/Users/cisco/json-2018-01-13.txt'))
    print(HDFSService().upload_to_hdfs('/Users/cisco/json-2018-01-13.txt','/cisco1/json-2018-01-13'))
