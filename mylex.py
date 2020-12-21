import sys
import ply.lex as lex
reserved = {
    'for':'FOR',
    'loop':'LOOP',
    'else':'ELSE',
    'if':'IF'
}

tokens = ['SQRT','NOTEQ','SMLEQ','LRGEQ','SMALL','LARGE','EQQUAL','COLON','NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN','POWER'
]+list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_POWER = r'\^'
t_SQRT = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_SMALL= r'\<'
t_LARGE = r'\>'
t_EQQUAL = r'\=\='
t_LRGEQ = r'\>\='
t_SMLEQ = r'\<\='
t_NOTEQ = r'\!\='


t_ignore = r' \t'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("integer value too large %s" % t.value)
        t.value = 0
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
lexer.input('')

while True:
    tok =lexer.token()
    if not tok:
        break
    print(tok)


