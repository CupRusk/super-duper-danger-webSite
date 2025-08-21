from fastapi import FastAPI, HTTPException, Request
from logic.db.models import User
from logic.db.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path
from logic.router.register import register
from logic.router.register import enter
Base.metadata.create_all(bind=engine)
# запуск FastApi
app = FastAPI()

# роутеры
app.include_router(register.router, prefix="/api")
app.include_router(enter.router, prefix="/api")


# корсы
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Пути
BASE_DIR = Path(__file__).parent.parent 
FRONTEND_DIR = BASE_DIR / "front-end" / "html"  # теперь указываем сразу html

# монтируем статику
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# рут отдаёт index
@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_file = FRONTEND_DIR / "index.html"  # точное имя файла
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as file:
            content = file.read()
        return HTMLResponse(content=content)
    else:
        raise HTTPException(status_code=404, detail="Файл html.index не найден")


