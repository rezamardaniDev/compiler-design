import ply.lex as lex

class LEXER:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'ID',
        'ASSIGN',
        'LBRACKET',
        'RBRACKET',
        'LT',
        'GT',
        'LE',
        'GE',
        'NE',
        'EQUAL',
        'SEMICOL',
        'STRING',
    ]

    reserved = {
        'elif': 'ELIF',
        'else': 'ELSE',
        ':': 'TWOP',
        'ashar': 'FLOAT',
        'sahih': 'INT',
        'agar': 'IF',
        'chap': 'PRINT',
        'begir': 'INPUT',
        'class': 'CLASS',
        'void': 'VOID'
    }

    tokens = tokens + list(reserved.values())

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    
    def t_ID(self, t):
        r':|[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_NOT(self, t):
        r'not'
        t.type = self.reserved.get(t.value, 'NOT')
        return t

    def t_EQUAL(self, t):
        r'=='
        t.type = self.reserved.get(t.value, 'EQUAL')
        return t

    def t_GE(self, t):
        r'>='
        t.type = self.reserved.get(t.value, 'GE')
        return t

    def t_LE(self, t):
        r'<='
        t.type = self.reserved.get(t.value, 'LE')
        return t

    def t_NE(self, t):
        r'!='
        t.type = self.reserved.get(t.value, 'NE')
        return t

    def t_LT(self, t):
        r'<'
        t.type = self.reserved.get(t.value, 'LT')
        return t

    def t_GT(self, t):
        r'>'
        t.type = self.reserved.get(t.value, 'GT')
        return t

    def t_SEMICOL(self, t):
        r';'
        t.type = self.reserved.get(t.value, 'SEMICOL')
        return t

    def t_STRING(self, t):
        r'"[a-zA-Z]*"'
        t.type = self.reserved.get(t.value, 'STRING')
        return t

    def t_ASSIGN(self, t):
        r'='
        t.type = self.reserved.get(t.value, 'ASSIGN')
        return t

    def t_LRACKET(self, t):
        r'{'
        t.type = LEXER.reserved.get(t.value, 'LBRACKET')
        return t

    def t_RBRACKET(self, t):
        r'}'
        t.type = LEXER.reserved.get(t.value, 'RBRACKET')
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    @staticmethod
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    @staticmethod
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def append_multiple_lines(self, file_name, lines_to_append):
        with open(file_name, "a+") as file_object:
            appendEOL = False
            file_object.seek(0)

            data = file_object.read(100)
            if len(data) > 0:
                appendEOL = True
            for line in lines_to_append:
               
                if appendEOL == True:
                    file_object.write("\n")
                else:
                    appendEOL = True
                
                file_object.write(line)

    def read_input_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.read().rstrip()
        return data

    def test(self):
       
        with open("output.txt", 'r+') as f:
            f.truncate(0)

        input_data = self.read_input_file('input.txt')

        self.lexer.input(input_data)

        TOKENS = []
        while True:
            addedData = ""
            tok = self.lexer.token()
            if tok != None:
                print(tok)
            if not tok:
                break  
            addedData = tok.type + "  " + str(tok.value)
            TOKENS.append(addedData)

        self.append_multiple_lines("output.txt", TOKENS)

lexer = LEXER()
lexer.test()