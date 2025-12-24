import asyncio


async def set_after(fut, delay, value):
    await asyncio.sleep(delay=delay)
    fut.set_result(value)


async def main():
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    asyncio.create_task(set_after(fut=fut, delay=3, value="Helo...."))
    print("World....")
    print(await fut)


if __name__ == "__main__":
    asyncio.run(main())
