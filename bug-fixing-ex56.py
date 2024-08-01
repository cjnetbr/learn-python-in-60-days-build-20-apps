menu = ["pasta", "pizza", "salad"]

user_choice = input("Enter the index of the item: ")

message = f"You chose {menu[int(user_choice)]}."
print(message)

'''
Bug-Fixing Exercise 2
Here is another piece of buggy code:

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate[menu]:
    print(f"{i}.{j}")

Fix the code, so it prints out the output below:

0.pasta
1.pizza
2.salad
'''
menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
  print(f"{i}.{j}")

'''
Here is another piece of code that contains a bug:

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print("f{i}.{j}")
The expected output is this:

0.pasta
1.pizza
2.salad
Fix the bug so the program prints out the above output.
'''

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")