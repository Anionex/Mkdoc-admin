# C++指针梳理

<blockquote style="border-color:#ffaa00;">指针是C的灵魂</blockquote>

例题切入：

```
设int *p,i:以下正确的语句是()。
A.*p=10:
B.i=p
C.i=*p;
D.p = 2*p + 1:
```

<blockquote style="border-color:#0F52BA"> 基础知识<br>&var取var的引用，返回地址<br>
*p解p的引用，返回值</blockquote>

想要实现一个可以改变a值得函数get，用两个方式

1. **函数签名和调用方式**：
   * **指针传递**：

     <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>cpp</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4 text-left undefined" dir="ltr"><code class="!whitespace-pre hljs language-cpp">int get(int *p)
     get(&a)
     </code></div></div></pre>

     调用时需要使用地址运算符 `&`。
   * **引用传递**：

     <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>cpp</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4 text-left undefined" dir="ltr"><code class="!whitespace-pre hljs language-cpp">int get(int &a)
     get(a)
     </code></div></div></pre>

     调用时直接传递变量，无需地址运算符。

## C++ 引用 vs 指针

可以看出，引用很容易与指针混淆，它们之间有三个主要的不同：

* 不存在空引用。引用必须连接到一块合法的内存。
* 一旦引用被初始化为一个对象，就不能被指向到另一个对象。指针可以在任何时候指向到另一个对象。
* 引用必须在创建时被初始化。指针可以在任何时间被初始化。

<table class="reference notranslate">
<tbody><tr><th width="40%">概念</th><th>描述</th></tr>
<tr><td><a href="https://www.runoob.com/cplusplus/passing-parameters-by-references.html" title="C++ 中通过引用传参">把引用作为参数</a></td><td>C++ 支持把引用作为参数传给函数，这比传一般的参数更安全。</td> </tr>
<tr><td><a href="https://www.runoob.com/cplusplus/returning-values-by-reference.html" title="C++ 中通过引用返回值">把引用作为返回值</a></td><td>可以从 C++ 函数中返回引用，就像返回其他数据类型一样。</td> </tr>
</tbody></table>

## 引用作为返回值

可以把引用作为返回值，就可以有一个骚操作：用括号解引用。

```
double vals[] = {10.1, 12.6, 33.1, 24.1, 50.0};
 
double& setValues(int i) {  
   double& ref = vals[i];  
   return ref;   // 返回第 i 个元素的引用，ref 是一个引用变量，ref 引用 vals[i]
}
 
int main ()
{
   setValues(1) = 20.23; // 改变第 2 个元素
   return 0;
}
```

setValues(1)等价于setValues[1]了。

## 把引用作为参数

常用在swap函数里面，这样可以真实影响到外部变量，但是也会导致潜在风险

为了解决这个一般用const修饰

于是我们有了常见的 `const type &var`！

## 关于一个有趣的问题

给指针所在位置赋值，我们用 `*p = 1`

这个*p解引用之后不是常数吗？常数=常数？？

其实，观察不是指针的类型，也会有类似的情况

我们怎么对a赋值？

a = 1

a其实也是一个数字，那最后是数字 = 数字？

不是的。

* 解引用操作符 `*` 返回的是一个左值，这意味着它可以出现在赋值操作符的左侧，可以被赋值。
* 因此，`*p = 1` 不是常数等于1的形式，而是将1赋值给指针 `p` 所指向的内存位置。

#### 拓展：

`a = 1; b = 1;a = b = 10;`的结果？

=号有结合律

b = 10返回10

a = 10

`*p = &x;a = *p = b?`的结果？

*p = b返回b，为10

a = 10

注释：在C++中，`lvalue = lvalue` 是完全可以的。赋值操作符（`=`）要求其左操作数是一个左值（lvalue），右操作数可以是一个左值或右值。左值表示一个可以标识的内存位置，而右值表示一个临时值或常量。

## 函数指针

```
#include <iostream>
using namespace std;

// 定义一个函数
int add(int a, int b) {
    return a + b;
}

int main() {
    // 定义一个指向返回int类型并带有两个int参数的函数指针
    int (*funcPtr)(int, int) = add;
  
    // 使用函数指针调用函数
    int result = funcPtr(5, 3);
    cout << "Result: " << result << endl; // 输出 8
  
    return 0;
}

```

Q:

> int result = funcPtr(5, 3); 这里为什么不是 int result = *funcPtr(5, 3); 不需要解引用吗，为什么？

A:

> 在 C++ 中，函数指针不需要显式解引用，因为函数调用运算符 `()` 具有更高的优先级，并且对函数指针的调用会自动解引用指针。这意味着：

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>cpp</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4 text-left undefined" dir="ltr"><code class="!whitespace-pre hljs language-cpp">int result = funcPtr(5, 3);
</code></div></div></pre>

等效于：

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>cpp</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4 text-left undefined" dir="ltr"><code class="!whitespace-pre hljs language-cpp">int result = (*funcPtr)(5, 3);
</code></div></div></pre>

> 两者都是合法的，且行为完全相同。编译器会自动将 `funcPtr` 解引用并调用它指向的函数，所以你可以省略显式的 `*`。这使得代码更加简洁和易读。

---

## 神奇的 void 指针

想必大家一定看到过 void 的这些用法：

```
void func();
int func1(void);
```

在这些情况下，void 表达的意思就是没有返回值或者参数为空。

但是对于 void 型指针却表示通用指针，可以用来存放任何数据类型的引用。

下面的例子就 是一个 void 指针：

`void *ptr;`
#6.1 应用场景
void 指针最大的用处就是在 C 语言中实现泛型编程，因为任何指针都可以被赋给 void 指针，void 指针也可以被转换回原来的指针类型， 并且这个过程指针实际所指向的地址并不会发生变化。 比如:

```
int num;
int pi = ##
printf("address of pi: %p\n", pi);
void pv = pi;
pi = (int*) pv;
printf("address of pi: %p\n", pi);
```

这两次输出的值都会是一样:

平常可能很少会这样去转换，但是当你用 C 写大型软件或者写一些通用库的时候，一定离不开 void 指针，这是 C 泛型的基石，比如 std 库里的 sort 函数申明是这样的:

`void qsort(void *base,int nelem,int width,int (*fcmp)(const void *,const void *));`
所有关于具体元素类型的地方全部用 void 代替。

void 还可以用来实现 C 语言中的多态，这是一个挺好玩的东西。

不过也有需要注意的:

#6.2 不能对 void 指针解引用
比如：

```
int num;
void pv = (void)##
*pv = 4; // 错误
为什么？
```

因为解引用的本质就是编译器根据指针所指的类型，然后从指针所指向的内存连续取 N 个字节，然后将这 N 个字节按照指针的类型去解释。

比如 int *型指针，那么这里 N 就是 4，然后按照 int 的编码方式去解释数字。

但是 void，编译器是不知道它到底指向的是 int、double、或者是一个结构体，所以编译器没法对 void 型指针解引用。

## 数组和指针的联系

<blockquote style="border-color:#0F52BA
;">
 实际上数组名并不完全等于指向头位置的指针
</blockquote>

更多：

[C/C++中数组做参数退化为指针 | 编程指北 (csguide.cn)](https://csguide.cn/cpp/basics/array_and_pointer.html#%E6%95%B0%E7%BB%84%E7%9A%84%E5%BC%95%E7%94%A8%E5%81%9A%E5%8F%82%E6%95%B0)

---

参考：

[1][深入理解 C/C++ 指针 | 编程指北 (csguide.cn)](https://csguide.cn/cpp/memory/understanding_of_pointers.html#_2-5-%E7%9C%8B%E4%B8%AA%E5%B0%8F%E9%97%AE%E9%A2%98)

[2][C++ 指针 | 菜鸟教程 (runoob.com)](https://www.runoob.com/cplusplus/cpp-pointers.html)

[3][C/C++中数组做参数退化为指针 | 编程指北 (csguide.cn)](https://csguide.cn/cpp/basics/array_and_pointer.html#%E6%95%B0%E7%BB%84%E7%9A%84%E5%BC%95%E7%94%A8%E5%81%9A%E5%8F%82%E6%95%B0)