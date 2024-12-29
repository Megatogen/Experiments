eng = "`1234567890-=~!"+'@'+"#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl;'ASDFGHJKL:"+'"'+"zxcvbnm,./ZXCVBNM<>? "
ru  = "ё1234567890-=Ё!"+'"'+"№;%:?*()_+йцукенгшщзхъЙЦУКЕНГШЩЗХЪфывапролджэФЫВАПРОЛДЖ"+'Э'+"ячсмитьбю.ЯЧСМИТЬБЮ, "
print('This utility supports eng, ru layouts, numbers and -=~!@#№$%^&*()_+[]:";'+"'"+'<>?,./ symbols.')
print('Enter "EXIT" or "QUIT" to exit from programm. In other case strike any other key.')
while True:
    inpt = input("Enter string to switch it to other layout: ")
    if inpt=="EXIT" or inpt=="QUIT":
        break
    outpt = ""
    for letter in inpt:
        if letter not in eng:
            outpt += eng[ru.find(letter)%len(ru)]
        else:
            outpt += ru[eng.find(letter)%len(eng)]
    print("Your string on other layout: " + outpt)