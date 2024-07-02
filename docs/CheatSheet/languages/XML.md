 
# XML
可扩展标记语言（英语：Extensible Markup Language，简称：XML）是一种标记语言和用于存储、传输和重构松散数据的文件格式。

## XML vs JSON
JSON 和 XML 都用于接收 web 服务端的数据。

JSON 和 XML在写法上有所不同，如下所示：
```
JSON 实例
{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}
``` 

```
XML 实例
<sites>
  <site>
    <name>菜鸟教程</name> <url>www.runoob.com</url>
  </site>
  <site>
    <name>google</name> <url>www.google.com</url>
  </site>
  <site>
    <name>微博</name> <url>www.weibo.com</url>
  </site>
</sites>
```
___
### JSON 与 XML 的相同之处：

JSON 和 XML 数据都是 "自我描述" ，都易于理解。
<blockquote style="border-color:#aefaff">
ps: 自我描述：不需要额外的文件来描述解释
</blockquote>
JSON 和 XML 数据都是有层次的结构

JSON 和 XML 数据可以被大多数编程语言使用
___
### JSON 与 XML 的不同之处：
JSON 不需要结束标签
JSON 更加简短
JSON 读写速度更快
JSON 可以使用数组

个人想法：**XML是历史遗留问题**