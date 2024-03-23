# 0x0A. Configuration management
### Server configuration management helps ensure that all the servers are in a desired state, which means that they have the right software installed, the right settings applied, the right data stored, and so on. It also helps avoid problems like server downtime, security breaches, performance issues, and so on. Puppet is one of the tools that can help with server configuration management.
- Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

```
- Install puppet-lint
$ gem install puppet-lint`
```
0. Create a file in /tmp
	* File path is /tmp/school
	* File permission is 0744
	* File owner is www-data
	* File group is www-data
	* File contains I love Puppet

1. Install a package
	* Install flask
	* Version must be 2.1.0

2. Execute a command
	* Create a manifest that kills a process named killme now
	* Must use the exec Puppet resource
	* Must use pkill
