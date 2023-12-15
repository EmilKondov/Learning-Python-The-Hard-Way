# On line 2 and 4 we are actually setting argument value which should be entered from the user while initiating the program
# from sys import argv
#
# script, filename = argv
filename = input()
# On line 6 we use the function open() in order to set a value for the variable txt whcih is te content of the file that we are opening.
txt = open(filename)
#Here we print a simple strin with variable
print(f"Here's your file {filename}:")
#Here we actually prin the content of the file which we assigned earlier as a value of the variable txt. Now we say "Hey text do you read function in other word to yourself .. () when no specific argument."
print(txt.read())


#Here we just repeat the same asking the user to enter the name of the file again and then use .read() again
# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
# print(txt_again.read())
