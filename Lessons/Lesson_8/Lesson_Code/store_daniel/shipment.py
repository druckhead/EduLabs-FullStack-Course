class Shipment:

    STATUS = ('Processing', 'Shipped', "Delivered")
    counter = 0

    def __init__(self, address: str):
        self.address = address
        self.status = 0
        Shipment.counter += 1

    def update_shipment(self):
        if self.status == len(Shipment.STATUS) - 1:
            # ShipmentArrivedException
            raise Exception
        self.status += 1
