class Shopping:
    cart = []  # bad use of static variable.

    def add_to_cart(self, item):
        return self.cart.append(item)


if __name__ == "__main__":
    cust1 = Shopping()
    cust1.add_to_cart("Pen")  # Both gets added.
    cust2 = Shopping()
    cust2.add_to_cart("pencil")

    print("Customer 1: ", cust1.cart)
    print("Customer 2: ", cust2.cart)

