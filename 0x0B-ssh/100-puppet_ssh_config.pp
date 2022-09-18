# This script makes changes to our config files

exec { 'echo':
  command => '/usr/bin/echo "\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no" >> /etc/ssh/ssh_config',
}
