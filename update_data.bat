@echo off
REM 切换到E:\目录
cd /d E:\

REM 运行generate_date.py脚本
python generate_date.py

REM 使用scp命令上传文件
REM 请确保你的SSH密钥已经配置正确
scp E:\data.txt root@8.217.222.156:/var/www/fxyenvstation.us.kg/