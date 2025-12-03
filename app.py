alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(text, shiftamount, direction):
    finaltext = ""

    if direction == "decode":
        shiftamount = shiftamount * -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            newposition = position + shiftamount
            finaltext += alphabet[newposition]
        else:
            finaltext += char

    print(f"{direction}ed message is {finaltext}")

isend = False
while not isend:
    direction = input("Enter encode or decode: ")
    message = input("Enter a message: ")
    shift = int(input("Enter the shift number: "))
    shift = shift % 26

    caesar(message, shift, direction)

    restart = input("Do you wanna play: yes or no: ")
    if restart == "no":
        isend = True
        print("Thank you!")