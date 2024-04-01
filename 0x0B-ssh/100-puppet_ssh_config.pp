# SSH client configuration must use private key and no password authentication
file_line {'Turn off passwd auth':
    ensure => 'created',
    path   => '/etc/ssh/ssh_config'
    line   => 'Password Authentication no',
}
file_line {'Declare identity file':
    ensure => 'created',
    path   => '/etc/ssh/ssh_config'
    line   => 'IdentityFile ~/.ssh/school'
}
