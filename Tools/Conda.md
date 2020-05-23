# Conda
---
* 安装Miniconda

[清华源Anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/)

[生信分析利器：JupyterLab](http://mp.weixin.qq.com/s?__biz=MzI1MTIwMjkyNg==&mid=2650431529&idx=1&sn=9be73c78a8ea00965477918f309f9204&chksm=f1f85c28c68fd53e336c4257cb973aa282e5ca388750539ddaaa09a4ec8875b551a85244477c&mpshare=1&scene=1&srcid=0305Vfsoi2NiBtC4ervLya0r&sharer_sharetime=1583404361829&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)

```
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
```
---
* 换源

> TUNA 还提供了 Anaconda 仓库与第三方源（conda-forge、msys2、pytorch等， [查看完整列表](https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/) ）的镜像，各系统都可以通过修改用户目录下的 .condarc 文件。Windows 用户无法直接创建名为 .condarc 的文件，可先执行 `conda config --set show_channel_urls yes` 生成该文件之后再修改。  

[CentOS_Linux神器vim编辑器实用基本操作](http://mp.weixin.qq.com/s?__biz=MzIwNjM2Njc1NA==&mid=2247484612&idx=1&sn=bbc089e542fd5fd80b3eaaea2d9b6a2f&chksm=9723f589a0547c9f537346b95a5b296e70e537ac77ea2150892de45f441d3ad21ee1e1375448&mpshare=1&scene=1&srcid=0211VpYK2dyZDnMVoFPmQ0VC&sharer_sharetime=1581398143353&sharer_shareid=96c4a266066ac094d370df9ca62a44e8#rd)

使用vim编辑文件`vim /root/.condarc`

> 用法:i   进入编辑模式并且在光标所在字符的前面开始编辑内容。  
> 用法:ESC + :wq  保存文件修改的内容并退出文件。  

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
---
## Conda命令
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
