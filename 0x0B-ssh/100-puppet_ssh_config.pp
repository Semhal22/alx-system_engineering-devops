# Configure file so that it can connect to a server without password
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => 'IdentityFile ~/.ssh/school  PasswordAuthentication no',
}
