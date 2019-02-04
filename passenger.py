class Passanger:
    price = 0.0
    fee = 0.0
    tax = 0.0

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return '<category: {}, price: {}, fee: {}, tax: {}>'.format(self.category, self.price, self.fee, self.tax)

    def set_price(self, price):
        self.price = price

    def set_fee(self, fee):
        self.fee = fee

    def set_tax(self, tax):
        self.tax = tax
