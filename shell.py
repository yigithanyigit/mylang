from interpreter import Interpreter

def shell():
    while True:
        text = input("shell> ")
        interpre = Interpreter(text)
        res = interpre.expr()
        print(res)



if __name__ == "__main__":
    shell()
