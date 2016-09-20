# Python 2.x and 3.x differences

## Python 2.7 compatibility

  * Python 2.7 can already make use of most 3.x features
  * The six library to overcome some of the differences
  * 2to3 script to turn Python 2.x code into Python 3.x code
  * Modernize and futurize tools to improve 2.x code compatibility

## Integer division

  * Python 2.x: `from __future__ import division`
  * Behavior of `/`, `//` and `%` operators

## Print statement or function

  * Python 2.x: `from __future__ import print_function`

## Unicode string literals

  * Python 2.x: `from __future__ import unicode_literals`
  * Binary data strings: `b"ascii"`

## Differences in libraries

  * Renames, reorganization
      - `from six.moves import python2_module_name`
      - See: https://pythonhosted.org/six/
  * Dynamic nature of Python allows a lot of magic to be performed
