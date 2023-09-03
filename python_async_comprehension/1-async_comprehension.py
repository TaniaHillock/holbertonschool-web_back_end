#!/usr/bin/env python3
"""Imports async_generator from 1-async_comprehension.py"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random, return the 10 random numbers.
    Function returns a typing.List[float]"""
    i = [i async for i in async_generator()]
    return i
