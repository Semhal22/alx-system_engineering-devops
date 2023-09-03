# Configure file so that it can connect to a server without password
file_line { 'Declare Identity File':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}
file_line { 'Refuse Password':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}
