import subprocess

# Declares variable, asks and scans for user input

ping_ip_Address = input("IP Address to Ping: ")

# Pings the IP address 30 times

subprocess.run(["ping", "-n", "30", ping_ip_Address])
