#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    server = 'http://0.0.0.0:5000/search_user'
    try:
        search = sys.argv[1]
    except IndexError:
        search = ''

    post = {'q': search}
    req = requests.post(server, data=post)
    response = req.json()
    if response:
        if response.get('id', None) is not None:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
        else:
            print("Not a valid JSON")
    else:
        print('No result')
