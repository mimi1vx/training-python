# Serialization and persistence

## Serialization

Useful for storing data or sending them over the network.

### JSON

  * dumps, dump
  * loads, load

    json.dumps({"asdf": 'zxxvc'})

    with open("example.json", "w") as stream:
        json.dump({"asdf": 'zxxvc'}, stream)

### XML

### pickle

## Database access

### shelve

Simple pythonic dictionary-like store: shelve

Example: db.py

### SQL

Example: sql.py
