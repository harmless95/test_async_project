import asyncio


class LoggingTask(asyncio.Task):
    def __init__(self, coro):
        print(f"Старт задачи: {coro.__name__}")
        super().__init__(coro)

    def __repr__(self):
        return f"<MyTask: {self.get_coro().__name__} - {self._state}>"

    def cancel(self):
        print(f"Отмена{self.get_coro().__name__}")
        return super().cancel()


def config_function(loop, coro):
    return LoggingTask(coro)


async def get_result_a(delay):
    await asyncio.sleep(delay=delay)
    return "A"


async def get_result_b(delay):
    await asyncio.sleep(delay=delay)
    return "B"


async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(lambda loop, coro: config_function(loop=loop, coro=coro))

    task1 = asyncio.create_task(get_result_a(delay=3))
    task2 = asyncio.create_task(get_result_b(delay=5))
    task3 = asyncio.create_task(get_result_a(delay=2))
    print(task1)
    print(task2)
    print(task3)

    print(f"Result: {await task1}, {await task2}, {await task3}")


if __name__ == "__main__":
    asyncio.run(main())
