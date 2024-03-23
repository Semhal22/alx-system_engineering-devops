# Install flask from pip3
exec {'install flask':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin/'],
}

exec {'install werkzeug':
  command => 'pip3 install werkzeug==2.1.1',
  path    => ['/usr/bin']
}