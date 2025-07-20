from data import BunTestData1, BunTestData2
from conftest import *



class TestBun:

    def test_get_bun_name_check_success(self, mock_bun):

         assert mock_bun.get_name() == BunTestData1.bun_name

    def test_get_bun_price_check_success(self, mock_bun_2):

        assert mock_bun_2.get_price() == BunTestData2.bun_price