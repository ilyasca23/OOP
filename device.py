class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        print(self)

    def __str__(self):
        return (f"{self.name} | ${self.price:.2f} | "
                f"Stock: {self.stock} | Warranty: {self.warranty_period} months")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return (super().__str__() +
                f" | Screen: {self.screen_size}\" | Battery: {self.battery_life}h")

    def make_call(self):
        return "Making a call..."


class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return (super().__str__() +
                f" | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz")

    def run_program(self):
        return "Running program..."


class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return (super().__str__() +
                f" | Resolution: {self.screen_resolution} | Weight: {self.weight}g")

    def browse_internet(self):
        return "Browsing internet..."
