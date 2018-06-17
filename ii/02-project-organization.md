# Project organization

## Project

  * Represented as a directory
  * Contents
      - Package and modules
      - Scripts
      - Installation information `setup.py`
      - `README` file

## Package

  * Directory that contains a python library
  * Contents
      - Package module code: `__init__.py`
      - Optional package script code

## Module

  * Python code file with `.py` extension

## Importing

  * `sys.path`
  * Absolute imports, relative imports

## Script

  * Executable python script
      - Usually without extention on unix, with `.py` extension on windows

  * Contents
      - Shebang on unix
      - Optional encoding (python 2.x or non-utf-8 python 3.x script)
      - Optional `__future__` imports
      - Imported modules/packages
      - Code, usually very simple

## Installation information

  * Installation script `setup.py` using distutils

<!-- end of list -->

    $ python setup.py --name
    $ python setup.py --version
    $ python setup.py --author

    $ python setup.py sdist
    $ ls -l dist
    $ tar -tf dist/Project-1.0.tar.gz
