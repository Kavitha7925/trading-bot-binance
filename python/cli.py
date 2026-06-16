from bot.client import APIClient
from bot.orders import OrderManager
from bot.logging_config import setup_logger

def main():
    logger = setup_logger()

    client = APIClient("https://api.example.com")
    order_manager = OrderManager(client)

    sample_order = {
        "symbol": "AAPL",
        "quantity": 10,
        "price": 150
    }

    try:
        response = order_manager.create_order(sample_order)
        logger.info(f"Order created: {response}")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()