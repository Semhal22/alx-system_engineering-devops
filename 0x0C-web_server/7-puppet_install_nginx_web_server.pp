# Configure server with Puppet
package { 'nginx':
  ensure => 'installed';
}

# Nginx server configuration

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;

	location / {
	    return 200 'Hello World!';
	}
        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }

  ",
}

# symbolic link to enable the config

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}
# removing the default nginx default config symlink
file { '/etc/nginx/sites-enabled/000-default':
  ensure => 'absent',
  notify => Service['nginx'],
}
# starting and enabling the Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
