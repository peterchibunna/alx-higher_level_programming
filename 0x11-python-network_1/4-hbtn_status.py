#!/usr/bin/python3
"""Description"""
if __name__ == "__main__":
    import requests

    data = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(data.text)))
    print('\t- content: {}'.format(data.text))
