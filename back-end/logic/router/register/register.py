from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from logic.db.database import session_local
from logic.db.models import User
from sqlalchemy.orm import Session
import bcrypt

router = APIRouter()

@router.post("/register")
async def register(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")

    # Получаем IP пользователя
    ip = request.client.host

    if not username or not password:
        raise HTTPException(status_code=400, detail="Поля username и password обязательны")
    
    db: Session = session_local()

    # Проверяем, есть ли уже такой пользователь
    existing_user = db.query(User).filter(User.login == username).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    # Хэшируем пароль (даже если хотим «небезопасно», оставим)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Создаём нового пользователя
    new_user = User(
        login=username,
        password_hash=hashed_password.decode('utf-8'),
        password=password,
        ip=ip,
        country=None  # можно позже получить по IP
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return JSONResponse({"success": True, "message": "Регистрация успешна!"})
