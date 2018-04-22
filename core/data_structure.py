import json

# 有序字典
import collections
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
print(dic)

# 字典转json
print(json.dumps(dic, ensure_ascii=False))