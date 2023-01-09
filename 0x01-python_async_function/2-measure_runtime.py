#!/usr/bin/env python3
'''task 2
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''computes average wait time'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n