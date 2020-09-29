# Fixes the PHP extension in the wp-settings directory
exec { 'phpextension':
   provider => 'shell',
   command =>  'wget https://raw.githubusercontent.com/UsmanGTA/holberton-system_engineering-devops/master/0x17-web_stack_debugging_3/wp_fixer.sh && chmod u+x wp_fixer.sh && sudo ./wp_fixer.sh',
}
