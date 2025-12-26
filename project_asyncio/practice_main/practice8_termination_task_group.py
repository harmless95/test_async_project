import asyncio
from asyncio import TaskGroup


class TerminationTask(Exception):
    """Exception raised to terminate a task group."""


async def function_termination():
    raise TerminationTask


async def work_task(user_id, delay):
    print(f"Start user: {user_id}")
    await asyncio.sleep(delay=delay)
    print(f"Done: {user_id}")


async def main():
    try:
        async with TaskGroup() as group:
            group.create_task(work_task(user_id=1, delay=2))
            group.create_task(work_task(user_id=2, delay=5))

            await asyncio.sleep(delay=1)
            group.create_task(function_termination())
    except* TerminationTask:
        pass


if __name__ == "__main__":
    asyncio.run(main())
