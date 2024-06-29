 # jinja

flask中使用render_template函数渲染html的时候，会替换相应的位置

e.g.`render_template("index.html", var1=var1, var2=var2, ...)`

然后可以在index.html中这么搭配使用：
```html
<p>the first var is {{ var1 }}</p>
...

```

## jinja的基本语法
- 控制结构 {% %}
- 变量取值 {{ }}
- 注释 {# #}

## jinja中使用自定义函数
render的时候传入一个指向函数的变量（？）

## jinja2中的过滤器

变量可以经过过滤器进行修改，like一个流水线
　<table border="0">
<tbody>
<tr align="center">
<td>过滤器名称</td>
<td>&nbsp; &nbsp; 说明&nbsp; &nbsp;&nbsp;</td>
</tr>
<tr align="center">
<td>safe</td>
<td>&nbsp;渲染时值不转义</td>
</tr>
<tr align="center">
<td>capitialize</td>
<td>&nbsp;把值的首字母转换成大写，其他子母转换为小写</td>
</tr>
<tr align="center">
<td>&nbsp;lower</td>
<td>&nbsp;把值转换成小写形式&nbsp;</td>
</tr>
<tr align="center">
<td>&nbsp;upper</td>
<td>&nbsp;把值转换成大写形式&nbsp;</td>
</tr>
<tr align="center">
<td>&nbsp;title</td>
<td>&nbsp;把值中每个单词的首字母都转换成大写</td>
</tr>
<tr align="center">
<td>&nbsp;trim</td>
<td>&nbsp;把值的首尾空格去掉</td>
</tr>
<tr align="center">
<td>&nbsp;striptags</td>
<td>&nbsp;渲染之前把值中所有的HTML标签都删掉</td>
</tr>
<tr align="center">
<td>join&nbsp;</td>
<td>&nbsp;拼接多个值为字符串</td>
</tr>
<tr align="center">
<td>&nbsp;replace</td>
<td>&nbsp;替换字符串的值</td>
</tr>
<tr align="center">
<td>&nbsp;round</td>
<td>&nbsp;默认对数字进行四舍五入，也可以用参数进行控制</td>
</tr>
<tr align="center">
<td>int&nbsp;</td>
<td>&nbsp;把值转换成整型</td>
</tr>
</tbody>
</table>

那么如何使用这些过滤器呢？ 只需要在变量后面使用管道(|)分割，多个过滤器可以链式调用，前一个过滤器的输出会作为后一个过滤器的输入。
ps：jinja会默认渲染成html，可能会存在一些符号的转换，使用safe过滤器来保持原文，比如js嵌入场景

``` 
{{ 'abc' | captialize  }}
# Abc
 
{{ 'abc' | upper  }}
# ABC
 
{{ 'hello world' | title  }}
# Hello World
 
{{ "hello world" | replace('world','daxin') | upper }}
# HELLO DAXIN
 
{{ 18.18 | round | int }}
# 18
```
## jinja控制结构

具有单分支，多分支等多种结构，
条件语句不需要使用冒号结尾
### 选择结构

``` 
{% if daxin.safe %}
  a
  {% elif daxin.dead %}
    b
  {% else %}
  c
{% endif %}
```

### 循环结构，只有for
```html
<ul>
  {% for user in users %}
    <li>{{ user.username|title }}</li>
  {% endfor %}
</ul>
```

## jinja2的继承和Super函数
待学习

## 
























<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
end

