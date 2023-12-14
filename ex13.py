# # the argument should be given with the command in powersheell.
# # In other words : python ex13.py orange grape pear
# from sys import argv
#
# # script, first, second, third = argv
# #
# # print("The script is called:", script)
# # print("Your first variable is:", first)
# # print("Your second variable is:", second)
# # print("Your third variable is:", third)

from sys import argv
name, apetizer, soup1, soup2, main_dish, desert = argv

print("Our restaurant name is:", name)
print("The apetizer for the day is:", apetizer)
print("The soup for the day is:", soup1, soup2)
print("Our main dish today is:", main_dish)
print("And ofcourse our best desert is:", desert)

print("What would you like to have?")
apetizer = input("Would you like to try our apetizer or you will skip it ")
soup = input("Would you like to have soupe and which one? ")
main_dish = input("Did you choose your main dish? ")
desert = input("Are you going for desert as well? ")

print(f"So I will repeat your order, you would like to have one {apetizer} for starter, a {soup}, {main_dish} and a {desert}  for deser. Thank you!")
