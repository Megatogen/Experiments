class Caesar:
    def encode(inpt, key):
        myAlphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя `1234567890-=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./'
        i = 1
        encoded = ""
        for letter in inpt:
            ltr = myAlphabet.find(letter)
            outpt = myAlphabet[(ltr + key) % len(myAlphabet)]
            encoded += outpt
            i += 1
        return encoded

    def decode(inpt, key):
        myAlphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя `1234567890-=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./'
        i = 1
        decoded = ""
        for letter in inpt:
            ltr = myAlphabet.find(letter)
            outpt = myAlphabet[(ltr - key) % len(myAlphabet)]
            decoded += outpt
            i += 1
        return decoded