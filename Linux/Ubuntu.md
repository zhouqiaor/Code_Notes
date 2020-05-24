# ECS&Linux

## ECS

1. 获取ECS
* 阿里云
* 华为云
* 腾讯云

2. 安装Ubuntu18.04

3. 远程连接
* 阿里云控制台-实例列表
	* VNC  
	* Workbench

## Linux指令

[面试常问的 25+ 个 Linux 命令](http://mp.weixin.qq.com/s?__biz=MzU3NDgxMzI0Mw==&mid=2247484311&idx=2&sn=5ee5aa73a71b00503c8712cebcf24219&chksm=fd2de6c3ca5a6fd5a36b1024f4e93faf0810f2312a9817063198e758bbe6687dbb33bacb539a&mpshare=1&scene=1&srcid=&sharer_sharetime=1585092574637&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)


更新系统源`sudo apt-get update`

创建目录`mkdir newfolder`

删除空目录`rmdir deleteEmptyFolder`

递归删除目录中所有内容`rm -rf deleteFile`

查看服务器磁盘空间`df -h`

查看当前目录占用最大文件`du -h --max-depth=1`

## Linux清理
### 软件清理
`/dev/vda1        40G  7.2G   31G  20% /`

清理旧版本的软件缓存`apt-get autoclean`

清理所有软件缓存`apt-get clean`

删除系统不再使用的孤立软件 `apt-get autoremove`
`/dev/vda1        40G  6.8G   31G  19% /`

所有已安装软件包的列表`apt list —installed`

```
apt-get remove --auto-remove python3
After this operation, 34.3 MB disk space will be freed.
apt-get remove --auto-remove python
After this operation, 1,627 MB disk space will be freed.
```

### 缓存
检查当前 APT 缓存文件的使用率`du -sh /var/cache/apt`

### 包 内核清理

清理Linux下孤立的包`sudo apt-get install deborphan -y`

删除多余的内核`dpkg —get-selections|grep linux`

删除老的内核文件：`sudo apt-get remove 内核文件名`（例如：linux-image-2.6.27-2-generic）

看当前内核`uname -a`

## xrdp远程桌面连接(可不安装)
[*Ubuntu 18.04 上使用xrdp远程桌面连接*](https://blog.csdn.net/qq_25556149/article/details/82216190)

安装 xrdp、tightvncserver：sudo apt-get install tightvncserver xrdp`

安装xubuntu-desktop：`sudo apt-get install xubuntu-desktop`

将xfce4-session写入到文件.xsession中：`echo xfce4-session >~/.xsession`

~~可以不修改_etc_xrdp_startwm.sh和配置_etc_X11_Xsession文件~~

重新启动xrdp服务：`sudo service xrdp restart`
