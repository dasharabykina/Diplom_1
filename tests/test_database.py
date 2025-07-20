from data import TestDataBase
from conftest import db
import pytest


class TestDB:
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.database_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price

    @pytest.mark.parametrize('index_ingredient, type_ingredient, name_ingredient, price_ingredient', TestDataBase.database_ingredients)
    def test_available_ingredients_db_success(self, db, index_ingredient, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = db.available_ingredients()
        assert (data_ingredients[index_ingredient].get_name() == name_ingredient and
                data_ingredients[index_ingredient].get_type() == type_ingredient and
                data_ingredients[index_ingredient].get_price() == price_ingredient)