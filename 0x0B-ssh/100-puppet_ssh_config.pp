# SSH client configuration must use private key and no password authentication
file {'/home/ubuntu/.ssh/config':
    ensure  => 'file',
    content => 'Identityfile ~/.ssh/school\nPasswordAuthentication no',
}
