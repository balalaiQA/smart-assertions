[![Build Status](https://api.travis-ci.org/balalaiQA/smart-assertions.svg?branch=master)](https://travis-ci.com/github/balalaiQA/smart-assertions)
[![PyPI version](https://badge.fury.io/py/smart-assertions.svg)](https://badge.fury.io/py/smart-assertions)
# smart-assertions
Soft assertions for Python

## Installation

```bash
    pip install smart-assertions
```
## Usage

Assertion is performed immediately after the call `soft_assert()`, 
but the expected result is obtained only after the call `verify_expectations()`

Quick example:
```python
    from  smart_assertions import soft_assert, verify_expectations

    def test_something():
        soft_assert(1 == 1)
        soft_assert(2 > 1, 'Message if test failed')
        soft_assert('one' != 'two', 'Some message')
        verify_expectations()
```

You can use asserts in loop:
```python
    from  smart_assertions import soft_assert, verify_expectations
    
    def test_asserts_in_loop():
        for number in range(1, 10):
            soft_assert(number % 2 == 0, '{} is not a multiple of 2'.format(number))
        verify_expectations()
```

Also you can use it with pytest parametrized tests:
```python
    import pytest
    from  smart_assertions import soft_assert, verify_expectations

    @pytest.mark.parametrize("number", list(range(1, 10)))
    def test_pytest_example(number):
        soft_assert(number % 2 == 0)
        verify_expectations()
```

Example of output:
```python
    AssertionError: Failed conditions count: [ 4 ]
    
    1. Exception: Custom message if test failed
    Fail in "/Users/nromanov/Documents/smart-assertions/unittest_example.py:28" test_mixed()
    
    2. Exception: Lists not equals
    Fail in "/Users/nromanov/Documents/smart-assertions/unittest_example.py:30" test_mixed()
    
    3. Exception: Your custom message; 4 < 5!
    Fail in "/Users/nromanov/Documents/smart-assertions/unittest_example.py:32" test_mixed()
    
    4. Exception: one != two
    Fail in "/Users/nromanov/Documents/smart-assertions/unittest_example.py:34" test_mixed()
```

More examples you can find in `unittest_example.py` 
