from device import Smartphone, Laptop, Tablet
from cart import Cart

# 20 devices
devices = [
    Smartphone("iPhone 14", 999, 10, 24, 6.1, 20),
    Smartphone("Samsung S23", 899, 8, 24, 6.5, 22),
    Smartphone("Pixel 8", 799, 12, 24, 6.3, 24),
    Smartphone("Xiaomi 13", 699, 15, 24, 6.7, 25),
    Smartphone("OnePlus 11", 750, 10, 24, 6.6, 23),

    Laptop("MacBook Pro", 1999, 5, 12, 16, 3.2),
    Laptop("Dell XPS", 1499, 7, 12, 16, 3.0),
    Laptop("HP Spectre", 1399, 6, 12, 16, 2.9),
    Laptop("Lenovo ThinkPad", 1299, 8, 12, 8, 2.8),
    Laptop("Asus ROG", 1799, 4, 12, 32, 3.5),

    Tablet("iPad Pro", 1099, 6, 18, "2048x1536", 450),
    Tablet("Galaxy Tab S8", 899, 9, 18, "2560x1600", 500),
    Tablet("Surface Go", 799, 7, 18, "1920x1280", 520),
    Tablet("Lenovo Tab", 499, 12, 18, "1920x1200", 480),
    Tablet("Huawei MatePad", 699, 10, 18, "2000x1200", 470),

    Smartphone("Nokia G50", 399, 20, 24, 6.8, 28),
    Laptop("Acer Aspire", 899, 9, 12, 8, 2.5),
    Tablet("Amazon Fire", 299, 15, 12, "1280x800", 400),
    Smartphone("Sony Xperia", 850, 5, 24, 6.4, 21),
    Laptop("MSI Creator", 1899, 3, 12, 32, 3.4),
]

cart = Cart()


def show_devices():
    print("\n--- Available Devices ---")
    for i, device in enumerate(devices):
        print(f"{i+1}. {device}")


while True:
    print("\n====== ELECTRONIC STORE ======")
    print("1. Show Devices")
    print("2. Add Device to Cart")
    print("3. Show Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_devices()

    elif choice == "2":
        show_devices()
        try:
            index = int(input("Select device number: "))
            amount = int(input("Enter quantity: "))
            if 1 <= index <= len(devices):
                cart.add_device(devices[index-1], amount)
            else:
                print("Invalid device number.")
        except:
            print("Invalid input.")

    elif choice == "3":
        cart.print_items()

    elif choice == "4":
        show_devices()
        try:
            index = int(input("Select device number to remove: "))
            amount = int(input("Enter quantity: "))
            if 1 <= index <= len(devices):
                cart.remove_device(devices[index-1], amount)
            else:
                print("Invalid device number.")
        except:
            print("Invalid input.")

    elif choice == "5":
        cart.checkout()

    elif choice == "6":
        print("Thank you for visiting our store!")
        break

    else:
        print("Invalid option.")
