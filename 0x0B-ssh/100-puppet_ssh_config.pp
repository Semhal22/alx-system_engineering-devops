# Configure file so that it can connect to a server without password
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => 'IdentityFile ~/.ssh/school\nPasswordAuthentication no',
}
