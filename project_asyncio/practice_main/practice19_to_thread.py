import asyncio
import time
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def blocking_io(delay):
    logger.info("Start blocking io: %s", time.strftime("%X"))
    time.sleep(delay)
    logger.info(
        "Finish blocking io: %s", time.strftime("%X")
    )  # Время выполнения текущей задачи


async def main():
    logger.info("Start main: %s", time.strftime("%X"))
    # Выполняются задачи одновременно блокирующая работает в отдельном потоке
    await asyncio.gather(asyncio.to_thread(blocking_io, 4), asyncio.sleep(delay=6))
    logger.info(
        "Finish main: %s", time.strftime("%X")
    )  # Время выполнения всех задач = max(4, 6) = 6 сек


if __name__ == "__main__":
    asyncio.run(main())
