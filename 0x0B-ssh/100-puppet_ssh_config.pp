# This script makes changes to our config files

exec {'echo':
  path    => '/usr/bin:/bin'
  command => 'echo "\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no" >> /etc/ssh/ssh_config'
  return  =>  [0, 1]
}
