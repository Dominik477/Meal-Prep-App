from pydantic import BaseModel, EmailStr


class ProductOut(BaseModel):
    id: int
    name: str
    calories_per_100g: float

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    calories_per_100g: float


class ProductUpdate(BaseModel):
    name: str | None = None
    calories_per_100g: float | None = None


class RegisterIn(BaseModel):
    email: EmailStr
    full_name: str
    password: str


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut
