from src.Lesson_Code.store_daniel.customer import Customer
from src.Lesson_Code.store_daniel.order_item import OrderItem
from src.Lesson_Code.store_daniel.store import Store

if __name__ == "__main__":
    print()
    ksp = Store("KSP")
    ksp.add_customer(Customer("LeBron James", "Cleveland", "2098384", "1-555-888-222"))
    ksp.add_customer(Customer("Michael Jordan", "Chicago", "20873451", "1-777-121-987"))

    # print(ksp.customers["2098384"])

    ksp.display_customers()
    print()

    ksp.add_product_to_inventory("A1234", 5, 8000, "Laptops", "Apple", "Macbook Pro 14-inch", 36)
    ksp.add_product_to_inventory("A4321", 8, 14000, "Laptops", "Apple", "Macbook Pro 16-inch", 2)

    print(ksp.inventory["A1234"])
    print(ksp.inventory["A4321"])
    print()

    ksp.place_order("2098384", [OrderItem("A1234", 1, 8000, "Apple", "MacbookPro 14-inch"),
                                OrderItem("A4321", 1, 14000, "Apple", "MacbookPro 16-inch")])
    ksp.display_orders()

    # for order in ksp.orders.values():
    #     print(order.get_total_price())