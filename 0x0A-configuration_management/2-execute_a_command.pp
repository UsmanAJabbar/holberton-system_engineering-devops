# Kills a given process called killmenow
# pkill is located in 'usr/bin'
exec { 'killmenow':
    path    => '/usr/bin/',
    command => 'pkill -f ./killmenow',
}
