class Category:
    name = str
    description = str
    produts = list
    count_category = 0
    count_products = 0

    def __init__(self, name, description, produts=None):
        self.product = None
        self.name = name
        self.description = description
        self.produts = produts if produts else []

        Category.count_category += 1
        Category.count_products += len(produts) if produts else 0
