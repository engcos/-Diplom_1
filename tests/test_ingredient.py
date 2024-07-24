import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
def test_ingredient_creation():
    # Создаем объект Ingredient и проверяем его свойства
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE  # Проверка типа ингредиента
    assert ingredient.get_name() == "hot sauce"  # Проверка имени ингредиента
    assert ingredient.get_price() == 100  # Проверка цены ингредиента

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
])
def test_ingredient_parametrized(type_, name, price):
    # Создаем объект Ingredient с параметрами и проверяем его свойства
    ingredient = Ingredient(type_, name, price)
    assert ingredient.get_type() == type_  # Проверка типа ингредиента
    assert ingredient.get_name() == name  # Проверка имени ингредиента
    assert ingredient.get_price() == price  # Проверка цены ингредиента
