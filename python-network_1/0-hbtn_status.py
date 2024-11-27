#!/usr/bin/python3
import urllib.request

# URL to fetch
url = "https://alu-intranet.hbtn.io/status"

# Open the URL and fetch the content
with urllib.request.urlopen(url) as response:
    body = response.read()  # Read the body of the response
    print("\t" + body.decode("utf-8"))  # Decode the body to UTF-8 and print with a tabulation

