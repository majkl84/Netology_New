import json
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = "postgresql://postgres:majkl4321@localhost:5432/netology"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
# сессия
Session = sessionmaker(bind=engine)
session = Session()

with open('data.json', 'r') as f:
    test_data = json.load(f)

# Создаем экземпляры моделей и сохраняем их в БД
for data in test_data:
    model = data['model']
    fields = data['fields']
    if model == 'publisher':
        publisher = Publisher(name=fields['name'])
        publisher.id = data['pk']
        session.add(publisher)
    elif model == 'book':
        book = Book(title=fields['title'], publisher_id=fields['publisher'])
        book.id = data['pk']
        session.add(book)
    elif model == 'shop':
        shop = Shop(name=fields['name'])
        shop.id = data['pk']
        session.add(shop)
    elif model == 'stock':
        stock = Stock(shop_id=fields['shop'], book_id=fields['book'], count=fields['count'])
        stock.id = data['pk']
        session.add(stock)
    elif model == 'sale':
        sale = Sale(price=fields['price'], count=fields['count'], stock_id=fields['stock'])
        sale.id = data['pk']
        session.add(sale)

# Сохраняем изменения в БД
session.commit()

session.close()