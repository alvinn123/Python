# Alvin Nguyen 2055636
# Create a class ItemToPurchase
class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):

        print(self.item_name + " " + str(self.item_quantity) + " @ $"
              + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))


# main function (trying to format for zybooks)
if __name__ == "__main__":

    # print the item 1
    print("Item 1")

    # Object item 1 and 2
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Ask for user input item 1
    item1.item_name = str(input("Enter the item name:\n"))
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nItem 2")

    # Ask for user input item 2
    item2.item_name = str(input("Enter the item name:\n"))
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculate the cost of items
    total = (item1.item_price*item1.item_quantity)+(item2.item_price * item2.item_quantity)

    # Display the total cost
    print("\nTotal: $" + str(total))
