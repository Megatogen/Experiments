myAlphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя `1234567890-=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./'
print('Enter "EXIT" or "QUIT" to exit from programm. In other case strike any other key.')
while True:
    print("Enter string for decoding: ")
    inpt = input()
    if inpt=="EXIT" or inpt=="QUIT":
        break
    inpt = inpt.lower()
    print("Enter key: ")
    key = input().lower()
    decoded = ""
    i = 1
    for letter in inpt:
        st = myAlphabet.find(letter)
        keyNow = (i % len(key)) - 1
        outpt = myAlphabet[(st - keyNow) % len(myAlphabet)]
        decoded += outpt
        i += 1
    print("Decoded: ///" + decoded + "///")