from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: float,
            car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
