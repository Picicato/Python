class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {budget_category.category}')
            budget_category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
  spent_dict = {}
  for category in categories:
    total_spent = 0 
    for transaction in category.ledger:
      if transaction['amount'] < 0:
        total_spent += abs(transaction['amount'])
    spent_dict[category.category] = round(total_spent, 2)
  
  total = sum(spent_dict.values())
  percent_dict = {}
  for category_name in spent_dict.keys():
    percent_dict[category_name] = int(round(spent_dict[category_name] / total, 2) * 100)
  
  output = 'Percentage spent by category\n'
  
  # Vertical chart (from 100 to 0 in steps of 10)
  for i in range(100, -10, -10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percent_dict.values():
      if percent >= i:
        output += 'o  '
      else:
        output += '   '
    output += '\n' 
  
  # Horizontal line
  output += ' ' * 4 + '-' * (len(percent_dict.values()) * 3 + 1)
  output += '\n     '
  
  # Maximum length of category names
  category_names = list(percent_dict.keys())
  max_len_category = max([len(name) for name in category_names])
  
  # Print the category names vertically
  for i in range(max_len_category):
    for name in category_names:
      if len(name) > i:
        output += name[i] + '  '
      else:
        output += '   '
    if i < max_len_category - 1:
      output += '\n     '
    
  return output


# Test the code with the given categories
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(20, 'clothing purchase')

auto = Category('Auto')
auto.withdraw(50, 'gas')

# Print the chart with the new "Auto" category
print(create_spend_chart([food, clothing, auto]))


