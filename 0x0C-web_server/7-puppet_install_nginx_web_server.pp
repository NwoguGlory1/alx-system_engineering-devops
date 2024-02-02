# Automating multiple configuratn with puppet manifest
# Command to install nginx
package { 'nginx':
  ensure => installed,
}

fine_line { 'install':
  ensure => 'present',
  path   => 'etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 301;',
}

# To save file in 
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensure service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
