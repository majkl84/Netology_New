import json
from models import Publisher, Book, Shop, Stock, Sale


class DataLoader:
    def __init__(self, session):
        self.session = session

    def load_data(self, filename):
        with open(filename, 'r') as f:
            test_data = json.load(f)

        for data in test_data:
            model = data['model']
            fields = data['fields']
            if model == 'publisher':
                if not self.session.query(Publisher).filter_by(name=fields['name']).first():
                    publisher = Publisher(name=fields['name'])
                    publisher.id = data['pk']
                    self.session.add(publisher)
            elif model == 'book':
                if not self.session.query(Book).filter_by(title=fields['title'],
                                                          id_publisher=fields['publisher']).first():
                    book = Book(title=fields['title'], id_publisher=fields['publisher'])
                    book.id = data['pk']
                    self.session.add(book)
            elif model == 'shop':
                if not self.session.query(Shop).filter_by(name=fields['name']).first():
                    shop = Shop(name=fields['name'])
                    shop.id = data['pk']
                    self.session.add(shop)
            elif model == 'stock':
                if not self.session.query(Stock).filter_by(id_shop=fields['shop'], id_book=fields['book']).first():
                    stock = Stock(id_shop=fields['shop'], id_book=fields['book'], count=fields['count'])
                    stock.id = data['pk']
                    self.session.add(stock)
            elif model == 'sale':
                if not self.session.query(Sale).filter_by(price=fields['price'], id_stock=fields['stock']).first():
                    sale = Sale(price=fields['price'], count=fields['count'], id_stock=fields['stock'])
                    sale.id = data['pk']
                    self.session.add(sale)

        self.session.commit()
