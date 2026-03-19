class Cart:
    def __init__(self):
        self.items = {}
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            if device in self.items:
                self.items[device] += amount
            else:
                self.items[device] = amount

            self.total_price += device.price * amount
            print("Added to cart.")
        else:
            print("Not enough stock.")

    def remove_device(self, device, amount):
        if device in self.items:
            if amount >= self.items[device]:
                self.total_price -= device.price * self.items[device]
                del self.items[device]
            else:
                self.items[device] -= amount
                self.total_price -= device.price * amount
            print("Removed from cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n--- Cart ---")
        for device, amount in self.items.items():
            print(f"{device.name} x{amount}")
        print(f"Total: ${self.total_price:.2f}")

    def checkout(self):
        for device, amount in self.items.items():
            if not device.is_available(amount):
                print("Some items are not available.")
                return

        for device, amount in self.items.items():
            device.reduce_stock(amount)

        print("\n--- Receipt ---")
        self.print_items()
        print("Purchase successful!")

        self.items.clear()
        self.total_price = 0
