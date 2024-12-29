class Caesar:
    def encode(inpt, key):
        myAlphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя `1234567890-=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./'
        i = 1
        for letter in inpt:
            ltr = myAlphabet.find(letter)
            outpt = myAlphabet[(ltr - key) % len(myAlphabet)]
            decoded += outpt
            i += 1
        return decoded