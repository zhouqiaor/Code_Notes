# Screen
[Linux screen命令 | 菜鸟教程](https://www.runoob.com/linux/linux-comm-screen.html)

[How To Use Linux Screen | Linuxize](https://linuxize.com/post/how-to-use-linux-screen/)

> Linux screen命令用于多重视窗管理程序。
> Screen为多重视窗管理程序。此处所谓的视窗，是指一个全屏幕的文字模式画面。通常只有在使用telnet登入主机或是使用老式的终端机时，才有可能用到screen程序。

```
screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s <shell>][-S <作业名称>]
```

*参数说明*：

* -A 　将所有的视窗都调整为目前终端机的大小。
* -d<作业名称> 　将指定的screen作业离线。
* -h<行数> 　指定视窗的缓冲区行数。
* -m 　即使目前已在作业中的screen作业，仍强制建立新的screen作业。
* *-r<作业名称> 　恢复离线的screen作业*。
* -R 　先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业。
* -s<shell> 　指定建立新视窗时，所要执行的shell。
* *-S<作业名称> 　指定screen作业的名称*。
* -v 　显示版本信息。
* -x 　恢复之前离线的screen作业。
* -ls或—list 　显示目前所有的screen作业。
* -wipe 　检查目前所有的screen作业，并删除已经无法使用的screen作业。

* Ctrl+a c 创建一个新窗口（带外壳）
* Ctrl+a “ 列出所有窗口
* Ctrl+a 0 切换到窗口0（按数字）
* Ctrl+a A 重命名当前窗口
* Ctrl+a S 将当前区域水平分为两个区域
* Ctrl+a | 将当前区域垂直分为两个区域
* Ctrl+a tab 将输入焦点切换到下一个区域
* Ctrl+a Ctrl+a 在当前区域和上一个区域之间切换
* Ctrl+a Q 关闭除当前区域以外的所有区域
* Ctrl+a X 关闭当前区域
* Ctrl+a d 从屏幕会话中分离

Kill screen session:`screen -S 23536 -X quit`




