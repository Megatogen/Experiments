myAlphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ `1234567890-=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./'
print('This Vigener decoder supports eng, ru alphabets, space, numbers and -=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./ symbols.')
print('Enter "EXIT" or "QUIT" to exit from programm. In other case strike any other key.')
while True:
    inpt = input("Enter string for decoding: ")
    if inpt=="EXIT" or inpt=="QUIT":
        break
    key = input("Enter key: ")
    if key=="EXIT" or key=="QUIT":
        break
    decoded = ""
    i = 1
    for letter in inpt:
        st = myAlphabet.find(letter)
        keyNow = (i % len(key)) - 1
        outpt = myAlphabet[(st - keyNow) % len(myAlphabet)]
        decoded += outpt
        i += 1
    print("Decoded: ///" + decoded + "///")