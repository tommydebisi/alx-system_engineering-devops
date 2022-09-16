# This script creates a file in `tmp`

# ensure set to file makes sure it's a normal file
file {'/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
