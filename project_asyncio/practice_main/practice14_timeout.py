import asyncio


async def long_task(delay):
    print(f"Run a long task: {delay}s")
    await asyncio.sleep(delay=delay)


async def main():
    try:
        async with asyncio.timeout(None) as at:
            current_loop = asyncio.get_running_loop().time() + 10
            at.reschedule(current_loop)
            await long_task(delay=11)
            print(f"Completed task")
        print("Finish task")

    except TimeoutError as ex:
        print("The task failed, the timeout expired")


if __name__ == "__main__":
    asyncio.run(main())
