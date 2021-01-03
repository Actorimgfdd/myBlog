## 一、环境配置

1. 下载，安装python，中文，路径智能，npm，npm智能，vtur，vue 3代码段，vscode-图标，活动服务器这些插件

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX[Https://www.dcloud.io/hbuilderx.html](https://www.dcloud.io/hbuilderx.html)

4. 安装小程序开发工具[Https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)

## 二、安装git：[Https://git-scm.com/；](https://git-scm.com/；)

1. 创建远程仓库myBlog

2. 初始化本地仓库，也就是在本地的myBlog文件夹下执行：`git init`、执行完后会创建一个.git的隐藏文件

3. 远程仓库和本地仓库进行关联：`git remote add origin "你的远程仓库地址"`

4. 如果出现错误，ssh没有创建

5. 先去创建密钥：`ssh-keygen`，一路Enter，生成密钥

6. 查看生成的密钥`cat ~/.ssh/id_rsa.pub`，将密钥写入到GitHub上的设置下的SSH和GPG键下

7. 推送四步骤：

   状态查看发生变化的文件  `git status`

   追踪所有发生变化的文件  `git add . `

   GIT提交-m“备注”提交到本地仓库   `git  commit -m "备注"`

   > 出现错误：fatal: unable to auto-detect email address
   >
   > ![image-20210103154733239](E:\Program Files\Typora\images\image-20210103154733239.png)
   >
   > 在终端中运行图中的两行代码！！！！！！

   Git Push-u 源母版第一次提交到远程仓库     `git push -u origin master`

   GIT推送之后的提交 `git push`

## 三、创建myBlog项目

1. 空文件夹下，执行`django-admin startproject myBlog`;
2. 给myBlog创建虚拟环境，使用：`python -m venv env`
3. 进入到虚拟环境，Windows下：`.\\env\\Scrtipst\\activate`;
4. 退出虚拟环境，Windows下：`deactivate`；
5. 使用VSCode打开myBlog，执行：`python manage.py startapp articles`

## 四、创建文章的模型