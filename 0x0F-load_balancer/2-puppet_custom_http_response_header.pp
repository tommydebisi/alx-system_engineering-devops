# Installs a Nginx server

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo echo "Hello World!" > /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By $(hostname);\n\trewrite ^\/redirect_me https:\/\/github.com\/tommydebisi permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
