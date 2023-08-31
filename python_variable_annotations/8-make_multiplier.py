#!/usr/bin/env python3
"""annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(multiplier: float) -> float:
        """multiplies a float by multiplier"""
    return multiplier * multiplier
return multiply
