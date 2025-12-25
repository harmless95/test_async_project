import asyncio
import time


async def some_python_coroutine(delay):
    raise ValueError
    await asyncio.sleep(delay=delay)
    return "A"


async def function_that_returns_a_future_object(delay):
    await asyncio.sleep(delay=delay)
    return "B"


async def main():
    print(time.strftime("%X"))
    await function_that_returns_a_future_object(delay=4)
    print(time.strftime("%X"))
    result = await asyncio.gather(
        some_python_coroutine(delay=3),
        function_that_returns_a_future_object(delay=2),
        return_exceptions=True,
    )
    print(result)
    print(time.strftime("%X"))


if __name__ == "__main__":
    asyncio.run(main())
