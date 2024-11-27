#!/usr/bin/python3
"""Fetches url"""
import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as req:
        body = req.read()
        # Display response body
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body.decode("utf-8")))
