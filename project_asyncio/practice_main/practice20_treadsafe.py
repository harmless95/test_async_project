import asyncio
import logging
import pathlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def function_tread(loop: asyncio.AbstractEventLoop):
    logger.info("Start sync function")

    # Блокирует поток, но не event loop
    pathlib.Path("example.txt").write_text("Hello2", encoding="utf8")

    coro = asyncio.sleep(3, result=4)  # Указываем result по умолчанию возвращает None

    # future — это мост между синхронным потоком и асинхронным event loop.
    # Блокирует ТОЛЬКО поток при .result(), оставляя event loop свободным.
    logger.info("Run async coroutine")
    future = asyncio.run_coroutine_threadsafe(coro=coro, loop=loop)

    logger.info("Finish async coroutine")
    # Если не успевает выполнится за время timeout поднимается исключение TimeoutError
    assert future.result(timeout=2) == 4
    logger.info("Finish sync function")


async def main():
    logger.info("Start main")
    loop = asyncio.get_running_loop()
    # Создаем Task и передает в поток
    await asyncio.to_thread(function_tread, loop)
    logger.info("Finish main")


if __name__ == "__main__":
    asyncio.run(main())
