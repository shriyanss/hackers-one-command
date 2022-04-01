with open("hosts.txt", 'r') as file:
  for line in file:
    line = line.replace("\n", '')
    ip = socket.gethostbyname(line)
    print(ip + ": " + line)
