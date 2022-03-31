# Hacker's One Command ;)
Find some useful commands to automate hacking (1 command to automate everything). If you found it useful, feel free to [star](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars) it!

## Bug bounty
- **Command 1**
  - Requirements
    - Amass
    - Httpx
    - Wget
    - Python 3
    - Nmap
  - Breakdown
    - Runs amass to find subdomains of domains listed in domains.txt (make sure you create it)
    - Run httpx to get live URLs
    - Create a folder named *`httpselfie`* and screenshot URLs from httpx
    - Go to previous directory and extract hosts from httpx results
    - Run nmap scan on hosts and give its output to *`nmap.txt`*
```
amass enum -passive -norecursive -noalts -df domains.txt -o subdomains.txt && cat subdomains.txt | httpx -o httpx.txt && mkdir httpselfie && cp httpx.txt httpselfie/httpx.txt && cd httpselfie && wget https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/httpselfie.py && python3 httpselfie.py httpx.txt url && cd ../ && wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/replace.py && python3 replace.py > hosts.txt && nmap -v -iL hosts.txt -oN nmap.txt 
```
