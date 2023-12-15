from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# here we define the file and we work with the information in it by using the function open()
target = open(filename, 'w')
#using function .truncate() we empty the file / erase the information.
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# using the function  .write()  we isnert the new information that we want to be saved in the file
target.write(f"{line1}\n{line2}\n{line3}")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
#it is important to use the function .close() to actually save and close the file.
target.close()
