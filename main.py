
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def times(a,b):
    return a*b

def divided(a,b):
    if b == 0:
        return "Операция недействительна"
    else:
        return a/b
    
def main():
    print("Введите пару целых чисел:")
    print("a = ",end='')
    a = int(input())
    print("b = ",end='')
    b = int(input())
    return

main()