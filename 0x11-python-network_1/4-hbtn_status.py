#!/usr/bin/python3
"""Description"""
if __name__ == "__main__":
    import requests

    data = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:')
    print('    - type: {}'.format(type(data)))
    print('    - content: {}'.format(data))
