from math import ceil

class EqualPriceStrategy:
    def process_passengers(self, booking):
        passengers = booking.get_passangers()
        self.validate(passengers)
        price = booking.price / len(passengers)
        fee = booking.fee / len(passengers)
        tax = booking.tax / len(passengers)
        for passenger in passengers:
            self.process_single_passenger(passenger, price, fee, tax)

    def process_single_passenger(self, passenger, price, fee, tax):
        passenger.set_price(self.round_float(price))
        passenger.set_fee(self.round_float(fee))
        passenger.set_tax(self.round_float(tax))

    def round_float(self, float_number):
        return ceil(float_number * 100) / 100.0

    def validate(self, passengers):
        if not len(passengers) > 0:
            raise ValueError('There should be one passanger at least!')
