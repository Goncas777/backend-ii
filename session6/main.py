import asyncio


async def task_function(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} completed"


async def run_task_with_timeout(name: str, delay: float, timeout: float) -> str:
    task = asyncio.create_task(task_function(name, delay))
    try:
        return await asyncio.wait_for(task, timeout=timeout)
    except asyncio.TimeoutError:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        return f"{name} timed out"


async def main() -> None:
    results = await asyncio.gather(
        run_task_with_timeout("Task 1", 1.0, 2.0),
        run_task_with_timeout("Task 2", 2.0, 1.0),
        run_task_with_timeout("Task 3", 0.5, 1.0),
    )
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
