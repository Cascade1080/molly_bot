import os

os.system("clear")  # clears the terminal
os.system("cat splash.txt")  # display's 'Molly'

print("Hello Steve!  What can I do for you?")
print("1: Countdown Timer")
print("2: Base64 Encode/Decode")
def menu(t):  # Defines menu class
    t = input("Please select something from the above menu: ")
    if t == '1':
        import countdown
        countdown
    elif t == '2':
        import base64_molly
        base64_molly
    else:
        print("That is not an option")


menu(input)

