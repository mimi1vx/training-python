from nose.tools import assert_equal

from f import func

def test_func():
    assert_equal(func(), 4)
