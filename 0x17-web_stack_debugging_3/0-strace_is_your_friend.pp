# Corrects the error on a apache web server

exec { 'debug_php_file':
  path     =>  ['/usr/bin', '/bin'],
  provider =>  shell,
  command  =>  "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
