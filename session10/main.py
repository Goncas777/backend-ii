from html import escape

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/safe")
async def safe_response(
    text: str = Query(
        ...,
        min_length=1,
        max_length=200,
        pattern=r"^[\w\s.,!?@#&'\-]+$",
    )
):
    # Escape HTML to prevent script injection in the response.
    safe_text = escape(text, quote=True)
    return {"safe_text": safe_text}
