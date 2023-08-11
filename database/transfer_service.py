from database.models import Transaction, Card
from database import get_db


# Перевод денег
def money_transfer_db(card_from, card_to, amount, transaction_date):
    db = next(get_db())

    card_from_db = db.query(Card).filter_by(card_number=card_from).first()
    card_to_db = db.query(Card).filter_by(card_number=card_to).first()

    # Проверка есть ли эти карты
    if card_from_db and card_to_db:
        # проверка достаточно ли денег
        if card_from_db.card_balance >= amount:
            card_from_db.card_balance -= amount
            card_to_db.card_balance += amount

            new_transaction = Transaction(card_from=card_from,
                                          card_to=card_to,
                                          amount=amount,
                                          transfer_time=transaction_date)

            db.add(new_transaction)
            db.commit()

            return True

        return 'Недостаточно средств'

    return 'Ошибка в данных'

# мониторинг по card_id
