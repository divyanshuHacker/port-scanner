import socket

def scan_port(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"Port {target_port}: Open")
        else:
            print(f"Port {target_port}: Closed")
        sock.close()
    except socket.error:
        print("Couldn't connect to server.")

def main():
    target_host = input("Enter the host to scan: ")
    target_ports = input("Enter the ports to scan (space-separated): ").split()
    for port in target_ports:
        scan_port(target_host, int(port))

if __name__ == "__main__":
    main()
