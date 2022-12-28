from sys import argv
from click import command

from numpy import argsort


class BillCalculator:
    def _init_(self):
        self.products = {}
        self.prices = {
            "TSHIRT": 1000,
            "JACKET": 2000,
            "CAP": 500,
            "NOTEBOOK": 200,
            "PENS": 300,
            "MARKERS": 500
        }
        self.discounts = {
            "TSHIRT": 10,
            "JACKET": 5,
            "CAP": 20,
            "NOTEBOOK": 20,
            "PENS": 10,
            "MARKERS": 5
        }
        self.max_quantities = {
            "TSHIRT": 2,
            "JACKET": 2,
            "CAP": 2,
            "NOTEBOOK": 3,
            "PENS": 3,
            "MARKERS": 3
        }

    def add_item(self, item, quantity):
        if item not in self.products:
            self.products[item] = 0
        self.products[item] += quantity
        if self.products[item] > self.max_quantities[item]:
            self.products[item] -= quantity
            return "ERROR_QUANTITY_EXCEEDED"
        return "ITEM_ADDED"

    def calculate_bill(self):
        total_discount = 0
        total_amount = 0
        for item, quantity in self.products.items():
            price = self.prices[item]
            discount = self.discounts[item]
            total_discount += price * discount * 0.01 * quantity
            total_amount += price * quantity
        if total_amount >= 1000:
            total_discount += total_amount * 5 * 0.01
        total_amount *= 1 + 0.1
        return total_discount, total_amount

    def print_bill(self):
        total_discount, total_amount = self.calculate_bill()
        print("TOTAL_DISCOUNT", total_discount)
        print("TOTAL_AMOUNT_TO_PAY", total_amount)

def main(input_file):
    calculator = BillCalculator()
    with open(input_file, "r") as f:
        for line in f:
            command, *argsort
