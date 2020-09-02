import json
import jsonpickle
from typing import List, Dict

import click
import click_log
from tabulate import tabulate

from .listmanager import GiftList, Product



def products_from_file(filepath=None) -> List[Product]:
    if filepath is None:
        return {}
    with open(filepath, "r") as json_file:
        res = json.load(
            json_file,
            object_hook=lambda p: Product(**p)
        )
    return {str(prod.id): prod for prod in res}


def giftlist_from_file(filepath: str, allowed_products: Dict[str, Product]) -> GiftList:
    allowed_product_ids = [str(k) for k in allowed_products.keys()]
    with open(filepath, "r") as json_file:
        giftlist = jsonpickle.decode(json_file.read())
    return GiftList(allowed_product_ids, giftlist)

def giftlist_to_file(filepath: str, giftlist: GiftList):
    with open(filepath, "w") as json_file:
        json_file.write(jsonpickle.encode(giftlist.giftlist))





@click.group()
@click.option("--list_file", type=click.Path(exists=True), default="/home/charlie/technical-challenge/giftlist.json")
@click.pass_context
def cli(ctx, list_file):
    ctx.ensure_object(dict)
    ctx.obj["list_file"] = list_file


@cli.command()
@click.option("--product_file", type=click.Path(exists=True))
@click.argument("product_id", type=str)
@click.pass_context
def add(ctx, product_file, product_id):
    """Add an item to the gift list"""
    giftlist_file = ctx.obj['list_file']
    products = products_from_file(product_file)
    giftlist = giftlist_from_file(giftlist_file, products)

    print(product_id)
    print(products)

    product = products.get(product_id)
    if product is None:
        raise ValueError(f"product {product_id} does not exist")
    giftlist.add_entry(product)
    giftlist_to_file(giftlist_file, giftlist)


@cli.command()
@click.option("--product_file", type=click.Path(exists=True))
@click.argument("product_id", type=str)
@click.pass_context
def remove(ctx, product_file, product_id):
    """Remove an item from the gift list"""
    giftlist_file = ctx.obj['list_file']
    products = products_from_file(product_file)
    giftlist = giftlist_from_file(giftlist_file, products)

    product = products.get(product_id)
    if product is None:
        raise ValueError(f"product {product_id} does not exist")
    giftlist.remove_entry(product)
    giftlist_to_file(giftlist_file, giftlist)


@cli.command()
@click.option("--product_file", type=click.Path(exists=True))
@click.argument("product_id", type=str)
@click.pass_context
def purchase(ctx, product_file, product_id):
    """Mark an item in the gift list as purchased"""
    giftlist_file = ctx.obj['list_file']
    products = products_from_file(product_file)
    giftlist = giftlist_from_file(giftlist_file, products)

    product = products.get(product_id)
    if product is None:
        raise ValueError(f"product {product_id} does not exist")
    giftlist.purchase_entry(product)
    giftlist_to_file(giftlist_file, giftlist)


@cli.command()
@click.pass_context
def listitems(ctx):
    """List all items in the gift list, with their code."""
    giftlist_file = ctx.obj['list_file']
    giftlist = giftlist_from_file(giftlist_file, {})
    
    table = [[entry.product.id, entry.product.name] for entry in giftlist.giftlist.values()]
    print(f"Displaying all items in {giftlist_file}")
    print(tabulate(table))


@cli.command()
@click.pass_context
def status(ctx):
    """Display a report of purchased and unpurchased items."""
    giftlist_file = ctx.obj['list_file']
    giftlist = giftlist_from_file(giftlist_file, {})
    
    purchased = [[prod.id, prod.name] for prod in giftlist.get_purchased_items()]
    unpurchased = [[prod.id, prod.name] for prod in giftlist.get_unpurchased_items()]

    print(f"Displaying status of items in {giftlist_file}")
    print("Purchased items:")
    print(tabulate(purchased))
    print("Unpurchased items:")
    print(tabulate(unpurchased))


if __name__ == "__main__":
    cli(obj={})
