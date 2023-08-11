from fastapi import Body

from main import app
from .profile_models import UserDent, CardDent


# Регистрация пользователя
@app.post('/api/register-user')
async def user_registration(user_data: UserDent):
    print(user_data)

    # После регистрации выдать айди пользователя
    return {'status': 1, 'message': 'Registration completed'}


# Вход в аккаунт
@app.post('/api/login-user')
async def login_user(phone_number: int = Body(), password: str = Body()):
    print(phone_number, password)
    # Проверка данных
    checker = None

    # если данные верны, отправляем юзер айди и данные пользователя
    return {'status': 1, 'message': 'Logged in'}


# Добавление карты в базу
@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    # вызов функции из бд для добавления карты в базу
    result = card_data
    print(card_data)

    # Если успешно добавлена карта, то status 1
    return {'status': 1, 'message': result}


# вывод данных о пользователе
@app.get('/api/user-data')
async def get_user_data(user_id: int):
    pass


# вывод всех или определенных карт пользователя
@app.get('/api/user-cards')
async def get_user_cards(user_id: int, card_id: int = 0):
    pass
