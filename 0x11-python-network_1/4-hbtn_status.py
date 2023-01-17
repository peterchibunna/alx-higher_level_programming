#!/usr/bin/python3
"""Description"""
if __name__ == "__main__":
    import requests

    data = requests.get('https://intranet.hbtn.io/status').content
    print('Body response:')
    print('    - type: {}'.format(type(data.decode('utf-8'))))
    print('    - content: {}'.format(data.decode('utf-8')))
