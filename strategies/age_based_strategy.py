from equal_price_strategy import EqualPriceStrategy

class AgeBasedStrategy(EqualPriceStrategy):
    def process_passengers(self, booking):
        passangers = booking.get_passangers()
        self.validate(passangers)
        
        adults = self.get_passengers_by_category(passangers, 'adult')
        infants = self.get_passengers_by_category(passangers, 'infant')
        children = self.get_passengers_by_category(passangers, 'child')
        
        for passenger in infants:
            self.process_single_passenger(passenger, 0, 0, 0)

        for passenger in children:
            price = booking.price / (len(adults) + (len(children) / 0.6))
            fee = booking.fee / (len(adults) + (len(children) / 0.6))
            tax = booking.tax / (len(adults) + (len(children) / 0.6))
            self.process_single_passenger(passenger, price, fee, tax)

        for passenger in adults:
            price = booking.price / (len(adults) + (len(children) * 0.6))
            fee = booking.fee / (len(adults) + (len(children) * 0.6))
            tax = booking.tax / (len(adults) + (len(children) * 0.6))
            self.process_single_passenger(passenger, price, fee, tax)

    def get_passengers_by_category(self, passangers, category):
        matched_passangers = []
        for passanger in passangers:
            if (passanger.category == category):
                matched_passangers.append(passanger)

        return matched_passangers

    def validate(self, passengers):
        if not len(passengers) > 0:
            raise ValueError('There should be at least one passanger!')
        
        for passenger in passengers:
            if (passenger.category == 'adult'):
                break
        else:
            raise ValueError('There should be at least one adult passanger!')
