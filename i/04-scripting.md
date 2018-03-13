## Modules and scripting

### Modules

  * File with `.py` suffix
  * Import using interactive interpreter; sys.path
  * Relative module import (from another module)
  * Module can be a script at the same time

Example: module.py

### Script

  * UNIX: Executable file with shebang, not necessarily with `.py` suffix
      - Shebang for python, python2 or python3
  * Windows: Just as any other module
  * Character encoding specification (needed for Python 3.x)

Example: script.py

### Split script code

  * Detect script role by `__name__`
  * Split between two parts
      - Module part
      - Main code doing the script work

### Package

  * Directory structure
  * `__init__.py`
  * `__main__.py`

Example: package

### Automatic compilation

  * Examine directory structre after importing modules
