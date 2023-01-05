from src.Lesson_Code.store_daniel.item import Item


class Product(Item):
    def __init__(self,
                 sku: str,
                 quantity: int,
                 price: float,
                 category: str,
                 brand: str,
                 model: str,
                 warranty_months: int):

        super().__init__(sku, quantity, price, brand, model)

        self.category = category
        self.brand = brand
        self.model = model
        self.warranty_months = warranty_months

    def update_stock(self, diff: int):
        if diff + self.quantity < 0:
            # OutOfStockException
            raise Exception
        self.quantity += 1

    def update_price(self, new_price: float):
        if new_price <= 0:
            # NegativePriceException
            raise Exception
        self.price = new_price

    def __str__(self):
        return f"<Product>: Brand: {self.brand}, Model: {self.model}, SKU: {self.sku}, QTY: {self.get_quantity}"

    def __repr__(self):
        return f"<Product>: SKU: {self.sku}, QTY: {self.qty}"

    def __eq__(self, other):
        return self.sku == other.sku
