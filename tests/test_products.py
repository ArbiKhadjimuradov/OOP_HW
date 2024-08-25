from src.product import Smartphone


def test_product_iphone(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_xiaomi(product_xiaomi):
    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.description == "512GB, Gray space"
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "15"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_lawngrass_init(lawngrass1):
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"