class Vendor:
    def __init__(self, name):
        self.name = name


class P2PSystem:
    def __init__(self):
        self.vendors = []
        self.inventory = {}
        self.balance = 10000
        self.current_po = None

    def add_vendor(self):
        name = input("Enter vendor name: ")
        self.vendors.append(Vendor(name))
        print("Vendor added successfully.")

    def show_vendors(self):
        if not self.vendors:
            print("No vendors available.")
            return
        for i, v in enumerate(self.vendors):
            print(f"{i + 1}. {v.name}")

    def create_pr(self):
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        print(f"PR Created: {qty} units of {item}")

    def create_po(self):
        if not self.vendors:
            print("No vendors available. Add vendor first.")
            return

        self.show_vendors()
        choice = int(input("Select vendor: ")) - 1
        vendor = self.vendors[choice]

        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))

        total = qty * price
        self.current_po = {
            "vendor": vendor.name,
            "item": item,
            "qty": qty,
            "price": price,
            "total": total
        }

        print(f"PO Created with {vendor.name} | Total Cost: {total}")

    def goods_receipt(self):
        if not self.current_po:
            print("No PO found.")
            return

        item = self.current_po["item"]
        qty = self.current_po["qty"]

        self.inventory[item] = self.inventory.get(item, 0) + qty
        print(f"Goods Received: {qty} units of {item}")
        print(f"Updated Stock: {self.inventory[item]}")

    def invoice(self):
        if not self.current_po:
            print("No PO found.")
            return
        print(f"Invoice Generated: {self.current_po['total']}")

    def payment(self):
        if not self.current_po:
            print("No PO found.")
            return

        amount = self.current_po["total"]
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of {amount} done to {self.current_po['vendor']}")
            print(f"Remaining Balance: {self.balance}")
            self.current_po = None
        else:
            print("Insufficient balance!")

    def show_inventory(self):
        if not self.inventory:
            print("Inventory empty.")
            return
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}")


def main():
    system = P2PSystem()

    while True:
        print("\n--- P2P SYSTEM MENU ---")
        print("1. Add Vendor")
        print("2. Show Vendors")
        print("3. Create Purchase Requisition (PR)")
        print("4. Create Purchase Order (PO)")
        print("5. Goods Receipt (GR)")
        print("6. Invoice Verification")
        print("7. Payment")
        print("8. Show Inventory")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            system.add_vendor()
        elif choice == '2':
            system.show_vendors()
        elif choice == '3':
            system.create_pr()
        elif choice == '4':
            system.create_po()
        elif choice == '5':
            system.goods_receipt()
        elif choice == '6':
            system.invoice()
        elif choice == '7':
            system.payment()
        elif choice == '8':
            system.show_inventory()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()