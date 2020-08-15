# This configures a custom NGINX server with
# basic files based off the tasks from 0 and 1
package { 'nginx':
    ensure   => 'installed',
    provider => 'apt'
}
package { 'index.html':
    ensure  => file,
    path    => '/var/www/html/index.html',
    content => 'Holberton School'
}
exec { 'Beep Beep Coming through':
    command  => "sed -i '/^\tserver_name.*/a \\tadd_header X-Served-By $hostname;' /etc/nginx/sites-available/default"
}
exec { 'Restart NGINX':
  command => 'sudo service nginx restart'
}
service { 'nginx':
  ensure   => running
}
