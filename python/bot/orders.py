from .validators import validate_order

class OrderManager:
    def __init__(self, client):
        self.client = client

    def create_order(self, order_data: dict):
        validate_order(order_data)
        return self.client.post("orders", order_data)

    def get_orders(self):
        return self.client.get("orders")