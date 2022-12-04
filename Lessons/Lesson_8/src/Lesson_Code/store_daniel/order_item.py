from src.Lesson_Code.store_daniel.item import Item


class OrderItem(Item):
    def __init__(self, sku: str, quantity: int, price: float, brand: str,
                 model: str,):
        super().__init__(sku, quantity, price, brand, model)
