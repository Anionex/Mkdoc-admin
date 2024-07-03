 
# Bat

## 基础
```
@echo off
:: 关闭命令回显

:: 1. 注释
:: 这是一条注释，用来解释代码

:: 2. 变量
set MY_VAR=Hello, World!
echo %MY_VAR%

:: 3. 用户输入
set /p USER_INPUT=请输入您的名字:
echo 您的名字是 %USER_INPUT%

:: 4. 条件语句
if "%USER_INPUT%"=="admin" (
    echo 欢迎管理员！
) else (
    echo 您不是管理员。
)

:: 5. 循环
echo 使用 for 循环显示 1 到 5:
for /L %%i in (1,1,5) do (
    echo %%i
)

:: 6. 函数（调用另一个批处理文件）
call :MyFunction
goto :EOF

:MyFunction
echo 这是一个函数
goto :EOF

:: 7. 文件操作
:: 创建一个文件
echo 这是一个测试文件 > testfile.txt

:: 读取文件内容
echo 读取文件内容：
type testfile.txt

:: 删除文件
del testfile.txt
echo 文件已删除

:: 8. 子程序（标号）
goto :Menu

:Menu
echo 1. 显示日期
echo 2. 显示时间
echo 3. 退出
set /p CHOICE=请选择一个选项（1-3）:
if "%CHOICE%"=="1" goto ShowDate
if "%CHOICE%"=="2" goto ShowTime
if "%CHOICE%"=="3" goto End
goto Menu

:ShowDate
echo 当前日期是:
date /t
goto Menu

:ShowTime
echo 当前时间是:
time /t
goto Menu

:End
echo 程序结束

```

## 案例：斐波拉契数列输出

```
@echo off
:: 关闭命令回显

:: 读取用户输入
set /p n=请输入斐波那契数列的项数（n）:

:: 检查输入是否为有效数字
setlocal enabledelayedexpansion
for /l %%i in (1,1,%n%) do (
    set "char=%%n:~%%i,1%%"
    if "!char!" lss "0" (
        echo 请输入一个有效的数字。
        goto :EOF
    )
    if "!char!" gtr "9" (
        echo 请输入一个有效的数字。
        goto :EOF
    )
)

:: 初始化前两个斐波那契数
set a=0
set b=1

:: 输出斐波那契数列
echo 斐波那契数列的前 %n% 项是:
for /l %%i in (1,1,%n%) do (
    if %%i==1 (
        echo !a!
    ) else if %%i==2 (
        echo !b!
    ) else (
        set /a temp=a + b
        echo !temp!
        set /a a=b
        set /a b=temp
    )
)

:: 结束脚本
endlocal

```

## setlocal enabledelayedexpansion的作用

```
@echo off
:: 关闭命令回显

:: 未启用延迟变量扩展部分
echo 未启用延迟变量扩展:
set VAR=initial
for %%i in (1 2 3) do (
    set VAR=%%i
    echo VAR=%%VAR%% (在未启用延迟扩展时)
    :: 输出结果: 在每次循环中，VAR 的值都显示为 initial
)

:: 启用延迟变量扩展部分
echo.
echo 启用延迟变量扩展:
setlocal enabledelayedexpansion
set VAR=initial
for %%i in (1 2 3) do (
    set VAR=%%i
    echo VAR=!VAR! (在启用延迟扩展时)
    :: 输出结果: 在每次循环中，VAR 的值会正确显示为 1, 2, 3
)
endlocal

:: 结束脚本
echo.
echo 脚本结束
pause

:: 说明：
:: 在未启用延迟变量扩展时，变量 VAR 在 for 循环内的值不会被正确更新，
:: 因为 %%VAR%% 在循环开始前已经被解析。
:: 启用延迟变量扩展后，通过 !VAR! 语法引用变量，
:: 变量的值会在每次引用时被重新解析，从而正确反映出循环内的更改。

```
## 打开浏览器
start http://...



