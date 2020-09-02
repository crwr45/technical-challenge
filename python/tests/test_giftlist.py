import unittest

from listmanager.listmanager import Product, GiftList, ListItem


class TestGiftList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.apple = Product(1, "Apple", "", "", 1)
        cls.banana = Product(2, "Banana", "", "", 1)
        cls.cherry = Product(3, "Cherry", "", "", 1)

        cls.forbidden_fruit = Product(99, "Durian", "", "", 1)

        cls.products = {
            "1": cls.apple,
            "2": cls.banana,
            "3": cls.cherry,
        }
        cls.products_keys = [i for i in cls.products.keys()]
        cls.some_products = {
            "1": cls.apple,
            "2": cls.banana,
        }
        cls.some_products_keys = [i for i in cls.some_products.keys()]

    def setUp(self):
        self.emptylist = GiftList(self.products_keys, {})
        self.fulllist = GiftList(self.products_keys,
                                {k: ListItem(prod)
                                 for k, prod 
                                 in self.products.items()})

    def test_add_entry(self):
        testlist = self.emptylist
        testlist.add_entry(self.apple)
        self.assertEqual(len(testlist.giftlist), 1)
        with self.assertRaises(PermissionError):
            testlist.add_entry(self.forbidden_fruit)
        with self.assertRaises(ValueError):
            testlist.add_entry(self.apple)

    def test_remove_entry(self):
        testlist = self.fulllist
        testlist.remove_entry(self.apple)
        self.assertEqual(len(testlist.giftlist), 2)
        with self.assertRaises(KeyError):
            testlist.remove_entry(self.apple)
        testlist.purchase_entry(self.banana)
        with self.assertRaises(ValueError):
            testlist.remove_entry(self.banana)

    def test_purchase_entry(self):
        testlist = self.fulllist
        testlist.purchase_entry(self.apple)
        self.assertTrue(testlist.giftlist["1"].purchased)
        with self.assertRaises(KeyError):
            testlist.purchase_entry(self.forbidden_fruit)
        with self.assertRaises(ValueError):
            testlist.purchase_entry(self.apple)

    def test_product_id_is_allowed(self):
        testlist = self.emptylist
        self.assertTrue(testlist.product_id_is_allowed(str(self.apple.id)))
        self.assertFalse(testlist.product_id_is_allowed(str(self.forbidden_fruit.id)))
        unrestrictedlist = GiftList([], {})
        self.assertTrue(unrestrictedlist.product_id_is_allowed(str(self.forbidden_fruit.id)))
    
    def test_get_purchased_items(self):
        testlist = self.fulllist
        testlist.purchase_entry(self.apple)
        self.assertListEqual(testlist.get_purchased_items(), [self.apple])
    
    def test_get_unpurchased_items(self):
        testlist = self.fulllist
        testlist.purchase_entry(self.apple)
        self.assertListEqual(testlist.get_unpurchased_items(), [self.banana, self.cherry])
