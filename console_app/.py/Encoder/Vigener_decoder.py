myAlphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя `1234567890-=~!@#$%^&*()_+{}|[]:";<>?,./'
print('Enter "exit", "quit" or "0" to exit from programm. In other case strike any other key.')
while input() != 0:
    print("Enter string for encoding: ")
    inpt = input().lower()
    print("Enter key: ")
    key = input().lower()
    encoded = ""
    i = 1
    for letter in inpt:
        st = myAlphabet.find(letter)
        keyNow = (i % len(key)) - 1
        outpt = myAlphabet[(st + keyNow) % len(myAlphabet)]
        encoded += outpt
        i += 1
    print("Encoded: ///" + encoded + "///")
