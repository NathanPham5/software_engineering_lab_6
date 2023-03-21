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



















if __name__ == "__main__":
    x = True
    while x:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")

        option = int(input("Please enter an option: "))
        if option == 1:
            pass_to_enc = input("Please enter your password to encode: ")
            thing = encode(pass_to_enc)
            print("Your password has been encoded and stored!")
        elif option == 2:
            pass
        elif option == 3:
            break

