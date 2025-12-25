import asyncio
import time
import logging

background = set()
logger = logging.getLogger(__name__)


async def corut_function(param):
    logger.warning("Running1: %s", param)
    await asyncio.sleep(delay=param)
    logger.warning("Running: %s", param)


async def main():
    print(time.strftime("%X"))
    for i in range(10):
        # Создаем фоновую задачу
        task = asyncio.create_task(corut_function(param=i))

        # Сохраняем сыллку
        background.add(task)

        # Задача удаляет свою собственную сыллку
        task.add_done_callback(background.discard)

    # Выполняются все задачи одновременно и время выполнения будет равна самой долгой операции
    await asyncio.gather(*list(background))
    print(time.strftime("%X"))


if __name__ == "__main__":
    asyncio.run(main())
