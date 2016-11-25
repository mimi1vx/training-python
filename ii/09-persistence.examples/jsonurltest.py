with urlopen("http://echo.jsontest.com/key/value/one/two") as stream:
    a = json.loads(stream.read().decode("ascii"))
