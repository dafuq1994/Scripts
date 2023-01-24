import socket
from threading import Thread

def scan_ports(host, start, end, open_ports):
    for port in range(start, end):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)

def scan_host(host, start_port, end_port):
    open_ports = []
    total_ports = end_port - start_port
    ports_scanned = 0
    thread_count = 100
    thread_list = []
    for i in range(thread_count):
        start = start_port + i * (total_ports // thread_count)
        end = start_port + (i + 1) * (total_ports // thread_count)
        t = Thread(target=scan_ports, args=(host, start, end, open_ports))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
        ports_scanned += end - start
        percentage = (ports_scanned / total_ports) * 100
        print(f"Scan progress: {percentage:.2f}%", end='\r')
    return open_ports

host_input = input("Enter the host to scan (IP/hostname or IP range): ")

if '-' in host_input:
    host_range = host_input.split("-")
    start_host = host_range[0]
    end_host = host_range[1]
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    for host_ip in range(int(start_host.split('.')[-1]), int(end_host.split('.')[-1])+1):
        host = '.'.join(start_host.split('.')[:-1]) + '.' + str(host_ip)
        open_ports = scan_host(host, start_port, end_port)
        print(f"Open ports on {host}: {open_ports}")
else:
    host = host_input
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    open_ports = scan_host(host, start_port, end_port)
    print(f"Open ports on {host}: {open_ports}")
