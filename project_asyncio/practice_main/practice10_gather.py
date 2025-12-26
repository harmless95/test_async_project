import asyncio


async def factorial_function(name, number):
    result_f = 1
    for i in range(2, number + 1):
        print(f"Task: {name}, number: {number}")
        result_f *= i
        await asyncio.sleep(delay=3)
    print(f"Task {name} completed factorial: {result_f}")
    return result_f


async def main():
    # 1) Выполняются одновременно 3 задачи.
    # 2) Все спят
    # 3) Task 'A' завершилось и выводит результат, но другие продолжают выполняться
    await asyncio.gather(
        factorial_function(name="A", number=2),
        factorial_function(name="B", number=6),
        factorial_function(name="C", number=4),
    )


if __name__ == "__main__":
    asyncio.run(main())
