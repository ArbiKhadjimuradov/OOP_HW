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
