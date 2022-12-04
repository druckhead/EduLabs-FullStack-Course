from src.Lesson_Code.store_daniel.order_item import OrderItem


class Order:
    def __init__(self, customer_id: str, order_id: str):
        self._customer_id = customer_id
        self._order_id = order_id

        self.cart: dict[str, OrderItem] = {}

    @property
    def get_customer_id(self):
        return self._customer_id

    @property
    def get_order_id(self):
        return self._order_id

    @property
    def get_cart(self):
        return self.cart

    def add_product(self, order_item: OrderItem):
        sku = order_item.get_sku
        self.cart[sku] = order_item

    def get_total_price(self):
        total_price: float = 0
        for order_item in self.cart.values():
            total_price += order_item.get_price * order_item.get_quantity
        return total_price

    def print_cart(self):
        print(self.cart)

    def __str__(self):
        p_str = "ORDER\n"
        p_str += f"Order ID: {self.get_order_id}\n"
        p_str += "Products:\n"
        count = 1
        for item in self.cart.values():
            p_str += f"{count}) {item.get_sku}: {item.get_brand} {item.get_model}\n"
            count += 1
        p_str += f"Order price: {self.get_total_price()}"
        return p_str

    def __repr__(self):
        p_str = "ORDER\n"
        p_str += f"Order ID: {self.get_order_id}\n"
        p_str += "Products:\n"
        count = 1
        for item in self.cart.values():
            p_str += f"{count}. {item.get_sku}\n"
            count += 1
        return p_str
