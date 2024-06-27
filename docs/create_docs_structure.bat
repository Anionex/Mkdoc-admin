@echo off
REM 创建文件夹结构
mkdir CheatSheet
mkdir CheatSheet\languages
mkdir CheatSheet\OS

REM 创建 Markdown 文件并写入初始内容
echo # Home > Home.md
echo # C & C++ > CheatSheet\languages\C & C++.md
echo # Python > CheatSheet\languages\Python.md
echo # Js > CheatSheet\languages\Js.md
echo # Math > CheatSheet\Math.md
echo # Algorithms > CheatSheet\Algorithms.md
echo # Linux > CheatSheet\OS\Linux.md
echo # Windows > CheatSheet\OS\Windows.md
echo # MacOS > CheatSheet\OS\MacOS.md
echo # Projects > Projects.md

echo Documentation structure created successfully!
