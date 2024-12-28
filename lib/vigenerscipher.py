class Vigener():
    def encode(self, inpt, key="a"):
        myAlphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя `1234567890-=~!@#$%^&*()_+{}|[]\:";<>?,./'
        inpt = inpt.lower()
        key = key.lower()
        encoded = ""
        i = 1
        for letter in inpt:
            st = myAlphabet.find(letter)
            keyNow = (i % len(key)) - 1
            outpt = myAlphabet[(st + keyNow) % len(myAlphabet)]
            encoded += outpt
            i += 1
        return encoded