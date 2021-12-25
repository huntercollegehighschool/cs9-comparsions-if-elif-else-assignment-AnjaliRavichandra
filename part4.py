'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below
first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))

if first_number > 0 and second_number > 0:
  print("positive")
elif first_number < 0 and second_number < 0:
  print("negative")
elif first_number > 0 and second_number < 0:
  print("opposite")
elif first_number < 0 and second_number > 0:
  print("opposite")
elif first_number == 0 or second_number == 0:
  print("zero")