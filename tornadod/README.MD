一. 线程池提高并发处理量
1. 使用Tornado自带的concurrent的语法糖run_on_executor。
2. 使用Python自带的concurrent的ThreadPoolExecutor线程池库。


## demo1
[Tornado高并发处理方法](https://blog.csdn.net/qq_28893679/article/details/69437496)

## demo2 
功能：单进程+多线程方式，实现非阻塞

参考：[Tornado协程中调用异步非阻塞函数](https://www.zhihu.com/search?type=content&q=tornado%20%E5%BC%82%E6%AD%A5%20%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)


demo2 问题:
1. 这种写法每个进程中最多能开多少个线程，也就是这中写法请求并发数量是多少？
2. 这种写法和tornado中 ```@tornado.gen.coroutine``` 写法有什么区别？