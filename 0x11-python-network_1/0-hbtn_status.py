#!/usr/bin/python3
""" Description"""

if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as connection:
        data = connection.read()
        print('Body response:')
        print('    - type: {}'.format(type(data)))
        print('    - content: {}'.format(data))
        print('    - utf8 content: {}'.format(data.decode('utf-8', 'replace')))
