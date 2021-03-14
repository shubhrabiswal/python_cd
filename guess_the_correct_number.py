#Guess the number
#The main goal of the project is to create a program that randomly 
#select a number in a range then the user has to guess the number. 
#user has three chances to guess the number if he guess correct then 
#a message print saying “you guess right “otherwise a negative message prints.
import random
number = random.randint(1,10)
for i in range(0,3):
  user = int(input("Guess a number \t"))
  if user == number:
    print("Your guess was right")
    print(number)
    break
if user != number:
    print("Your guess was wrong \nThe number is")
    print(number)
