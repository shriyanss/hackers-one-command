# Hacker's One Command ;)
Find some useful commands to automate hacking (1 command to automate everything). If you found it useful, feel free to [star](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars) it!

## Bug bounty
- **Just do some basic recon with some tools** (*#001*)
  - Preparation
    - Create an environment variable name HOST with command `HOST="target.com"`
  - Requirements
    - Amass
    - Httpx
    - Wget
    - Python 3
    - Nmap
    - waybackurls
  - Breakdown
    - Runs amass to find subdomains of domains listed in domains.txt (make sure you create it)
    - Run httpx to get live URLs
    - Create a folder named *`httpselfie`* and screenshot URLs from httpx
    - Go to previous directory and extract hosts from httpx results
    - Run nmap scan on hosts and give its output to *`nmap.txt`*
```
echo $HOST > domains.txt && amass enum -passive -norecursive -noalts -df domains.txt -o subdomains.txt && cat subdomains.txt | httpx -o httpx.txt && waybackurls $HOST > waybackurls.txt && wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/ipResolve.py && python3 ipResolve.py > ip.txt && mkdir httpselfie && cp httpx.txt httpselfie/httpx.txt && cd httpselfie && wget https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/httpselfie.py && python3 httpselfie.py httpx.txt url && cd ../ && wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/replace.py && python3 replace.py > hosts.txt && nmap -v -iL hosts.txt -oN nmap.txt
```
- **Do nikto scanning with basic recon (above)** (*#002*)
  - Preparation
    - Create an environment variable name HOST with command `HOST="target.com"`
    - Create an environment variable name URL with command `URL="https://target.com"`
  - Requirements
    - Amass
    - Httpx
    - Wget
    - Python 3
    - Nmap
    - Nikto
  - Breakdown
    - Runs amass to find subdomains of domains listed in domains.txt (make sure you create it)
    - Run httpx to get live URLs
    - Create a folder named *`httpselfie`* and screenshot URLs from httpx
    - Go to previous directory and extract hosts from httpx results
    - Run nmap scan on hosts and give its output to *`nmap.txt`*
    - Run nikto 
```
echo $HOST > domains.txt && amass enum -passive -norecursive -noalts -df domains.txt -o subdomains.txt && cat subdomains.txt | httpx -o httpx.txt && waybackurls $HOST > waybackurls.txt && wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/ipResolve.py && python3 ipResolve.py > ip.txt && mkdir httpselfie && cp httpx.txt httpselfie/httpx.txt && cd httpselfie && wget https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/httpselfie.py && python3 httpselfie.py httpx.txt url && cd ../ && wget https://raw.githubusercontent.com/shriyanss/hackers-one-command/main/utils/replace.py && python3 replace.py > hosts.txt && nmap -v -iL hosts.txt -oN nmap.txt && nikto -url $URL -ask no -Cgidirs all -o nikto.txt -Tuning 1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,x -timeout 30
```
