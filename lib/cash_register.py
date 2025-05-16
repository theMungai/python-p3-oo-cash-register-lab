#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction_amount = 0

  def add_item(self, item, price, quantity = 1):
    self.total += (price * quantity)
    self.items.extend([item] * quantity)
    self.last_transaction_amount = price * quantity

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    self.last_transaction_amount = 0

cash_register = CashRegister()
cash_register.add_item("eggs", 90, 3)
cash_register.add_item("fish", 60)
cash_register.add_item("bacon", 50)
