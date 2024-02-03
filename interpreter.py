
TYPE_INTEGER = 'INTEGER'
TYPE_FLOAT = 'FLOAT'

TYPE_PLUS = 'PLUS'
TYPE_MINUS = 'MINUS'
TYPE_DIV = 'DIV'
TYPE_MUL = 'MUL'

TYPE_EOF = 'EOF'
TYPE_WHITESPACE = 'WHITESPACE'



class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return f"Token({self.type}: {self.value})"


class Interpreter:
    def __init__(self, text) -> None:
        self.text = text 
        self.pos = 0
        self.current_token = None
        self.current_char = text[self.pos]

    def error(self) -> None:
        raise Exception('Error While Parsing input')


    def advance(self) -> None:
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None

        else:
            self.current_char = self.text[self.pos]
             

    def make_number(self):
        number = ''

        while self.current_char is not None and self.text[self.pos].isdigit() is True:
            number += self.text[self.pos]
            self.advance()

        return number

    def skip_whitespace(self):
        self.advance()

    def get_next_token(self):
        
        while self.current_char is not None:
        
            
            if self.current_char == ' ':
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                number = self.make_number()
                token = Token(TYPE_INTEGER, int(number))
                return token
            
            if self.current_char == '+':
                token = Token(TYPE_PLUS, None)
                self.advance()
                return token

            if self.current_char == '-':
                token = Token(TYPE_MINUS, None)
                self.advance()
                return token

            self.error()

        return Token(TYPE_EOF, None)
                
        

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()


    def expr(self):
        result = Token(TYPE_INTEGER, 0)
        
        self.current_token = self.get_next_token()
        while self.current_token.type is not TYPE_EOF:
            
            left = result if result.value != 0 else self.current_token
            self.eat(TYPE_INTEGER)

            op = self.current_token

            if op.type == TYPE_PLUS:
                self.eat(TYPE_PLUS)
            elif op.type == TYPE_MINUS:
                self.eat(TYPE_MINUS)

            right = self.current_token
            #self.eat(TYPE_INTEGER)

            if op.type == TYPE_PLUS:
                result.value = left.value + right.value
            elif op.type == TYPE_MINUS:
                result.value = left.value - right.value

        return result.value


          
    
