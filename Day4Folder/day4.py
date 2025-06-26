# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day4")
# import random
# for count in range(10):
#     dicevalue = random.randint(1, 9999)
#     print(dicevalue)
########################################################################
# Task 1:



########################################################################
# Task 2:

riddle = "what do you call a 3 deer in 3 herds with three heads?"
hidden = " the thrice of a deer"
guess = input( riddle)
tries = 1
while guess != hidden:
    print("wrong! try again")
    tries = tries + 1
    guess = input( riddle )
else:
    print("you are correct! and you got it after " + str(tries) + " tries.")
########################################################################
# Additional exercises:
import random 