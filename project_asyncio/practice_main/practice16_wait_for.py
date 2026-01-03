import asyncio
import logging

logger = logging.getLogger(__name__)


async def long_task(delay):
    logger.info("Running a coroutine long task %s", delay)
    await asyncio.sleep(delay=delay)


async def main():
    logger.info("Start main")
    try:
        await asyncio.wait_for(long_task(delay=6), 5)
        logger.info("Completed running task")
    except TimeoutError as ex:
        logger.warning("TimeoutError %s", ex)


if __name__ == "__main__":
    asyncio.run(main())
