# Scripts

V1.0

#1 This script takes a host and a range of ports to scan as input, and returns a list of open ports.
It's important to note that some ports and hosts might be filtered or firewalled, and the script won't be able to tell the difference between a closed and filtered port.

Script uses multiple threads to simultaneously scan a range of ports. The number of threads can be adjusted by changing the value of thread_count variable.
Each thread is responsible for scanning a range of ports and the progress is calculated by keeping track of the number of ports scanned by each thread.
It also uses a timeout of 0.1s when creating a socket to speed up the scan.

To scan a IP range use(192.168.1.xx-192.168.1.xx) port.

