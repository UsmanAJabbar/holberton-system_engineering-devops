# Increases the number of requests nginx could handle
exec { 'fix':
	path    => ['/usr/bin/', '/bin/'],
	command => 'echo ULIMIT="-n 4096" >> /etc/default/nginx',
}
service { 'nginx':
	ensure    => running,
	enable    => true,
	subscribe => Exec['fix'],
}
