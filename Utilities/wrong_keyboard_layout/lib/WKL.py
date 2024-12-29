class wkl:
    def switch_layout(inpt):
        eng = "`1234567890-=~!"+'@'+"#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl;'ASDFGHJKL:"+'"'+"zxcvbnm,./ZXCVBNM<>? "
        ru  = "ё1234567890-=Ё!"+'"'+"№;%:?*()_+йцукенгшщзхъЙЦУКЕНГШЩЗХЪфывапролджэФЫВАПРОЛДЖ"+'Э'+"ячсмитьбю.ЯЧСМИТЬБЮ, "
        outpt = ""
        for letter in inpt:
            if letter not in eng:
                outpt += eng[ru.find(letter)%len(ru)]
            else:
                outpt += ru[eng.find(letter)%len(eng)]
        return outpt