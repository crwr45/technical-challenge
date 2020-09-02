#!/usr/bin/env python3
from collections import namedtuple
from dataclasses import dataclass
from typing import List, Dict


# Wraps a product as defined in "products.json". Only `id` and `name` are used.
Product = namedtuple("Product", ["id", "name", "brand", "price", "in_stock_quantity"])


@dataclass
class ListItem:
    # A complete product record.
    product: Product

    # Records if this entry has been purchased or not.
    purchased: bool = False


@dataclass
class GiftList:
    """
    A very simple Gift List.
    Each product can appear only once, and quantity cannot be set.
    There is no interface provided for updating allowed products once they are set.
    There is no way to "un-purchase" an item.
    """

    # a list of IDs that are allowed to be added to the list. Will not remove existing gift items if changed.
    allowed_product_ids: List[str]

    # The list itself. Keys are the string product ID.
    giftlist: Dict[str, ListItem]

    def add_entry(self, product: Product):
        product_id = str(product.id)
        if not self.product_id_is_allowed(product_id):
            raise PermissionError(f"Product {product_id} is not allowed in this gift list")
        if product_id in self.giftlist.keys():
            raise ValueError(f"Product {product_id} cannot be in the same list twice")

        self.giftlist[product_id] = ListItem(product, False)
    
    def remove_entry(self, product: Product):
        product_id = str(product.id)
        current_entry = self.giftlist.get(product_id)
        if current_entry is None:
            raise KeyError(f"Product {product_id} is not in the gift list")
        if current_entry.purchased:
            raise ValueError(f"Cannot remove product {product_id} as it has aready been purchased")

        del self.giftlist[product_id]

    def purchase_entry(self, product: Product):
        product_id = str(product.id)
        current_entry = self.giftlist.get(product_id)
        if current_entry is None:
            raise KeyError(f"Product {product_id} is not in the gift list")
        if current_entry.purchased:
            raise ValueError(f"Cannot purchase product {product_id} as it has aready been purchased")

        current_entry.purchased = True
    
    def product_id_is_allowed(self, product_id: str):
        if self.allowed_product_ids == []:
            return True
        return product_id in self.allowed_product_ids
    
    def get_purchased_items(self) -> List[Product]:
        return [entry.product for entry in self.giftlist.values() if entry.purchased]
    
    def get_unpurchased_items(self) -> List[Product]:
        return [entry.product for entry in self.giftlist.values() if not entry.purchased]


