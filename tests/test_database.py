import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_database_available_buns():
    # Проверяем доступные булочки в базе данных
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"


def test_database_available_ingredients():
    # Проверяем доступные ингредиенты в базе данных
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
