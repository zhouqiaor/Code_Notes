# Git

Git官网教程，非常完善！！！

[Git - 关于版本控制](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%85%B3%E4%BA%8E%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6)

[服务器上的Git - 协议](https://git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E5%8D%8F%E8%AE%AE)

## 安装Git
```
apt install git
```

## 配置Git
```
git config --global user.name "user_name"
git config —global user.email "email_id"
```

## SSH Keys

[Git - 生成 SSH 公钥](https://git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E7%94%9F%E6%88%90-SSH-%E5%85%AC%E9%92%A5)

[Git：SSH、SSH与HTTP区别、git常用命令_运维_Code farmer Aiden-CSDN博客](https://blog.csdn.net/liuxiaodong400/article/details/81221834)

> Git 可以使用四种不同的协议来传输资料：本地协议（Local），HTTP 协议，SSH（Secure Shell）协议及 Git 协议。    

* 本地创建 SSH Keys

```
ssh-keygen -t rsa -C "XXX@163.com”
```

> -t 指定密钥类型，默认是 rsa ，可以省略。    
-C 设置注释文字，比如邮箱。  
-f 指定密钥文件存储文件名。  


使用默认文件名（推荐）,设置push密码

* 将SSH key上传到github

打开id_rsa.pub`vim ~/.ssh/id_rsa.pub`，拷贝全部内容

登录Github账号，从右上角的设置Settings 进入，然后点击Personal setting 中的SSH and GPG keys，点击New SSH key，把复制的 SSH key 代码粘贴到对应的输入框中，记得 SSH key 代码的前后不要留有空格或者回车。输入别名，默认使用邮箱。

* 测试SSH key

```
ssh -T git@github.com
```


```
# ssh -T git@github.com
The authenticity of host 'github.com (52.74.223.119)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? 

# yes
Warning: Permanently added 'github.com,52.74.223.119' (RSA) to the list of known hosts.
Enter passphrase for key '/root/.ssh/id_rsa': 
Hi XXX! You've successfully authenticated, but GitHub does not provide shell access.
```

配置成功

## commit失效问题

[更改远程仓库的 URL - GitHub 帮助](https://help.github.com/cn/github/using-git/changing-a-remotes-url)

[备份本地git库到GitHub时在能够ssh成功但是无法push的错误的解决_运维_vslyu的博客-CSDN博客](https://blog.csdn.net/vslyu/article/details/80356939)

```
(base) root@iZ5gchbe06niz0Z:~/lab/Chaos# git remote -v
origin  git@github.com:zhouqiaor/Chaos.git (fetch)
origin  git@github.com:zhouqiaor/Chaos.git (push)
```

将目录更改为存储库的本地克隆（如果尚未存在），然后运行：
```
git remote set-url origin git@github.com:username/your-repository.git
```




## 开始Git
仓库初始化`git init`

查看文件的状态`git status`

将工作区的文件保存到暂缓区`git add`

README.md`git add Git.md`

将暂缓区的文件提交到当前分支`git commit`

`git remote add origin https://github.com/user\_name/Mytest.git>`

`git push origin master`

## 取消文件版本控制

[git取消跟踪已版本控制的文件](https://www.cnblogs.com/xxoome/p/9186155.html)

[git rm与git rm —cached - 向着太阳生 - 博客园](https://www.cnblogs.com/toward-the-sun/p/6599656.html)

不再追踪文件改动 `git update-index —assume-unchanged filePath`

恢复追踪文件改动 `git update-index —no-assume-unchanged filePath`

删除暂存区或分支上文件, 同时删除本地文件
```git
git rm file_path
git commit -m ‘delete somefile’
git push
```

删除暂存区或分支上的文件, 保留本地文件
```git
git rm —cached file_path
git rm -r --cached .ipynb_checkpoints
Git commit -m ‘delete remote somefile’
git push
```

## 其它
`git help`

`git config user.name ""`

`git config user.email ""`

查看配置信息命令`git config -l`

[Git清理删除历史提交文件](https://www.jianshu.com/p/7ace3767986a)

[如何解决 GitHub 提交次数过多 .git 文件过大的问题？](https://www.zhihu.com/question/29769130)

垃圾回收`git gc --prune=now`





