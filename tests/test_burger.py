from data import BunTestData1, BunTestData2
from praktikum_module.burger import Burger
from conftest import *


class TestBurger:

    def test_set_buns_add_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize('ingredients, added_ingredient',[
        [BunTestData1.sauce_name, BunTestData1.sauce_name],
        [BunTestData1.filling_name, BunTestData1.filling_name],
        [BunTestData2.filling_name, BunTestData2.filling_name]
        ]
    )
    def test_add_ingredient_add_success(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1


    @pytest.mark.parametrize('ingredients, removed_ingredient',[
        [BunTestData1.sauce_name, BunTestData1.sauce_name],
        [BunTestData2.filling_name, BunTestData2.filling_name]
        ]
    )
    def test_remove_ingredient_delete_success(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients


    def test_move_ingredient_move_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2 and burger.ingredients[0] == mock_filling and burger.ingredients[1] ==mock_sauce

    def test_get_price_burger_success(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == BunTestData2.burger_final_cost

    def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_receipt() == ('(==== Краторная булка N-200i ====)\n'
                                        '= sauce Соус Spicy-X =\n'
                                        '= filling Мини-салат Экзо-Плантаго =\n'
                                        '= filling Мясо бессмертных моллюсков Protostomia =\n'
                                        '(==== Краторная булка N-200i ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')