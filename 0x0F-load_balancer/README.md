# 0x0F. Load balancer
- HAProxy, which stands for High Availability Proxy, is a popular open source software TCP/HTTP Load Balancer and proxying solution which can be run on Linux, macOS, and FreeBSD. Its most common use is to improve the performance and reliability of a server environment by distributing the workload across multiple servers (e.g. web, application, database).
0. Double the number of webservers
    * Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
    * The name of the custom HTTP header must be X-Served-By. The value of the custom HTTP header must be the hostname of the server Nginx is running on
1. Install your load balancer
    * Configure HAproxy on lb-01 server, so that it send traffic to web-01 and web-02
    * Distribute requests using a roundrobin algorithm
