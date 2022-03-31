# Hacker's One Command

## Bug bounty
- Command 1
  - Requirements
    - Amass
    - Httpx
    - Wget
    - Python 3
```
amass enum -passive -norecursive -noalts -df domains.txt -o subdomains.txt && cat subdomains.txt | httpx -o httpx.txt && mkdir httpselfie && cp httpx.txt httpselfie/httpx.txt && cd httpselfie && wget https://raw.githubusercontent.com/shriyanss/HTTPSelfie/main/httpselfie.py && python3 httpselfie.py httpx.txt url
```
