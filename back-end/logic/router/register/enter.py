from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from logic.db.database import session_local
from logic.db.models import User
from sqlalchemy.orm import Session

import bcrypt

router = APIRouter()

@router.post("/login")
async def login(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")

    db: Session = session_local()
    user = db.query(User).filter(User.username == username).first()
    db.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return JSONResponse({"success": True, "message": "Вход выполнен!"})
    else:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
