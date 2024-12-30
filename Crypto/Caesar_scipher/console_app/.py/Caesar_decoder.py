myAlphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ `1234567890-=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./'
print('This Caesar decoder supports eng, ru alphabets, space, numbers and -=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./ symbols.')
print('Enter "EXIT" or "QUIT" to exit from programm. In other case strike any other key.')
Y=1
N=0
needToQuit=N
while True:
    inpt = input("Enter string for decoding: ")
    if inpt=="EXIT" or inpt=="QUIT":
        break
    while True:
        try:
            key = input("Enter offset (int): ")
            if inpt=="EXIT" or inpt=="QUIT":
                needToQuit=Y
                break
            key = int(key)
        except Exception:
            print("Incorrect value. Please, enter int.")
        else:
            break
    if needToQuit==Y:
        break

    decoded = ""
    i = 1
    for letter in inpt:
        ltr = myAlphabet.find(letter)
        outpt = myAlphabet[(ltr - key) % len(myAlphabet)]
        decoded += outpt
        i += 1
    print("Decoded: ///" + decoded + "///")
