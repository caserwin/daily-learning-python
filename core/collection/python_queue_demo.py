# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 下午2:35
# @Author  : yidxue

from collections import deque

if __name__ == "__main__":
    queue = deque(['fsf', 'wefw', 'egew'], 3)
    queue.append("ssss")
    print(queue)
    queue.popleft()
    print(queue)
    queue.pop()
    print(queue)
    print(len(queue))
    for i in queue:
        print(i)
