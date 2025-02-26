"""
Use Copilot to improve code coverage. 

1) TODO Rewrite this code to ensure that the OrderProcessor class is structured in a way that makes it easier to test all possible branches and exceptions. This can be achieved by refactoring the code to separate concerns and reduce complexity.

2) TODO Write unit tests for the OrderProcessor class to cover all possible branches and exceptions.
Test cases will include:
- Valid order processing
- Order with no items
- Order with invalid item quantity
- Order with no customer
- Items with different product IDs and prices
"""

class OrderProcessor:
    def process_order(self, order):
        self._validate_order(order)
        self._process_items(order.items)
        self._validate_customer(order.customer)
        self.process_payment(order)

    def _validate_order(self, order):
        if order is None:
            raise ValueError("order cannot be None")
        if not order.items:
            raise ValueError("Order must have at least one item.")

    def _process_items(self, items):
        for item in items:
            self._validate_item(item)
            self._process_item(item)

    def _validate_item(self, item):
        if item.quantity <= 0:
            raise ValueError("Item quantity must be greater than zero.")

    def _process_item(self, item):
        if item.product_id == 0:
            if item.price > 100:
                self._handle_high_value_no_id(item)
            else:
                self._handle_low_value_no_id(item)
        else:
            if item.price > 100:
                self._handle_high_value_with_id(item)
            else:
                self._handle_low_value_with_id(item)

    def _handle_high_value_no_id(self, item):
        print("High value item with no product ID.")

    def _handle_low_value_no_id(self, item):
        print("Low value item with no product ID.")

    def _handle_high_value_with_id(self, item):
        print("High value item with product ID.")

    def _handle_low_value_with_id(self, item):
        print("Low value item with product ID.")

    def _validate_customer(self, customer):
        if customer is None:
            raise ValueError("Order must have a customer.")

    def process_payment(self, order):
        print("Processing payment for order.")


class Order:
    def __init__(self, customer=None, items=None):
        self.customer = customer
        self.items = items if items is not None else []


class Customer:
    def __init__(self, name):
        self.name = name


class OrderItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price