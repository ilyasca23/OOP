import unittest
from device import Smartphone
from cart import Cart

class TestStore(unittest.TestCase):

    def test_add_to_cart(self):
        phone = Smartphone("TestPhone", 1000, 5, 12, 6.1, 20)
        cart = Cart()
        cart.add_device(phone, 2)
        self.assertEqual(cart.get_total_price(), 2000)

    def test_reduce_stock(self):
        phone = Smartphone("TestPhone", 1000, 5, 12, 6.1, 20)
        phone.reduce_stock(2)
        self.assertEqual(phone.stock, 3)

if __name__ == "__main__":
    unittest.main()
