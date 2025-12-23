import asyncio
import time


async def function_example(count, text):
    await asyncio.sleep(count)
    print(f"Await function: {text}")


async def main():
    task1 = asyncio.create_task(
        function_example(count=1, text="hello"),
    )
    task2 = asyncio.create_task(
        function_example(count=2, text="world"),
    )
    # task1 и task2 обрабатываются одновременно и эффективны для фоновых задач время выполнения 2 сек.
    print(f"Start: {time.strftime("%X")}")
    await task1
    await task2
    print(f"End: {time.strftime("%X")}")


if __name__ == "__main__":
    asyncio.run(main())
