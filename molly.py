import os
os.system("clear")  # clears the terminal

print("Hello Steve!  What can I do for you?")
print("1: Countdown Timer")
def menu(t):  # Defines menu class
    t = input("Please select something from the above menu: ")
    if t == '1':
        import countdown
        countdown
    else:
        print("That is not an option")


menu(input)

