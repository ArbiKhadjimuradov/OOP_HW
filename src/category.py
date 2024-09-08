from src.product import Product

class Category:
    name = str  #название категории
    description = str  #описание
    products = list  #лист с продуктами
    count_category = 0  #количество категорий
    count_products = 0  #количество продуктов

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.count_category += 1
        Category.count_products += len(products) if products else 0

    def add_product(self, products):
        if isinstance(products, Product):
            try:
                if products.quantity == 0:
                    raise ExeptionForCategory("Нельзя внести товар с нулевым количеством")
            except ExeptionForCategory as e:
                print(str(e))
            else:
                self.__products.append(products)
                Category.count_products += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    def count_product(self):
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        total_products_count = sum([p.quantity for p in self.__products])
        return f"{self.name}, количество продуктов: {total_products_count} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def middle_price(self):
        try:
            total_price = sum(products.price * products.quantity for products in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0


class ExeptionForCategory(Exception):
    def __init__(self, message=None):
        super().__init__(message)