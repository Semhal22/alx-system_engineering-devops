# SSH client configuration must use private key and no password authentication
file {'/etc/ssh/ssh_config':
    ensure  => 'file',
    content => "Identityfile ~/.ssh/school\nIdentitiesOnly yes\nPasswordAuthentication no",
}
