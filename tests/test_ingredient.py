from conftest import *


class TestIngredient:

    def test_get_name_sauce_success(self, mock_sauce):
        assert mock_sauce.get_name() == BunTestData1.sauce_name


    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == BunTestData1.filling_name


    def test_get_price_sauce_success(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == BunTestData2.sauce_price


    def test_get_price_filling_success(self, mock_filling_2):
        assert mock_filling_2.get_price() == BunTestData2.filling_price


    def test_get_type_sauce_success(self, mock_sauce):
        assert mock_sauce.get_type() == BunTestData1.sauce_type


    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == BunTestData1.filling_type