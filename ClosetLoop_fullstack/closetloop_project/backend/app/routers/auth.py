from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import RegisterIn, LoginIn, ChangePasswordIn, TokenOut, UserOut
from ..security import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=TokenOut)
def register(data: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter((User.email == data.email) | (User.username == data.username)).first():
        raise HTTPException(400, "Email or username already exists")
    user = User(
        username=data.username.strip(),
        email=data.email.lower(),
        password_hash=hash_password(data.password),
        display_name=data.display_name.strip() or data.username.strip()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return TokenOut(access_token=create_access_token(user.id), user=user)

@router.post("/login", response_model=TokenOut)
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email.lower()).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(401, "Invalid email or password")
    return TokenOut(access_token=create_access_token(user.id), user=user)

@router.post("/logout")
def logout():
    return {"message": "Logged out. Remove the bearer token on the client."}

@router.post("/change-password")
def change_password(
    data: ChangePasswordIn,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not verify_password(data.current_password, current_user.password_hash):
        raise HTTPException(400, "Current password is incorrect")
    current_user.password_hash = hash_password(data.new_password)
    db.commit()
    return {"message": "Password changed successfully"}
