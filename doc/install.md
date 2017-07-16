## 部署July

安装CentOS是使用`mini`版的镜像安装的，所以在部署的过程中我们安装所需要的所有依赖包。

---

- 环境查看

```bash
[root@CentOS ~]# cat /etc/redhat-release 
CentOS Linux release 7.3.1611 (Core) 
[root@CentOS ~]# uname -a
Linux CentOS 3.10.0-514.10.2.el7.x86_64 #1 SMP Fri Mar 3 00:04:05 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```

### 安装Python3

项目是在py3环境下进行编码的，正好Centos默认的py版本是2，我们还需要安装py3才能让程序run起来，在此之前，需要安装开发工具包，因为要编译安装Python

```bash
[root@CentOS ~]# yum -y group install "Development Tools"
```

安装Python的依赖包，不安装依赖可能安装完成后没有pip3 软件。

```bash
[root@CentOS ~]# yum -y install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel vim
```

下载目前最新的Python3.5.x

```bash
[root@CentOS ~]# wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
```

> 可能你需要通过`yum -y install wget`

解压编译安装

```bash
[root@CentOS ~]# tar xf Python-3.5.3.tgz 
[root@CentOS ~]# cd Python-3.5.3
[root@CentOS Python-3.5.3]# ./configure --prefix=/usr/local/python3.5
[root@CentOS Python-3.5.3]# make
[root@CentOS Python-3.5.3]# make install
```

为`pip3`和`python3`创建链接

```bash
[root@CentOS Python-3.5.3]# ln -fs /usr/local/python3.5/bin/python3 /usr/local/bin/
[root@CentOS Python-3.5.3]# ln -fs /usr/local/python3.5/bin/pip3 /usr/local/bin/
```

验证安装

```bash
[root@CentOS Python-3.5.3]# pip3 -V
pip 9.0.1 from /usr/local/python3.5/lib/python3.5/site-packages (python 3.5)
[root@CentOS Python-3.5.3]# python3 -V
Python 3.5.3
```

### 使用虚拟环境进行项目

项目运行和开发都在虚拟环境中运行，需要安装`virtualenv`

```bash
[root@CentOS Python-3.5.3]# cd
[root@CentOS ~]# pip3 install virtualenv
```

- 创建并切换到虚拟环境

```bash
[root@CentOS ~]# mkdir /usr/local/virtualenv
[root@CentOS ~]# cd /usr/local/virtualenv/
[root@CentOS virtualenv]# /usr/local/python3.5/bin/virtualenv July
[root@CentOS virtualenv]# source July/bin/activate
(July) [root@CentOS virtualenv]# cd
```

- 部署项目

```bash
# 从github下载项目
(July) [root@CentOS ~]# git clone https://github.com/anshengme/July.git
(July) [root@CentOS ~]# cd July/
# 安装相关以来包
(July) [root@CentOS July]# pip install -r requirements.txt
# 生成数据库表
(July) [root@CentOS July]# python manage.py makemigrations users blog admin
(July) [root@CentOS July]# python manage.py migrate
# 使用测试数据库
(July) [root@CentOS July]# rm -f db.sqlite3 
(July) [root@CentOS July]# mv doc/july.sqlite3 db.sqlite3
# 运行
(July) [root@CentOS July]# python manage.py runserver
```

新打开一个`bash`窗口查看是否运行成功

```bash
[root@CentOS ~]# curl -I 127.0.0.1:8000
# 看状态码就成
HTTP/1.0 200 OK
Date: Wed, 15 Mar 2017 06:34:44 GMT
Server: WSGIServer/0.2 CPython/3.5.3
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Vary: Cookie
Set-Cookie:  csrftoken=4W7di5dolFM6zoGK9LW2chM8lDsTGdqPYiuC5X7OL98w4az56mlr1EYKd27tWKxw; expires=Wed, 14-Mar-2018 06:34:44 GMT; Max-Age=31449600; Path=/
```

### 安装Nginx

```bash
(July) [root@CentOS July]# cd
(July) [root@CentOS ~]# wget http://nginx.org/download/nginx-1.10.3.tar.gz
(July) [root@CentOS ~]# yum -y install openssl openssl-devel pcre pcre-devel libxml2 libxml2-devel xslt libxslt-devel gd gd-devel perl perl-devel perl-ExtUtils-Embed GeoIP-devel
(July) [root@CentOS ~]# tar xf nginx-1.10.3.tar.gz 
(July) [root@CentOS ~]# cd nginx-1.10.3
(July) [root@CentOS nginx-1.10.3]# ./configure --prefix=/etc/nginx \
--prefix=/etc/nginx \
--sbin-path=/usr/sbin/nginx \
--modules-path=/usr/lib/nginx/modules \
--conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--pid-path=/var/run/nginx.pid \
--lock-path=/var/run/nginx.lock \
--http-client-body-temp-path=/var/cache/nginx/client_temp \
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \
--with-http_ssl_module \
--with-http_realip_module \
--with-http_addition_module \
--with-http_sub_module \
--with-http_dav_module \
--with-http_flv_module \
--with-http_mp4_module \
--with-http_gunzip_module \
--with-http_gzip_static_module \
--with-http_random_index_module \
--with-http_secure_link_module \
--with-http_stub_status_module \
--with-http_auth_request_module \
--with-http_xslt_module=dynamic \
--with-http_image_filter_module=dynamic \
--with-http_geoip_module=dynamic \
--with-http_perl_module=dynamic \
--with-threads \
--with-stream \
--with-stream_ssl_module \
--with-http_slice_module \
--with-mail \
--with-mail_ssl_module \
--with-file-aio \
--with-http_v2_module \
--with-ipv6
(July) [root@CentOS nginx-1.10.3]# make
(July) [root@CentOS nginx-1.10.3]# make install
```

#### 配置Nginx

```bash
(July) [root@CentOS nginx-1.10.3]# vim /etc/nginx/nginx.conf
user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    use epoll;
    multi_accept on;
    worker_connections  1024;
}

http {
    server_tokens off;
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    charset utf-8;

    sendfile        on;
    tcp_nopush      on;
    tcp_nodelay     on;

    keepalive_timeout  65;

    gzip                        on;
    gzip_disable                "msie6";
    gzip_vary                   on;
    gzip_proxied                any;
    gzip_comp_level             6;
    gzip_buffers                16 8k;
    gzip_http_version           1.1;
    gzip_types                  text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    include /etc/nginx/conf.d/*.conf;
}
(July) [root@CentOS nginx-1.10.3]# vim /etc/nginx/conf.d/july.conf
server {
    listen     80 ;
    server_name localhost;
    charset     utf-8;
    client_max_body_size 64M;
    access_log /var/log/nginx/logs/july.access.log main;
    error_log /var/log/nginx/logs/july.error.log warn;
    location /static/blog {
        alias /root/July/apps/blog/static/blog;
    }
    location /static {
        alias /root/July/static;
    }
    location /admin/article/lib {
        alias /root/July/static/editormd/lib;
    }
    location /admin/article/plugins {
        alias /root/July/static/editormd/plugins;
    }
    location /media {
        alias /root/July/media;
    }
    location / {
        proxy_pass http://127.0.0.1:8000/;
    }
}
```

启动Nginx

```bash
# 启动之前先创建Nginx所需要的目录
(July) [root@CentOS nginx-1.10.3]# mkdir -p /var/cache/nginx/client_temp
(July) [root@CentOS nginx-1.10.3]# nginx 
# 检查一下
(July) [root@CentOS nginx-1.10.3]# netstat -tlno | grep "80"
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      off (0.00/0/0)
```

### 使用Uwsgi运行Django

安装`Uwsgi`

```bash
(July) [root@CentOS nginx-1.10.3]# cd
(July) [root@CentOS ~]# pip install uwsgi
(July) [root@CentOS ~]# cd July/
# 后台启动Uwsgi
(July) [root@CentOS July]# (July) [root@CentOS July]# uwsgi --http :8000 --module July.wsgi --processes 5 --daemonize uwsgi.log
```

别问我为什么不用配置文件方式启动`uwsgi`，因为`我不会`。

### 访问

打开浏览器，输入地址`172.16.10.3`看看会输出什么。

然后你会看到这个，如图：

![blog](https://github.com/anshengme/July/raw/master/doc/img/home.png)

### 一些信息

因为我们提前导入了些数据库，所以呢，你需要知道后台的admin账号和密码

|账号|密码|
|:--|:--|
|ianshengme@gmail.com|ansheng.me|

## 反馈与建议

- 邮箱：<ianshengme@gmail.com>
- GitHub: https://github.com/anshengme/july/issues
