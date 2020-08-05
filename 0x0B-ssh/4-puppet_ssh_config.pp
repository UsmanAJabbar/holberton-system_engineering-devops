# Disables Password Authentication and Adds Auth Key
include stdlib
file_line {'Disable Password Auth':
	ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
file_line {'Update Identity Key':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/holberton',
}
