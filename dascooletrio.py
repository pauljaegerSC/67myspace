print("Hallo Welt")
print("Hallo Welt")
def addiere(a, b):
    return(a+b)


def ist_gerade(n):
    if n % 2 == 0:
        return(True)
    else:
        return(False)
    
def berüßung(name):
    print(f"Hello {name}!")


def fakultaet(n):
    if n == 0:
        return 1
    else:
        ergebnis = 1
        i = 1
        while i <= n:
            ergebnis *= i
            i += 1
        return ergebnis
    
def ist_palindrom(text):
    umgekerter_text = text[::-1]
    if text.lower() == umgekerter_text.lower():
        return True
    else:
        return False



print(addiere(3, 2))
print(ist_gerade(3))
berüßung("Paul")
print(fakultaet(5))
print(ist_palindrom("jhfhjk"))


was geht yallah
