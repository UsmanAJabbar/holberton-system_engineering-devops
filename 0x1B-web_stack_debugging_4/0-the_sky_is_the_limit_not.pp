# Increases the number of requests nginx could handle
exec { 'fix':
  path    => ['/usr/bin/', '/bin/'],
  command => 'echo ULIMIT=\"-n 4096\" >> /etc/default/nginx',
}
exec { 'restart service':
  provider => 'shell',
  command  => 'sudo service nginx restart',
}
