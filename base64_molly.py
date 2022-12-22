#import base64
import base64
print("1: Encode")
print("2: Decode")
t = input("Select from the above: ")

if t == '1':
    msgE = input("Data to be encoded: ")
    encB = msgE.encode('ASCII')  # Takes input and encodes in to a byte format
    enc = base64.b64encode(encB)  # Takes byte formatted message and converts it to base64
    print(enc)
elif t == '2':
    msgD = input("Data to be decoded: ")
    decB = msgD.encode('ASCII')
    dec = base64.b64decode(decB)
    print(dec)
else:
    print("That is not an option.")

