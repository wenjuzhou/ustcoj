# USTC-OJ 原型设计说明 #

## 目录 ##

### 未登录前主页面 ###
### 创建账号页面 ###
### 登陆页面 ###
### 登陆后主页面 ###
### 程序列表页面 ###
### 群组列表页面 ###
### 打标签页面 ###
### 状态页面 ###
### 排名页面 ###
### 用户相关页面 ###

## 各页面具体描述 ##

### 未登录前主页面 ###

<p>主要包含有七个模块</p>

- USTC-OJ图表
	- 跳转到当前页面
- 导航栏
	- problem:跳转到程序列表页面
	- contest:跳转到群组列表页面
	- access:跳转到打标签页面
	- sign in:跳转到登陆页面
- create count按钮
	- 跳转到创建账号页面
- problem按钮
	- 跳转到程序类别页面
- contest按钮
	- 跳转到群组列表页面
- problem按钮
	- 跳转到打标签页面
- 网站基本信息

<p>未登录主页面展示图：</p>
![](pageimages/main.png)


### 创建账号页面 ###

<p>主要包含有三个模块</p>

- USTC-OJ图表
	- 跳转到未登录前主页面
- 导航栏
	- problem:跳转到程序列表页面
	- contest:跳转到群组列表页面
	- access:跳转到打标签页面
	- sign in:跳转到登陆页面
- 创建账号
	- username:用户名
	- password:用户密码
	- passowrd commit:密码确认
	- email:邮箱
	- class:用户类别，根据用户类别决定是否绑定idcard
	- idcard：学生卡/教师卡号
	- idpassword：学生卡/教师卡密码
	- register:确认注册按钮

<p>创建账号页面展示图：</p>
![](pageimages/createcount.png)


### 登陆页面 ###

<p>主要包含有三个模块</p>

- USTC-OJ图表
	- 跳转到未登录前主页面
- 导航栏
	- problem:跳转到程序列表页面
	- contest:跳转到群组列表页面
	- access:跳转到打标签页面
	- sign in:跳转到登陆页面
- 创建账号
	- username:用户名
	- password:用户密码
	- sign in:确认登陆
	
<p>创建账号页面展示图：</p>
![](pageimages/signin.png)