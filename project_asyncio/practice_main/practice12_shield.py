import asyncio
from asyncio import shield, CancelledError


async def sleep_function(delay):
    await asyncio.sleep(delay=delay)
    return f"Sleep: {delay}"


async def main():
    task = asyncio.create_task(sleep_function(delay=4))
    try:
        task_shield = await shield(task)
    except CancelledError:
        task_shield = None


if __name__ == "__main__":
    asyncio.run(main())
