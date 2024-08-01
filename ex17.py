'''
Coding Exercise 2
We have a list of two IPs in the code area.

Extend the code so your program:

1. Prompts the user to input an index (e.g., 0 or 1).

2. Depending on the user input, the program should return either or You chose 100.122.133.111 You chose 100.122.133.111

Note: In order for the system to mark your exercise as correct, your code should return the exact output (i.e., upper case in and no spaces or other characters after the IP. YYou chose

For example:
Enter the index of the IP you want: 1
You chose 100.122.133.111
'''
ips = ['100.122.133.105', '100.122.133.111']
prompts = input("Enter an index (e.g., 0 or 1: ")
if prompts == "0":
  print(f"You chose {ips[0]}")
else:
  print(f"You chose {ips[1]}")