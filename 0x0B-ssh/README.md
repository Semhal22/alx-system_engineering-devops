# 0x0B. SSH
### The most common way of connecting to a remote Linux server is through SSH. SSH stands for Secure Shell and provides a safe and secure way of executing commands, making changes, and configuring services remotely.
0. Use a private key
	* Bash script that uses ssh to connect to 281593-web-01
	* Uses private key with user ubuntu
1. Create an SSH key pair
	* Name of the private key must be school
	* Number of bits in the created key to be created 4096
	* Passphrase should be betty
2. Client configuration file
	* Configure SSH configuration file so as to connect to a server without typing a password
	* Refuse authentication using a password
4. Client configuration file (w/ Puppet)
	* Using puppet to perform the above task
