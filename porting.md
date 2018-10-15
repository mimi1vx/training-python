# Python 2.x to 3.x porting

Resources:

  * https://docs.python.org/3.0/whatsnew/3.0.html
  * http://python3porting.com/
  * https://portingguide.readthedocs.io/en/latest/
  * https://six.readthedocs.io/

## Experience Check

  * Operating system usage
  * Python coding knowledge
  * Python version knowledge
  * Git source control knowledge
  * Unit testing knowledge

## Introduction

### Python versions

  * Minimum versions: Python 3.3/3.5 / Python 2.6/2.7

    import sys
    sys.version_info
    sys.version_info.major

### Unit testing considerations

  * Unit test framework (e.g. pytest)
  * Test both Python 2.x and Python 3.x as supported by your code

### Moving to modern Python

  * Modernizing code to avoid obsolete 2.x syntax and patterns
      - Upgrade syntax to a subset of 2.7 and 3.3
      - Avoid any 3.x features not backported to 2.7 (e.g. `super()`)
      - Avoid any post 3.3 features (e.g. `async`)
  * Porting code to actually run in 3.x using various techniques
      - Use dynamic features of Python
      - Monkey-patch module scope and libraries if needed
      - Make use of `ImportError`, `NameError` and similar
      - Instead use `six` where possible
  * Dropping 2.x support
      - Drop legacy burden as soon as possible
  * Using latest 3.x features
      - Once the legacy burden is gone
      - Python goes modern!

### Source control considerations

  * Use separate commits for automated changes
  * Separate logical manual changes

## Tools

### 2to3

One way convertor and fixer from 2.x to 3.x code. A rather bizzare idea of
modifying the source code at build time.

### six compatibility library

  * Types and support features
      - `six.text_type`
      - `six.binary_type`
  * Moves and renames
      - How to import varying stuff manually?
      - `six.moves`
      - `six.add_move()`

### modernize

    pip install --user modernize

    python-modernize .

    # Git way, rewrite files, no backups
    python-modernize -wn .
    git diff

### futurize

    # (openSUSE)
    zypper in python3-futurize

    futurize .

    # Git way
    futurize -wn .
    git diff

## Language and library differences

### Minor syntax differences

  * Mixed tabs and spaces no longer allowed in 3.x
      - `testindent.py`
  * Tuple unpacking in function argument list not in 3.x
      - `testtupleargs.py`
  * Backticks no longer in 3.x
      - `backticks.py`
  * Alternative not-equal (`<>`)
      - `notequal.py`
  * `None`, `True`, `False` keywords in 3.x
      - Therefore not assignable.
      - Also optimized so that people don't optimize c-style using `while 1:`.
      - Also try `import keyword; keyword.kwlist`

### Exceptions

Syntax changes:

  * Only 2.6 syntax of `except` supported in 3.x
      - Bad: `except Exception, error:`
      - Bad: `except (KeyError, IndexError):`
      - Bad: `except KeyError, IndexError:` (hard to spot mistake)
      - Good: `except Exception as error:`
      - Good: `except (KeyError, IndexError) as error:`
      - See `py3exception.py`
  * Only 2.6 syntax of `raise` supported in 3.x
      - Bad: `raise Exception, "Test!"`
      - Good: `raise Exception("Test!")`
      - Special: `import six; six.reraise(Exception, 'Test!',  traceback)`
  * The target cleared at the end of the except block
      - When using `except Exception as target:`
  * Exceptions no longer iterable in 3.x like in 2.6
      - Bad: `except RuntimeError as (num, message):`
  * Only `BaseException` objects allowed in 3.x
      - No `raise` and `except` support for other objects.

Library changes:

  * `StandardError` removed, use `Exception`
  * `sys.exc_*` removed, use `sys.exc_info()`

### Importing modules

  * Absolute imports
      - Module name/path not prefixed with a dot
      - Modules inside packages no longer search in relative directory
      - When submodules import other submodules, they need to start with
        the top package name
  * Relative imports
      - Prefixed by one or more dots
      - Only applicable to modules inside packages
      - Explicit relative imports required
  * Star imports
      - Only available on module level in 3.x
      - No longer work in function
      - Python 2.x supports it but had to disable local variable
        optimization
  * Circular imports may fail occasionally
      - Bad: `badimport/*.py`

### Library reorganization

  * For most common renames just see `six.moves` documentation
      - Otherwise you need to refer to the versioned library docs directly.
  * Some string operations removed from `string` module
      - Use `str` methods.

### Numeric types

  * Growing integers
      - Single integer type in 3.x
      - Growing `int` into `long` in 2.x
      - Distinction moved into internal implementation
      - Optional `L` suffix no longer allowed in 3.x
      - Representation changed accordingly
  * Octal literals changed
      - Good: `0o777`
      - Bad: `0777`
      - Leading zeroes not allowed
      - Semantics of `int(..., base=0)` changed accordingly.
  * Division semantics changed
      - `from __future__ import division`
      - `__div__` implements `/` in 3.x
      - `__truediv__` implements `/` in 3.x (2.x with future import)
      - `__floordiv__` implements `//`
      - Fix: `__truediv__ = `__div__`
  * Rounding semantics changed

### Input and output

  * Convenient `print()` function
      - `from __future__ import print_function`
      - The complicated `print` keyword removed
      - Instead a `print()` function introduced with a pretty simple
        implementation
  * Safe `input()` function
      - `input()` in 2.x is `eval(input())` in 3.x
      - Use `int(input)`, `float(input)` and similar
      - One of the worst features of Python 2.x!
  * The `file` built-in is gone
      - Types of file objects vary anyway (e.g. 2.x open vs io.open)

### String types

  * `from __future__ import unicode_literals`
  * `unicode` in 2.x, `str` in 3.x
  * `str` in 2.x, `bytes` in 3.x
  * `six.text_type`, `six.binary_type`
  * The native string type
      - `str == six.text_type` in 3.x
      - `str == six.binary_type` in 2.x
      - Future imports cannot change that!
  * Literals
      - `u'asdf'` required in 2.x, noop in 3.x (or with future import)
      - `b'asdf'` required in 3.x (or with future import), noop in 2.x
      - `'asdf'` native string type (unless future import)
  * Text `.encode()` and binary string `.decode()` methods.
  * The strange `str.encode()` in 2.x
      - Decodes as ASCII before encoding
  * Other automatic recoding cases
      - `str(my_unicode_string)`
      - ASCII codec
      - The single worst feature of Python 2.x leading to programs crashed
        the first time they see non-ascii!
  * Text and bytes can't be mixed in 3.x
      - Bad: `b':'.join(['one', 'two'])`
      - `basestring` abandoned in 3.x
  * Text and binary modes of `open()` in 3.x
      - `encoding` argument also available
      - `from io import open` to replace 2.x open with 3.x
  * Issues with libraries

### Data manipulation

  * Move slightly towards functional programming
  * `map()` and `filter()` return iterators in 3.x
      - List/generator comprehensions recommended instead
  * `zip()` returns an iterator in 3.x
      - Use `list(zip(...))` when necessary
  * `next()` since 2.6
      - Uses `.__next__()` in 3.x
      - Uses `.next()` in 2.x
      - Compat: `next = __next__` in class definition
  * `apply()` is gone
      - Use asterisk notation for function calls instead
  * `reduce()` moved to `functools`
  * `exec()` function introduced
      - Replaces `exec` statements in 2.x
  * `reload()` moved to `importlib`
  * `intern()` moved to sys
      - String literals apparently get interned automatically
  * `coerce()` removed
      - Not needed

#### Comparison and sorting

  * Numbers and strings are not mutually comparable in 3.x
  * Lists of mixed numbers and strings are not sortable
  * No more `.__cmp__()` special method
      - All comparisons should be implemented.
      - You can use `functools.total_ordering()`.
      - For sorting `__lt__()` is good enough.
  * No more `cmp` argument in sorting functions
      - Everything can be handled using `key` functions.
      - Even comparison based sorts can be handled using proxy comparable
        key objects.
      - See `functools.cmp_to_key()` as an example.

#### Dictionary API

  * Key existence
      - `.has_key()` removed, use `in`
  * Lists vs iterators vs views
      - `dict.keys()`
      - `dict.values()`
      - `dict.items()`
  * Indexing not available with views
      - Use `list(d.items())` to convert to indexable list
  * Iterating over dictionaries
      - Just use `d.items()` if 2.x performance is not a concern
      - Use `six.iteritems()` or `six.viewitems()` if it is
  * Modify dictionary while iterating
      - `for keys in list(d.keys()):`
  * Key ordering
      - Order not significant
      - Stable item ordering since 3.6, insert order maintained
  * Dictionary versioning for optimization
      - Guards for namespaces

### Object model

  * Old style classes not supported in 3.x
      - `class X:` in 2.x
      - For 2.x compatibility use `class X(object):`
      - For 3.x `class X:` defines a new style class
  * Old style class caveats
      - Should not be used after 2.1
      - Doesn't have many Python class features, especially those related
        to inheritance (e.g. `__mro__` semantics)
  * Metaclass syntax differs
      - Good: `class Foo(Parent, metaclass=Meta):`
      - Bad: `__metaclass__ = Meta`
      - Magic: `class Foo(six.with_metaclass(Meta, Parent)):`
  * `__oct__` and `__hex__` removed
      - Use `__index__ = __int__` to indicate that integer representation
        is suitable for indexing and conversion to oct/hex.
  * Slicing now implemented using indexing by slice objects.
  * `__nonzero__` renamed to `__bool__`
      - Use `__bool__ = __nonzero__`
  * Unbound method objects are gone
      - Function is returned directly
  * Buffer API replaced with memoryview API


### Comprehensions

  * List iteration variable no longer leaked in 3.x
  * Comprehention over tuples is now explicit
      - Good: `[i for i in (1, 2, 3)]`
      - Bad: `[i for i in 1, 2, 3]`

### Functions

  * Renamed function special methods
      - From `func_` prefixed to dunder attribute names

### Miscellaneous changes

  * Python compiled files location
