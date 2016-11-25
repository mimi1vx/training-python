# Classes, methods, attributes

  * Class syntax

## Record-style class

    class Employee:
        pass

    john = Employee()
    john.name = 'John Doe'
    john.location = 'Prague'
    john.language = 'English'

Examples: employee.py, employee2.py

## Class initialization and destruction

  * `__init__()`, `__str__()`, `__repr__()`

Example: cls.py

## Context manager (with statement)

Example: context.py

## Attribute access

  * `__class__`, type()
  * `__dict__`, vars()
  * `getattr()`, `setattr()`, `delattr()`
  * `.__getattr__()`, `__setattr__()`, `__delattr__()`

Example: attr.py

## Properties

Example: prop.py

item.py TODO why doesn't work

## Standard method decorators

  * @classmethod, @staticmethod

## Other

https://docs.python.org/3/reference/datamodel.html#special-method-names

## Case study: Roman numerals

  * Python 2.x compatibility
  * Regular expressions
      - Compiled regex objects
  * Initialization
      - By an object of different types
  * Conversion to integer
  * String conversion and representation
  * Addition

## Inheritance

Example: shape.py
