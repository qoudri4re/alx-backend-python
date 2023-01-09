#!/usr/bin/env python3
'''Task 0'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random number of seconds'''
    waitTime = random.uniform(0, max_delay)
    await asyncio.sleep(waitTime)
    return waitTime
