try:
    import time as timeUtil
    import random as rnd
except:
    class NoLibError(Exception):
        pass
    raise NoLibError("Any libs not found. You need to install ALL dependencies.")
def typeWrite(*strings: str, time: float=0, speed: float=1) -> None:
    """
    Выводит в консоль строки *strings за время time.
    Args:
        *strings (str) : То, что необходимо вывести в консоль.
        time (float) : Время в секундах.
        speed (float) : Скорость в символах в секунду. При указании time данный аргумент игнорируется.
    Returns:
        None
    """
    if strings:
        length = 0
        for str in strings:
            length += len(str)
        if time:
            timeForLetter = time/length
        elif speed:
            timeForLetter = 1/speed
        longString = ""
        for str in strings:
            longString += str
        for letter in longString:
            print(letter, end="", flush=True)
            timeUtil.sleep(timeForLetter)
        print()

def randomSpawnWrite(*strings: str, time: float=0, speed: float=1) -> None:
    """
    Выводит в консоль строки *strings за время time.
    Args:
        *strings (str) : То, что необходимо вывести в консоль.
        time (float) : Время в секундах.
        speed (float) : Скорость в символах в секунду. При указании time данный аргумент игнорируется.
    Returns:
        None
    """
    if strings:
        length = 0
        for str in strings:
            length += len(str)
        if time:
            timeForLetter = time/length
        elif speed:
            timeForLetter = 1/speed
        
        dataStr = ""
        outStr = ""

        for str in strings:
            for ltr in str:
                dataStr += ltr
        
        for ltr in dataStr:
            if ltr=="\n":
                outStr += "\n"
            else:
                outStr += " "
        
        printed = []
        for i in range(len(dataStr)):
            rand = rnd.randint(0, len(dataStr)-1)
            while rand in printed:
                rand = rnd.randint(0, len(dataStr)-1)
            outStr=outStr[:rand]+dataStr[rand]+outStr[rand+1:]
            printed.append(rand)
            if i != 0:
                ncount = outStr.count("\n")
                print("\r"+"\033[A"*ncount, end="")
            for ltr in outStr:
                print(ltr, end="", flush=True)
            if timeForLetter >= 0.01:
                timeUtil.sleep(timeForLetter)
            else:
                pass
        print()
if __name__ == "__main__":
    randomSpawnWrite("Хоп, хэй, лала лэй", "\nЙомайо", time = 5)