### QQ群导出系统

#### 20211022：

    1、扫描完成的用户无需要等待，可以继续进行调用扫描。
    


#### 20211021：

    1、去除验证码注册系统，通用验证码注册为5678
    
    2、更新firfox加载文件selenium模块，使用最新程序3.10。
    
    3、优化部分代码，补充sql文件。
    
#### 20200530：
  
  1、完善，并设计了用户登入系统。超级管理员观察系统。

  2、用户登入系统：

    1、可以实现注册，登入，修改密码等功能。

    2、通过获取后台二维码，扫描登入后，批量导出QQ群文件。

    3、可以查看自己拥有的时间数。

  3、超级管理员系统：

    1、可以查看用户账号的使用时间，进行充值等等。

    2、查看，下载，用户所导出的QQ群文件。

    3、查看，或者删除，新增公告栏等等。

#### 20200531：

  1、超级管理系统：
    
    1、bug：充值时长时，当小于系统当前时间的时候，并未使用当前时间进行，充值。已修复。
    
    2、对于展示方面已经部分优化界面。和展示内容顺序。
    
#### 20200601：
  
  1、用户登入系统：
    
    1、将二维码验证cookies时间设置成60秒。60秒后失效。
    
    2、bug状态， 当用户多次扫码，并使用同一个QQ的时候，会出现，列表里存在重复的值。需要修改sql语句进行临时修复。但是服务器依然存在相同数据源。
    
#### 20200605：
  
  1、用户登入系统：
    
    1、优化用户初次登入时，修改自己的信息的时候，出现无法进入的问题。已解决。
    
    
#### 20200605：
  
  1、用户登入系统：
    
    1、优化最新的手机号匹配验证。JS。
    
  2、超级管理系统：
  
    1、优化网盘管理系统，未有数据时，强行退出的bug。

#### 20200607：
  
  1、用户登入系统：
    
    1、优化用户修改个人信息时，出现清空信息现象。
    

