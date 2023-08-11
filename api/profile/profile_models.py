from pydantic import BaseModel

from datetime import datetime


# Модель входных данных пользователя
class UserDent(BaseModel):
    profile_photo: str
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    reg_date: datetime
    password: str


# Модель для карты пользователя
class CardDent(BaseModel):
    user_id: int
    card_number: int
    cardholder: str
    exp_date: int
    card_balance: float
    card_name: str









