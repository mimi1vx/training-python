# Serialization and persistence

## Serialization

Useful for storing data or sending them over the network.

### JSON, YAML

  * dumps, dump
  * loads, load

    json.dumps({"asdf": 'zxxvc'})

    with open("example.json", "w") as stream:
        json.dump({"asdf": 'zxxvc'}, stream)

Online: http://echo.jsontest.com/key/value/one/two

### XML

    >>> from lxml import etree
    >>> p = etree.Element("p")
    >>> p.text = "Hello"
    >>> etree.tostring(p)
    b'<p>Hello</p>'

Example: writexml.py

### pickle

## Database access

### shelve

Simple pythonic dictionary-like store: shelve

Example: db.py

### SQL

Example: sql.py
