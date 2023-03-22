def encode(pass_to_enc):
    encoded_pass = ""
    for i in pass_to_enc:
        i = int(i)
        if i == 7:
            i = "0"
        elif i == 8:
            i = "1"
        elif i == 9:
            i = "2"
        else:
            i += 3
            i = str(i)
        encoded_pass += i
    return encoded_pass


def decode(encoded_pass):
    decoded_pass = ''
    for x in encoded_pass:
        if int(x) >= 3:
            new_val = int(x) - 3
            decoded_pass += str(new_val)
        if int(x) == 2:
            new_val = 9
            decoded_pass += str(new_val)
        if int(x) == 1:
            new_val = 8
            decoded_pass += str(new_val)
        if int(x) == 0:
            new_val = 7
            decoded_pass += str(new_val)
    return decoded_pass


if __name__ == "__main__":
    x = True
    while x:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print('')
        option = int(input("Please enter an option: "))
        if option == 1:
            pass_to_enc = input("Please enter your password to encode: ")
            thing = encode(pass_to_enc)
            print("Your password has been encoded and stored!")
            print('')
        elif option == 2:
            decoded_pass = decode(thing)
            print(f"The encoded password is {thing}, and the original password is {decoded_pass}.")
            print('')
        elif option == 3:
            break
