# HAR
### 使用方法：

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

