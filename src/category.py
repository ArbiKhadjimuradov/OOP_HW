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
        self.__products.append(products)
        Category.count_products += 1

    def __str__(self):
        return f"{self.name}, {self.count_category}:  {self.count_products} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
