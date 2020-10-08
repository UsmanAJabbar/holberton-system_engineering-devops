# Increases the number of files holberton as a user could handle
exec { 'fix_hardlimit':
	path    => ['/usr/bin/', '/bin/'],
	command => 'sed -i "/holberton hard nofile 5/aholberton hard nofile 5000" /etc/security/limits.conf',
}
exec { 'fix_softlimit':
	path    => ['/usr/bin/', '/bin/'],
	command => 'sed -i "/holberton soft nofile 4/aholberton soft nofile 4000" /etc/security/limits.conf',
}
