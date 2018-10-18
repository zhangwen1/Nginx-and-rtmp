# Nginx-and-rtmp
Nginx
打开浏览器访问此机器的 IP，如果浏览器出现 Welcome to nginx! 则表示 Nginx 已经安装并运行成功


cd nginx-1.8.1
./configure --add-module=../nginx-rtmp-module
make
sudo make install
