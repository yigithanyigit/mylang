
TYPE_INTEGER = 'INTEGER'
TYPE_FLOAT = 'FLOAT'

TYPE_PLUS = 'PLUS'
TYPE_MINUS = 'MINUS'
TYPE_DIV = 'DIV'
TYPE_MUL = 'MUL'

TYPE_LPAREN = 'LPAREN'
TYPE_RPAREN = 'RPAREN'

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
        self.current_char = text[self.pos]
        self.current_token = self.get_next_token()
        self.op_list = (TYPE_PLUS, TYPE_MINUS, TYPE_DIV, TYPE_MUL)

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
        
            
            if self.current_char.isspace():
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

            if self.current_char == '*':
                token = Token(TYPE_MUL, None)
                self.advance()
                return token

            if self.current_char == '/':
                token = Token(TYPE_DIV, None)
                self.advance()
                return token

            if self.current_char == '(':
                token = Token(TYPE_LPAREN, None)
                self.advance()
                return token


            if self.current_char == ')':
                token = Token(TYPE_RPAREN, None)
                self.advance()
                return token

 
            self.error()

        return Token(TYPE_EOF, None)
                
        

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if self.current_token.type == TYPE_INTEGER:
            self.eat(TYPE_INTEGER)
            return token.value
        elif self.current_token.type == TYPE_LPAREN:
            self.eat(TYPE_LPAREN)
            result = self.expr()
            self.eat(TYPE_RPAREN)
            return result


    def term(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type in (TYPE_MUL, TYPE_DIV):
            if self.current_token.type == TYPE_MUL:
                self.eat(TYPE_MUL)
                result *= self.factor()
            elif self.current_token.type == TYPE_DIV:
                self.eat(TYPE_DIV)
                result /= self.factor()
 
        return result


    def expr(self):

        result = self.term()
        while self.current_token.type in self.op_list:
            if self.current_token.type == TYPE_PLUS:
                self.eat(TYPE_PLUS)
                result += self.term()
            elif self.current_token.type == TYPE_MINUS:
                self.eat(TYPE_MINUS)
                result -= self.term()

        return result

          
    
