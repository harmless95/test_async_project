import asyncio


async def long_task(name, delay):
    await asyncio.sleep(delay=delay)
    return f"{name} - {delay}"


async def main():
    tasks = [
        asyncio.create_task(long_task(name="утро", delay=0.5)),
        asyncio.create_task(long_task(name="день", delay=1)),
        asyncio.create_task(long_task(name="вечер", delay=3)),
        asyncio.create_task(long_task(name="ночь", delay=1)),
    ]
    for task in asyncio.as_completed(tasks, timeout=3):
        try:
            result = await task
            print(result)
        except asyncio.TimeoutError:
            print("Сработал Timeout")


if __name__ == "__main__":
    asyncio.run(main())
