from fastapi import FastAPI
import asyncio

app = FastAPI()


async def fetch_source_a() -> str:
    await asyncio.sleep(1)
    return "Data from source A"


async def fetch_source_b() -> str:
    await asyncio.sleep(1)
    return "Data from source B"


@app.get("/async-data")
async def get_async_data():
    results = await asyncio.gather(fetch_source_a(), fetch_source_b())
    return {"source_a": results[0], "source_b": results[1]}
