import pytest
from praktikum.bun import Bun

def test_bun_creation():
    # Создаем булочку и проверяем её имя и цену
    bun = Bun("white bun", 200)
    assert bun.get_name() == "white bun"
    assert bun.get_price() == 200

@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("red bun", 300),
])
def test_bun_parametrized(name, price):
    # Параметризованный тест для различных булочек
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
