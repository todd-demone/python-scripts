#!/usr/bin/env python3
"""tests for hello.py"""

import pytest
from hello import say_hello


# --------------------------------------------------
def test_say_hello_no_arg():
    """tests with no arguments"""

    result = say_hello()
    assert result == "Hello, World!"


# --------------------------------------------------
def test_say_hello_with_arg():
    """tests with optional --name argument"""

    result = say_hello("Bob")
    assert result == "Hello, Bob!"


# --------------------------------------------------
def test_say_hello_with_non_string_arg():
    """tests with non-string argument"""

    with pytest.raises(TypeError):
        say_hello(123)
