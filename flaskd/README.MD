## 1. Flask 异步

端口设置为 5001， 所以浏览器中请求：
```
http://127.0.0.1:5001/jobs
```

浏览器立即返回：
```
Two jobs was launched in background!
```

控制台打印：
```bash
Task #1 started!
Task #2 started with args: hello 123!
Task #2 is done!
Task #1 is done!
```

## 2. 同步/异步、阻塞/非阻塞

这里的异步是指并发执行任务，不是说一个任务处理完后，串行处理下一个任务

1. 同步与异步：同步和异步关注的是消息通信机制 (synchronous communication/ asynchronous communication)。

    * 所谓同步，就是在发出一个*调用*时，在没有得到结果之前，该*调用*就不返回。但是一旦调用返回，就得到返回值了。换句话说，就是由*调用者*主动等待这个*调用*的结果。
    * 而异步则是相反，*调用*在发出之后，这个调用就直接返回了，所以没有返回结果。换句话说，当一个异步过程调用发出后，调用者不会立刻得到结果。而是在*调用*发出后，*被调用者*通过状态、通知来通知调用者，或通过回调函数处理这个调用。

2. 阻塞与非阻塞：阻塞和非阻塞关注的是程序在等待调用结果（消息，返回值）时的状态.

    * 阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才会返回。
    * 非阻塞调用指在不能立刻得到结果之前，该调用不会阻塞当前线程。


[怎样理解阻塞非阻塞与同步异步的区别？](https://www.zhihu.com/question/19732473/answer/20851256)

## 3. 参考

1. [在 Flask 中使用简单异步任务](https://zhuanlan.zhihu.com/p/30897711)
1. [flask application with background threads](https://stackoverflow.com/questions/22615475/flask-application-with-background-threads)