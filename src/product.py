class Product:
    name: str #название
    description: str #описание
    price: (float, 1) #цена
    quantity: int #количество

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    @classmethod
    def new_product(cls, new_product: dict):
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
            return