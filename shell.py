from interpreter import Interpreter, Lexer

def shell():
    while True:
        text = input("shell> ")
        lexer = Lexer(text)
        interpre = Interpreter(lexer)
        res = interpre.expr()
        print(res)



if __name__ == "__main__":
    shell()
