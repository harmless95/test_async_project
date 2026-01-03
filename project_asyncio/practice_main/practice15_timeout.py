import asyncio


async def long_task(delay):
    print(f"Start: {delay}s")
    await asyncio.sleep(delay=delay)


async def main():
    loop = asyncio.get_running_loop()
    deadline = loop.time() + 2
    print(f"DEBUG deadline={deadline:.3f} now={loop.time():.3f}")
    try:
        async with asyncio.timeout(deadline):
            await long_task(delay=10)
            print(f"Finish")
    except TimeoutError as ex:
        print(f"Task running failed")


if __name__ == "__main__":
    asyncio.run(main())
