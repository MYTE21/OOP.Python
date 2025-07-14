"""
Step 1: Base Code

This script defines an `Order` class for managing a list of items in a shopping cart,
calculating the total price, and processing payments with basic debit/credit validation.
"""

class Order:
    def __init__(self):
        """
        Initializes an Order object with:
        - items: a list of item names.
        - quantities: a list of quantities corresponding to each item.
        - prices: a list of prices corresponding to each item.
        - status: current status of the order ('open' by default).
        """
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """
        Adds an item to the order.
        Parameters:
            - name (str): The name of the item.
            - quantity (int): The quantity of the item.
            - price (float): The price of a single unit of the item.
        Returns: None.
        """
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        """
        Calculates and returns the total price of all items in the order.
        Parameters: None.
        Returns:
            - total (float): The total price of all items in the order.
        """
        total = 0

        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total

    def pay(self, payment_type: str, security_code: str) -> None:
        """
        Processes the payment and updates the order status to 'paid' if successful.
        Parameters:
            - payment_type (str): The type of payment ('debit' or 'credit').
            - security_code (str): The security code for verification.
        Returns: None.
        Raises:
            Exception: If the payment_type is not recognized.
        """
        if payment_type == "debit":
            print("Processing debit payment type ...")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type ...")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


if __name__ == "__main__":
    # Create an order and add sample items.
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    # Display total cost.
    print(order.total_price())

    # Make a payment.
    order.pay("debit", "0372846")

    # Display updated order status.
    print(order.status)
