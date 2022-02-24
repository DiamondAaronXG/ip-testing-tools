import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Enter a ip to scan: ")

def pscan(port):
	try:
		con = s.connect((target,port))
		return True
	except:
		return False

for x in range(25):
	if pscan(x):
		print(f"port {x} is open")
