def validate_order(order: dict):
    required_fields = ["symbol", "quantity", "price"]

    for field in required_fields:
        if field not in order:
            raise ValueError(f"Missing field: {field}")

    if order["quantity"] <= 0:
        raise ValueError("Quantity must be positive")

    if order["price"] <= 0:
        raise ValueError("Price must be positive")