import socket

# Creates a socket object

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Decalares variable, asks and scans for user input

target = input("Enter a ip to scan: ")

# This functuon attempts to connect to a given port on the IP address

def pscan(port):
	try:
		con = s.connect((target,port))
		return True
	except:
		return False

# Loops through ports 0-24

for x in range(25):

	# Checks if each port is open
	
	if pscan(x):

		# Prints the result is a port is open
		
		print(f"port {x} is open")
