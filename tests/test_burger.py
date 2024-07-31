import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    # Создаем мок-объект Bun
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    bun.get_name.return_value = "white bun"
    return bun

@pytest.fixture
def mock_ingredient_sauce():
    # Создаем мок-объект Ingredient с типом соус
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50
    ingredient.get_name.return_value = "sour cream"
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient

@pytest.fixture
def mock_ingredient_filling():
    # Создаем мок-объект Ingredient с типом начинка
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 150
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient

def test_burger_creation(mock_bun):
    # Создаем объект Burger и проверяем установку булочки
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun  # Проверка установленной булочки

def test_burger_add_ingredient(mock_bun, mock_ingredient_sauce):
    # Проверяем добавление ингредиента в бургер
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    assert len(burger.ingredients) == 1  # Проверка количества ингредиентов
    assert burger.ingredients[0] == mock_ingredient_sauce  # Проверка добавленного ингредиента

def test_burger_remove_ingredient(mock_bun, mock_ingredient_sauce):
    # Проверяем удаление ингредиента из бургера
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0  # Проверка количества ингредиентов после удаления

def test_burger_move_ingredient(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    # Проверяем перемещение ингредиента в бургере
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == mock_ingredient_filling  # Проверка перемещения ингредиента
    assert burger.ingredients[1] == mock_ingredient_sauce  # Проверка перемещения ингредиента

def test_burger_get_price(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    # Проверяем расчет цены бургера
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    assert burger.get_price() == 100 * 2 + 50 + 150  # Проверка итоговой цены бургера

def test_burger_get_receipt(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    # Проверяем получение чека для бургера
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    receipt = burger.get_receipt()
    expected_receipt = (
        "(==== white bun ====)\n"
        "= sauce sour cream =\n"
        "= filling cutlet =\n"
        "(==== white bun ====)\n"
        "\nPrice: 400"
    )
    assert receipt == expected_receipt  # Проверка содержимого чека