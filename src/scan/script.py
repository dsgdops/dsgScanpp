import nmap

def run_scan(host):
    nm = nmap.PortScanner()
    nm.scan(host, '22-443')
    port = nm[host]['tcp']
    return port

print(run_scan("192.168.0.1"))