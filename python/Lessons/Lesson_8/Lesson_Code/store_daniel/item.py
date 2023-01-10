class Item:
    def __init__(self, sku: str, quantity: int, price: float, brand: str, model: str):

        self.sku = sku
        self.quantity = quantity
        self.price = price
        self.brand = brand
        self.model = model

    @property
    def get_sku(self) -> str:
        return self.sku

    @property
    def get_quantity(self) -> int:
        return self.quantity

    @property
    def get_price(self) -> float:
        return self.price

    @property
    def get_brand(self) -> str:
        return self.brand

    @property
    def get_model(self) -> str:
        return self.model
