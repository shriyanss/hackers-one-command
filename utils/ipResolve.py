with open("subdomains.txt", 'r') as file:
  for line in file:
    try:
      line = line.replace("\n", '')
      ip = socket.gethostbyname(line)
      print(line + ": " + ip)
     except:
       pass
