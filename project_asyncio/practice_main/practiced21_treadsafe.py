import asyncio
import concurrent.futures
import contextlib
from typing import Generator


@contextlib.contextmanager
def loop_in_thread() -> Generator[asyncio.AbstractEventLoop]:
    loop_fut = concurrent.futures.Future[asyncio.AbstractEventLoop]()
    stop_event_loop = asyncio.Event()

    async def main() -> None:
        loop_fut.set_result(asyncio.get_running_loop())
        await stop_event_loop.wait()

    with concurrent.futures.ThreadPoolExecutor(1) as tpe:
        complete_fut = tpe.submit(asyncio.run, main())
        for fur in concurrent.futures.as_completed((loop_fut, complete_fut)):
            if fur is loop_fut:
                loop = loop_fut.result()
                try:
                    yield loop
                finally:
                    loop.call_soon_threadsafe(stop_event_loop.set)
            else:
                fur.result()


with loop_in_thread() as loop:
    coro = asyncio.sleep(1, result=3)
    future = asyncio.run_coroutine_threadsafe(coro=coro, loop=loop)

    assert future.result(timeout=2) == 3
