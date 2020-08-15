# This configures a custom NGINX server with
# basic files based off the tasks from 0 and 1
package { 'nginx':
    ensure   => 'installed',
    provider => 'apt'
}
package { 'index.html':
    ensure   => file,
    path	 => '/var/www/html/index.html',
    content  => 'Holberton School'
}
exec { 'Beep Beep Coming through':
    command  => "sed -i '41a \\tadd_header X-Served-By $hostname;' /etc/nginx/sites-available/default"
}
service { 'nginx':
	ensure   => running
}
