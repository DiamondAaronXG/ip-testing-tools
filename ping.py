import subprocess
ping_ip_Address = input("IP Address to Ping: ")
subprocess.run(["ping", "-n", "1", ping_ip_Address])