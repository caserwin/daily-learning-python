import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("./config.conf")
secs = cf.sections()
opts = cf.options("hdfs")
kvs = cf.items("hdfs")
in_path = cf.get("hdfs", "host")

print(secs)
print(opts)
print(kvs)
print(in_path)