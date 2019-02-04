class Booking:
    def __init__(self, price, fee, tax, passangers):
        self.price = price
        self.fee = fee
        self.tax = tax
        self.passangers = passangers

    def get_passangers(self):
        return self.passangers
