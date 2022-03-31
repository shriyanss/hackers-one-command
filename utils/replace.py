with open("httpx.txt", 'r') as file:
    for line in file:
        line = line.replace("\n", '')
        line = line.replace('http://', '')
        line = line.replace('https://', '')
        print(line)
