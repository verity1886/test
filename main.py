from booking import Booking
from passenger import Passanger
from strategies.equal_price_strategy import EqualPriceStrategy
from strategies.age_based_strategy import AgeBasedStrategy


class PriceCalculator:
    def __init__(self, booking, strategy):
        self.booking = booking
        self.strategy = strategy

    def prepare_passengers(self):
        self.strategy.process_passengers(self.booking)

if __name__ == '__main__':
    passanger1 = Passanger('adult')
    passanger2 = Passanger('infant')
    passanger3 = Passanger('child')

    booking1 = Booking(100.0, 10.0, 20.0, [passanger1, passanger2, passanger3])
    strategy1 = EqualPriceStrategy()

    PriceCalculator(booking1, strategy1).prepare_passengers()
    print(booking1.get_passangers())

    passanger4 = Passanger('adult')
    passanger5 = Passanger('infant')
    passanger6 = Passanger('child')

    booking2 = Booking(100.0, 10.0, 20.0, [passanger4, passanger5, passanger6])
    strategy2 = AgeBasedStrategy()

    PriceCalculator(booking2, strategy2).prepare_passengers()
    print(booking2.get_passangers())

    # In order to have same price, fee & tax they could be just set 
    # after summing of appropriate fields of passengers after calculating :)
