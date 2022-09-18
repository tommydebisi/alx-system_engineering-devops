# This script makes changes to our config files

exec {'echo':
  command => '/usr/bin/echo "\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
