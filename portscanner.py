
import socket
import termcolor

def scan(target,ports):
	for port in range(1, ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(termcolor.colored("[+] Port Opened: " + str(port), 'green'))	
		sock.close()	
	except:
		pass

targets = input("[*] Enter target to scan: ")
ports = int(input("[*] Enter how many ports to scan: "))
if ',' in targets:
	print("[*] Scanning multiple targets. . .")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)

else:
	scan(targets,ports)
