import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s: %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


async def long_task(delay):
    logger.info("Start long task: %s", delay)
    await asyncio.sleep(delay=delay)
    return delay


async def main():
    aws = [asyncio.create_task(long_task(delay=i)) for i in range(1, 5 + 1)]
    done, pending = await asyncio.wait(aws, timeout=3, return_when="ALL_COMPLETED")
    for i in done:
        try:
            result = await i
            logger.info("Completed task result: %s", result)
        except asyncio.CancelledError:
            logger.info("Done task was cancelled")

    for p in pending:
        p.cancel()
        logger.info("Cancelled pending task: %s", p.get_name())
        try:
            await p
        except asyncio.CancelledError:
            logger.info("Pending task %s cancelled successfully", p.get_name())


if __name__ == "__main__":
    asyncio.run(main())
