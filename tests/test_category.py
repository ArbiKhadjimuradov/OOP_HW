def test_category_phone(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3
    assert first_category.count_category == 2
    assert second_category.count_category == 2
    assert first_category.count_products == 4
    assert second_category.count_products == 4


def test_category_tv(first_category, second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(second_category.products) == 1
