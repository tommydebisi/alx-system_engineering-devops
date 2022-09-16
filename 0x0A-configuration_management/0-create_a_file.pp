# This script creates a file in `tmp`

file {'/tmp/school':
  ensure  => link,
  target  => '/tmp/school'
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
