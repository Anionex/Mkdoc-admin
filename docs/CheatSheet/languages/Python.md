# Python 

## string

### endswith
`"hello world".endswith("orld") == true`
不支持正则。

## os库

### os.path系列

1. os.path.join 
用于把两个路径部分连接起来

2. os.path.isdir


3. os.path.dirname
返回当前路径的目录部分
如果已经是目录，会返回上一级目录


4. os.path.exists()

## 如何创建和删除文件

### 创建：
直接用w模式open一个文件就行

Q:创建dir和多级dir呢？


### 删除：
`os.remove(file)`函数