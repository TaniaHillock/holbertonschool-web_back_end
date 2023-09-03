#!/usr/bin/env python3
"""Import async_comprehension from 1-async_comprehension.py
and write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime measures the total runtime and return it"""
import asyncio
import random
from typing import Generator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The coroutine will collect 10 random numbers using an async comprehensing over async_generator,
    then return the 10 random numbers"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
