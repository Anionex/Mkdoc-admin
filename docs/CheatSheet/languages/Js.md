# Js 

## const & let & var


以下是 `var`、`let` 和 `const` 在 JavaScript 中的几个主要区别：

1. **作用域**：
   - `var`：函数作用域。
   - `let` 和 `const`：块作用域。

2. **重复声明**：
   - `var`：允许重复声明。
   - `let` 和 `const`：不允许在同一作用域内重复声明。

3. **提升（Hoisting）**：
   - `var`：变量提升并初始化为 `undefined`。
   - `let` 和 `const`：变量提升但不初始化（存在暂时性死区）。

4. **赋值**：
   - `var` 和 `let`：可以更新。
   - `const`：不能更新，声明时必须初始化。

5. **全局作用域**：
   - `var`：成为全局对象的属性。
   - `let` 和 `const`：不会成为全局对象的属性。

更多详细信息，请参考 [菜鸟教程](https://www.runoob.com/js/js-let-const.html)。