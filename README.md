# autoWeb
This will show how to build a website and transmiss your date to websit automation  

Follow the stips，you will achieve your own website.  
Prerequisites for completing the project：  
1.You need to regist a Register a domain name.  
2.You should have a Virtual Private Server(VPS),this will recommand AWS Cloud Server,because that's free.  
&nbsp;&nbsp;&nbsp;&nbsp; If you are in China,i will recommand you use aliyun,that's 3 month free for college students, and choose  
&nbsp;&nbsp;&nbsp;&nbsp; hongkong sit.  
3.You had better konw some linux command.  


The some detals are as follows:  
1.Setting up an Amazon server  
![image](https://github.com/user-attachments/assets/956d3d49-aff7-421b-a617-dff50ee2e44b)  

2.Connect to your server  
3.DNS 配置：  
你需要将域名 xxx.com 指向你的服务器 IP 地址。这可以通过你的域名注册商的 DNS 管理界面完成。  
具体步骤如下：  
登录到你的域名注册商账户。  
找到 DNS 管理 或 域名解析 设置。  
添加一个 A 记录，将 域名 指向你的服务器 IP 地址  

4.云服务器中安装 Nginx，在/hoem目录下  
commond：  
sudo apt update  
sudo apt install nginx  

5.将 Nginx 的配置文件放在 /home 目录中，然后通过符号链接将其链接到 Nginx 的配置目录。以下是具体步骤  

创建 Nginx 配置文件：sudo nano /home/envbase.us.kg.conf  

在文件中添加以下内容：  
server {
    listen 80;
    server_name envbase.us.kg;

    root /home/my_website;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

创建符号链接：  
将配置文件链接到 Nginx 的 sites-available 目录：  
sudo ln -s /home/envbase.us.kg.conf /etc/nginx/sites-available/envbase.us.kg  

启用配置：  
创建一个符号链接到 sites-enabled 目录以启用配置：  
sudo ln -s /etc/nginx/sites-available/envbase.us.kg /etc/nginx/sites-enabled/  

测试 Nginx 配置：  
确保配置是正确的：sudo nginx -t  

重新加载 Nginx：  
如果配置测试成功，重新加载 Nginx 以应用新配置：sudo systemctl reload nginx  

6.在服务器的 /home 目录下建立一个简单的网页:  mkdir /home/my_website  
进入创建的目录：cd /home/my_website  
创建一个简单的 HTML 文件：  
echo "<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple webpage.</p>
</body>
</html>" > index.html
