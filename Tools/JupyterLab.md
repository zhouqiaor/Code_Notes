# Conda&JupyterLab
## 安装Miniconda
[清华源Anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/)
[生信分析利器：JupyterLab](http://mp.weixin.qq.com/s?__biz=MzI1MTIwMjkyNg==&mid=2650431529&idx=1&sn=9be73c78a8ea00965477918f309f9204&chksm=f1f85c28c68fd53e336c4257cb973aa282e5ca388750539ddaaa09a4ec8875b551a85244477c&mpshare=1&scene=1&srcid=0305Vfsoi2NiBtC4ervLya0r&sharer_sharetime=1583404361829&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)

1. 下载Miniconda3-latest-Linux-x86_64.sh

```
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2. 安装

```
sh Miniconda3-latest-Linux-x86_64.sh
```

```
Miniconda3 will now be installed into this location:
/root/miniconda3
  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below
```

是否添加 conda 信息到 .bashrc 文件中，每次打开新的命令行窗口都自动启动 conda base？这个最好选择‘是’，不然自己设置会麻烦一些，选否也没什么太大问题  

```
Do you wish the installer to initiateize Minionda3 by running condo init? [yes|no]
[no] >>> yes
```

打开新的命令行或者执行`source ~/.bashrc`启动base环境

## 安装配置JupyterLab

[云服务器搭建神器JupyterLab（多图）](https://www.zhihu.com/tardis/sogou/art/48387217)

[远程部署jupyter notebook-问答-阿里云开发者社区-阿里云](https://developer.aliyun.com/ask/213538?spm=a2c6h.13524658)

[搭建远程 JupyterLab 服务 - 简书](https://www.jianshu.com/p/6611b656bfc9)

1. 安装

```shell
conda install jupyterlab
```

2. 配置

* 获得sha1

```
# ipython

>>> from notebook.auth import passwd
>>> passwd()
Enter password: 
Verify password: 
Out[2]: 'sha1:XXX:XXX’
```

* 生成配置文件`jupyter lab —generate-config`

```
Writing default config to: /root/.jupyter/jupyter_notebook_config.py
```

* 编辑配置文件

```
vim /root/.jupyter/jupyter_notebook_config.py
```

```
c.NotebookApp.allow_root = True
c.NotebookApp.ip = ‘0.0.0.0’
c.NotebookApp.notebook_dir = u’JupyterLab’#在原始路径下新建JupyterLab文件夹
c.NotebookApp.open_browser = False
c.NotebookApp.password = u’sha1:XXX:XXX’
c.NotebookApp.port = 8080
```

3. 运行
* 安装窗口管理器`apt install screen`
* 新建窗口`screen -S lab`
* 运行`jupyter lab`
不明错误，有时会导致远程连接的加载速度

```
[I 21:43:53.998 LabApp] 302 GET /lab? (117.182.183.87) 1.76ms
[I 21:44:02.873 LabApp] 302 POST /login?next=%2Flab%3F (117.182.183.87) 1.32ms
[W 21:44:35.581 LabApp] Could not determine jupyterlab build status without nodejs
```


## 扩展插件
Jupyterlab的插件都是基于NodeJS安装的，但同时所有npm的包也会自动保存到当前的python环境中（或虚拟环境）

`conda install -c conda-forge nodejs`

## 安装R
[R环境安装](http://mp.weixin.qq.com/s?__biz=MzU2ODU3ODY0Nw==&mid=2247484826&idx=1&sn=5939bf8bb8e2df374f75b031e0339f6f&chksm=fc8a82a2cbfd0bb4bfb199bd910695c2a5f50920a09cf1a33852625f954109f3b09a897392f8&mpshare=1&scene=1&srcid=0305FzYhRyZgBwRFYFf1pND9&sharer_sharetime=1583414077483&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)


## Conda
### 换源
> TUNA 还提供了 Anaconda 仓库与第三方源（conda-forge、msys2、pytorch等， [查看完整列表](https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/) ）的镜像，各系统都可以通过修改用户目录下的 .condarc 文件。Windows 用户无法直接创建名为 .condarc 的文件，可先执行 `conda config --set show_channel_urls yes` 生成该文件之后再修改。  

* vim编辑
[CentOS_Linux神器vim编辑器实用基本操作](http://mp.weixin.qq.com/s?__biz=MzIwNjM2Njc1NA==&mid=2247484612&idx=1&sn=bbc089e542fd5fd80b3eaaea2d9b6a2f&chksm=9723f589a0547c9f537346b95a5b296e70e537ac77ea2150892de45f441d3ad21ee1e1375448&mpshare=1&scene=1&srcid=0211VpYK2dyZDnMVoFPmQ0VC&sharer_sharetime=1581398143353&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)
使用vim编辑文件`vim /root/.condarc`

> 用法:i  
> 表示进入编辑模式并且在光标所在字符的前面开始编辑内容，小写的I，比较常用。  

```
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

>  用法:ESC + wq  
> 表示保存文件修改的内容并退出文件。  

### Conda命令
* 基本

```
conda list # 查看安装了哪些包。 
conda update conda # 检查更新当前conda 
conda update anaconda # 检查更新anaconda 
conda update python # 检查更新Python
```

* Kernel

```
jupyter kernelspec list  # 查看已安装的内核和位置
conda install ipykernel  # 安装ipykernel包到当前的python环境中
Python -m ipykernel install --name XXX  # 
```

* 环境管理

```
conda info --envs  # 查看环境
conda env export > env.yml  # 导出目前激活的环境
conda env export --no-builds> env.yml
conda env create -f env.yml  # 粘贴环境
conda create --name zhpy3u python=3.7  # 创建环境
conda env remove -n zhpy3u  # 删除环境
```

## 安装Xeus-Cling

[Xeus-Cling: Run C++ code in Jupyter Notebook | Learn OpenCV](https://www.learnopencv.com/xeus-cling-run-c-code-in-jupyter-notebook/)

[像Python一样玩C/C++](http://mp.weixin.qq.com/s?__biz=MzI2NjYwOTAyMg==&mid=2247485898&idx=1&sn=97baa6a53e3eefcb8f7ecb226f339e93&chksm=ea8ac1dbddfd48cd3907991a9a613ebc69a85174dc0c0bd7b1d9962dfdda34e3f7f1d08a7a37&mpshare=1&scene=1&srcid=0314CSXEjH0M0icHE7AZOKSw&sharer_sharetime=1584180577711&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)

```
conda install -c conda-forge xeus-cling
```