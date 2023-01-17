#!/usr/bin/python3
"""Description"""
import requests

if __name__ == "__main__":
    d = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(d.text)))
    print("\t- content: {}".format(d.text))
