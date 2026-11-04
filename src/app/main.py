from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="SDC Supply Chain Portal")

# Future: include API routers here (e.g. app.include_router(documents.router))
# and add a database session, mirroring the RAMS tracker layout.

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
async def index():
    return FileResponse(STATIC_DIR / "index.html")
