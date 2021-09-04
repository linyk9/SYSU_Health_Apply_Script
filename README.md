# SYSU-Health-Apply-Script
#### 可用于中山大学的健康申报系统
#### 执行可以每日申报
---
# 食用方法
### **1 selenium安装及配置**
#### **1.1 selenium安装**
###### 命令行下使用以下pip命令
###### pip install selenium (记得换清华源)
#### 1.2 配置
###### 在git上下载最新的geckodriver.exe 
###### 网址:https://github.com/mozilla/geckodriver/releases
###### 将geckodriver.exe其放在Chrome/Firefox安装目录下
###### 将浏览器安装目录添加到系统环境变量中
---
### 2 pytesseract、tesseract安装及配置
#### 2.1 pytesseract安装
###### 命令行下使用以下pip命令
###### pip install pytesseract (记得换清华源)
#### 2.2 tesseract安装及配置
###### 下载最新正式版tesseract
###### 网址:https://digi.bib.uni-mannheim.de/tesseract/
###### 安装tesseract-ocr-w64-setup-v5.0.0.20190623.exe
###### 将tesseract安装目录添加到系统环境变量中
---
### 3 添加自己的NetID、密码
###### 打开healthApply.py
###### 82行的语句
###### `apply = Apply('你的NetID', '密码')`
###### 用自己的NetID、密码替换即可
---
# 历史版本
---
### V 1.0
###### 搭建基础申报框架
---
