# Increases the number of files holberton as a user could handle
exec { 'fix_hardlimit':
	path    => ['/usr/bin/', '/bin/'],
	command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000" /etc/security/limits.conf',
}
exec { 'fix_softlimit':
	path    => ['/usr/bin/', '/bin/'],
	command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000" /etc/security/limits.conf',
}
