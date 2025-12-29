import asyncio


async def long_task(delay):
    print(f"Run a long task: {delay}s")
    await asyncio.sleep(delay=delay)


async def main():
    try:
        async with asyncio.timeout(8):
            task = await asyncio.create_task(long_task(delay=7))
            print(f"Completed task")
        print("Finish task")

    # The asyncio.timeout() context manager is what transforms the asyncio.CancelledError into a TimeoutError,
    # which means the TimeoutError can only be caught outside of the context manager.
    except TimeoutError as ex:
        print("The task failed, the timeout expired")


if __name__ == "__main__":
    asyncio.run(main())
