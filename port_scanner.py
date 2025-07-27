import socket
import time

# ANSI colors for terminal
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def scan(target, start_port, end_port):
    open_ports = []
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN}[OPEN]{RESET} Port {port} is open")
            open_ports.append(port)
        s.close()

    duration = time.time() - start_time
    print(f"\nScan completed in {duration:.2f} seconds.")
    return open_ports

print("=== Advanced Port Scanner ===")

target = input("Enter target IP or domain: ")

try:
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        raise ValueError("Invalid port range.")
except ValueError:
    print(f"{RED}Invalid input!{RESET} Please enter valid numbers.")
    exit(1)

open_ports = scan(target, start_port, end_port)

# Save results to file
if open_ports:
    with open("scan_results.txt", "w") as f:
        f.write(f"Open ports on {target}:\n")
        for p in open_ports:
            f.write(f"{p}\n")
    print(f"\nResults saved to scan_results.txt")
else:
    print(f"{RED}No open ports found.{RESET}")