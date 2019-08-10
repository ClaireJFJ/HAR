# **HAR数据请求转换模块**

## **概述：**

HAR（HTTP Archive format）是一种通用的HTTP通讯包文档格式。请实现一个可以调用的Python3模块，读取包含HTTP请求通讯的数据序列的HAR文件，将其转化为一系列的http.client请求重放代码，并提供验证结果功能。

## **功能要求**

• 支持GET、POST请求

• 支持HTTP及HTTPS

• 保留原始Headers

• 支持Cookies和Session机制

• 验证结果支持状态码验证和response结果验证

## 使用方法：

```python
import HAR
```

查看该HAR包里有多少个请求：

```python
HAR.numbers('test.har')
```

重放请求并比对数据包是否一致,比对的请求序号为第2个参数

```python
a=HAR.readhar('test.har',0)
a.sendandcompare()
```


