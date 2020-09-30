# Fixes the PHP extension in the wp-settings directory
exec { 'phpextension':
  path    => [ '/bin/', '/usr/bin/' ],
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
}
