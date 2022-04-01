with open("subdomains.txt", 'r') as file:
	for line in file:
		line = line.replace("\n", '')
		try:
			ip = socket.gethostbyname(line)
			print(f"{line}: {ip}")
		except:
			pass
