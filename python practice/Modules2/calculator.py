def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b


def main():
    print("calculator says: "+__name__)
    add(2,2)
    sub(2, 2)

if __name__=="__main__":
    main()

else:
    print("calculator says NO " + __name__)


