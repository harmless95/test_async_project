import asyncio


async def main():
    print("Hello world")
    await asyncio.sleep(1)
    print("Home")

if __name__ == "__main__":
    asyncio.run(main())