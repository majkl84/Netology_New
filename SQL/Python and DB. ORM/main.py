from database import create_engine, create_tables, get_session
from data_loader import DataLoader
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("gui.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# создаем подключение к базе данных
engine = create_engine()

# создаем таблицы
create_tables(engine)

# получаем сессию
session = get_session(engine)

data_loader = DataLoader(session)
data_loader.load_data('data.json')


def search():
    # Получаем текст из QPlainTextEdit
    publisher_name_or_id = form.search.toPlainText()

    # Проверяем, является ли введенное значение идентификатором публициста
    if publisher_name_or_id.isdigit():
        # Если да, то выполняем запрос к базе данных, где идентификатор равен введенному значению
        query = (
            session.query(Shop.name)
            .join(Stock)
            .join(Book)
            .join(Publisher)
            .filter(Publisher.id == int(publisher_name_or_id))
            .distinct()
        )
    else:
        # Если нет, то выполняем запрос к базе данных, где имя публициста равно введенному значению
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
    if result:
        form.label.setText('\n'.join(result))
    else:
        form.label.setText('Ничего не найдено')


form.btnsearch.clicked.connect(search)

app.exec()
session.close()
