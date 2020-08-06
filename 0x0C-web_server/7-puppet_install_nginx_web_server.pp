# Sets up a server based off of the tasks completed in tasks 1-4
# with a single puppet file
# REQUIREMENTS
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request 
# (requesting a page) using curl, it must return a page that
# contains the string Holberton School
# The redirection must be a "301 Moved Permanently"
include stdlib
package { 'nginx':
    ensure   => 'installed',
    provider => 'apt',
}

file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'Holberton School',
}

file_line { '/etc/nginx/sites-available/default':
    ensure   => 'present',
    multiple => 'true',
    after    => 'server_name _;',
    line     => 'rewrite ^/redirect_me https://usmanjabbar.com permanent;',
}

service { 'nginx':
    ensure => running,
}
