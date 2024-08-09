class Category:
    name = str #название категории
    description = str #описание
    products = list #лист с продуктами
    count_category = 0 #количество категорий
    count_products = 0 #количество продуктов

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.count_category += 1
        Category.count_products += len(products) if products else 0
