import subprocess

# Declares variable, asks and scans for user input

ping_ip_Address = input("IP Address to Ping: ")

# Pings the IP address one time

subprocess.run(["ping", "-n", "1", ping_ip_Address])
