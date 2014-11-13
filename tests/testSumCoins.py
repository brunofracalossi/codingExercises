from unittest import TestCase
from impl.sumCoins import sumCoins


class TestCoinsSum(TestCase):

    def test_simplest_sum(self):
        coins = [1, 3, 5]
        self.assertEquals(0, sumCoins(coins).getMinCoins(0))

    def test_simple_sum_1(self):
        coins = [1, 3, 5]
        self.assertEquals(1, sumCoins(coins).getMinCoins(3))

    def test_simple_sum_2(self):
        coins = [1, 3, 5]
        self.assertEquals(2, sumCoins(coins).getMinCoins(4))

    def test_simple_sum_3(self):
        coins = [1, 3, 5]
        self.assertEquals(3, sumCoins(coins).getMinCoins(11))

    def test_simple_sum_4(self):
        coins = [1, 3, 5, 11]
        self.assertEquals(1, sumCoins(coins).getMinCoins(11))

    def test_simple_sum_5(self):
        coins = [1]
        self.assertEquals(42, sumCoins(coins).getMinCoins(42))