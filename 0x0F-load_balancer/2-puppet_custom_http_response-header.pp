# This configures a custom NGINX server with
# basic files based off the tasks from 0 and 1
package {'haproxy':
    ensure  => installed,
    version => '1.8',
}
exec {'wget':
    provider => 'shell',
    command  => 'wget https://raw.githubusercontent.com/UsmanGTA/holberton-system_engineering-devops/master/0x0F-load_balancer/1-install_load_balancer && chmod +x 1-install_load_balancer && sudo ./1-install_load_balancer',
}