# HTTP client and server

## Dowlnoad data from URL

    import urllib.request

    with urllib.request.urlopen("http://www.python.org/") as response:
        print(response.read())

    request = urllib.request.Request('http://www.python.org/')
    request.add_header('Referer', 'http://www.example.net/')
    response = urllib.request.urlopen(request)

## Run HTTP server

  * CGI, FastCGI, WSGI
  * Various frameworks on top of WSGI and other protocols

Example: server.py

play with requests

    import requests
    r = requests.get('https://api.github.com/events')
    data = r.json()
    print(data[0])
