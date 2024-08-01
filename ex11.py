'''
Coding Exercise 3
We have defined the same ranking list as in the previous exercise:

This time you should create a program that:

1. Contains the above list.

2 Prompts the user to input the person's name.

3. Returns the rank that person has.

For example:
Enter a name: Sen
2
'''
ranking = ['John', 'Sen', 'Lisa']
while True:
  rank = input("Enter a name or 0 for exit: ")
  match rank:
    case "John":
      print(ranking.index(rank) + 1)
    case "Sen":
     print(ranking.index(rank) + 1)
    case "Lisa":
      print(ranking.index(rank) + 1)
    case "0":
      break