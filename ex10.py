'''
The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.

Your task is to create a program that:

1. Contains the above list.

2. Prompts the user to input a rank number.

3. Returns the person who has the given rank.



For example:
Enter rank number: 2
Sen

'''
ranking = ['John', 'Sen', 'Lisa']
while True:
  rank = int(input("Enter rank number or 0 for exit: "))
  match rank:
    case 1:
      print(ranking[0])
    case 2:
      print(ranking[1])
    case 3:
      print(ranking[2])
    case 0:
      break