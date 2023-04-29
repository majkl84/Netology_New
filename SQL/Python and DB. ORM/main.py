import json
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

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
        if not session.query(Publisher).filter_by(name=fields['name']).first():
            publisher = Publisher(name=fields['name'])
            publisher.id = data['pk']
            session.add(publisher)
    elif model == 'book':
        if not session.query(Book).filter_by(title=fields['title'], id_publisher=fields['publisher']).first():
            book = Book(title=fields['title'], id_publisher=fields['publisher'])
            book.id = data['pk']
            session.add(book)
    elif model == 'shop':
        if not session.query(Shop).filter_by(name=fields['name']).first():
            shop = Shop(name=fields['name'])
            shop.id = data['pk']
            session.add(shop)
    elif model == 'stock':
        if not session.query(Stock).filter_by(id_shop=fields['shop'], id_book=fields['book']).first():
            stock = Stock(id_shop=fields['shop'], id_book=fields['book'], count=fields['count'])
            stock.id = data['pk']
            session.add(stock)
    elif model == 'sale':
        if not session.query(Sale).filter_by(price=fields['price'], id_stock=fields['stock']).first():
            sale = Sale(price=fields['price'], count=fields['count'], id_stock=fields['stock'])
            sale.id = data['pk']
            session.add(sale)

# Сохраняем изменения в БД
session.commit()
#
# # получаем имя или идентификатор издателя через input()
# publisher_name_or_id = input("Введите имя или идентификатор издателя: ")
#
# # формируем запрос на выборку магазинов, которые продавали книги заданного издателя
# query = (
#     session.query(Shop.name)
#     .join(Stock)
#     .join(Book)
#     .join(Publisher)
#     .filter(Publisher.name == publisher_name_or_id)
#     .distinct()
# )
#
# # выводим результаты запроса
# print(f"Магазины, продававшие книги издательства {publisher_name_or_id}:")
# for shop_name, in query:
#     print(shop_name)

def search():
    # Получаем текст из QPlainTextEdit
    publisher_name_or_id = form.search.toPlainText()

    # Выполняем запрос к базе данных
    query = (
        session.query(Shop.name)
        .join(Stock)
        .join(Book)
        .join(Publisher)
        .filter(Publisher.name == publisher_name_or_id)
        .distinct()
    )

    # Выводим результаты запроса в QLabel
    result = []
    for shop_name, in query:
        result.append(shop_name)
    form.label.setText('\n'.join(result))

form.btnsearch.clicked.connect(search)

app.exec()
session.close()
