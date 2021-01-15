# JustDailyReport
#  江苏科技大学每日健康上报

###### 在Just.py中找到此程序段填入你的学号和密码。

![](image\1.png)

###### 在data的等号后填入你用fiddler抓包的内容

用fiddler抓包时，打开fiddler，[然后用任意浏览器打开](http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp)并进行当日第一次提交，**注意，一定是当日第一次提交**，第二次及以后提交都无法获取到完整的字段。

![](image\5.png)

![](image\2.png)

###### 注意，tbrq字段和tjsj字段需要改成如图格式：

![](image\3.png)



![](image\4.png)

###### 在图示中填入你的Server酱Key，Server酱是一个集成的可以向微信发通通知的api接口，如果不了解，可以去百度，申请一个Key后填写如图所示。

![](image\6.png)



程序运行成功后Server酱通知：

![](image\7.png)



###### 程序可以部署在腾讯云函数中，并设置定时触发，从而达到每日自动签到的功能。

**函数名称任意，地域选择上海，运行环境选择Python3.6**

![](image\8.png)

**在代码编辑器里粘贴进程序代码，把默认代码删除，然后点击完成。**

![](image\9.png)

**建议按照如图所示设置触发器。**

![](image\10.png)