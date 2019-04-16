### 元素查找
Pandas 的 DataFrame 不像Spark中的DataFrame或者是Flink中的DataSet/DataStream，没有SQL/Table API，即不能通过where(),filter() 或者是SQL的方式查询，所以查找挺不方便的。

查找一共有三种方式，[]、loc[]、iloc[]。

1. []，根据列标签查找。
2. loc[]函数，基于索引查找，第一个参数是行标签，第二个参数是列标签。
3. iloc[]函数，基于位置查找。

### dataframe 删除行列
1. del: 删除dataframe中指定的列，这个是直接影响当前的dataframe，注意 del是python中的内置语句，没有返回值。如：del df['a']
2. drop：不会影响原来的dataframe，dop方法会返回一个删除了指定列的新的dataframe

### 项目
1. https://github.com/hangsz/pandas-tutorial
2. https://github.com/fengdu78/machine_learning_beginner/tree/master/pandas/Pandas_Exercises

### 参考
1. [pandas dataframe](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
2. [23种Pandas核心操作，你需要过一遍吗？](https://zhuanlan.zhihu.com/p/43018099)
3. [十分钟搞定pandas](http://www.shizhuolin.com/2015/04/19/978.html?from=timeline&isappinstalled=0)