import asyncio
import time


async def sleep_function(delay):
    await asyncio.sleep(delay=delay)
    return f"Sleep {delay}"


async def return_function():
    return "Return"


async def sleep_function2(delay):
    await asyncio.sleep(delay=delay)
    return f"Sleep {delay}"


async def sleep_function3(delay):
    await asyncio.sleep(delay=delay)
    return f"Sleep {delay}"


async def main():
    print(time.strftime("%X"))
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(sleep_function(delay=4))
        task2 = tg.create_task(return_function())
        task3 = tg.create_task(sleep_function2(delay=7))
        task4 = tg.create_task(sleep_function3(delay=2))
    print(
        f"Result: {task1.result()}, {task2.result()}, {task3.result()}, {task4.result()}"
    )
    print(time.strftime("%X"))


if __name__ == "__main__":
    asyncio.run(main())
