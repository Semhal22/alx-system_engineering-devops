# 0x0C. Web server
- A web server is a software or hardware device that accepts and responds to requests from clients over the internet or a network. A web server typically hosts web pages, images, videos, or other web resources that can be accessed by web browsers or other applications.
- This project includes tasks to configure an Ubuntu machine with some requirements
0. Transfer a file to your server
    * Transfers a file from our client to a server
1. Install nginx web server
    * Nginx should be listening on port 80
    * When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
2. Setup a domain name
3. Redirection
    * Configure nginx so that /redirect_me is redirecting to another page
    * The redirection must be a “301 Moved Permanently”
