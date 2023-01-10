import random

from src.Lesson_Code.store_daniel.customer import Customer
from src.Lesson_Code.store_daniel.order import Order
from src.Lesson_Code.store_daniel.order_item import OrderItem
from src.Lesson_Code.store_daniel.product import Product


class Store:
    def __init__(self, store_name: str):
        self.store_name = store_name

        # id to customer
        self.customers: dict[int, Customer] = {}

        # sku to product
        self.inventory: dict[str, Product] = {}

        # order_id to OrderItem
        self.orders: dict[str, Order] = {}

    def add_customer(self, customer: Customer):
        id_num = customer.get_id_num
        self.customers[id_num] = customer

    def display_customers(self):
        print(self.customers)

    def add_product_to_inventory(self,
                                 sku: str,
                                 quantity: int,
                                 price: float,
                                 category: str,
                                 brand: str,
                                 model: str,
                                 warranty_months: int):
        new_product = Product(sku, quantity, price, category, brand, model, warranty_months)
        self.inventory[sku] = new_product

    def add_quantity_to_product(self, sku: str, quantity: int):
        self.inventory[sku].update_stock(quantity)

    def add_quantity_to_multiple_products(self, skus: list, quantities: list):
        for sku, qty in zip(skus, quantities):
            self.add_quantity_to_product(sku, qty)

    def get_products_by_brand(self, brand: str) -> list[Product]:
        ret_val = list()
        for product in self.inventory.values():
            if product.brand == brand:
                ret_val.append(product)
        return ret_val

    def get_out_of_stock_products(self):
        pass

    def place_order(self, customer_id: str, cart: list[OrderItem]):
        if customer_id not in self.customers:
            # NotACustomerException
            raise Exception
        new_order = Order(customer_id, str(random.randint(111111, 999999)))
        for order_item in cart:
            if self.inventory[order_item.get_sku].get_quantity - order_item.get_quantity < 0:
                # NoStockException
                raise Exception
        for order_item in cart:
            new_order.add_product(order_item)
            self.inventory[order_item.get_sku].quantity -= order_item.get_quantity
        self.orders[new_order.get_order_id] = new_order

    def display_orders(self):
        for item in self.orders.values():
            print(item)
