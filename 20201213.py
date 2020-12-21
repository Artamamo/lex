import ply.yacc as yacc
import math
from mylex import tokens
names = {}
def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]
def p_statement_for(p):
    '''statement : FOR NAME LOOP NUMBER NUMBER COLON NAME EQUALS NAME PLUS NUMBER
                 | FOR NAME LOOP NUMBER NUMBER COLON NAME EQUALS NAME MINUS NUMBER
                 | FOR NAME LOOP NUMBER NUMBER COLON NAME EQUALS NAME TIMES NUMBER
                 | FOR NAME LOOP NUMBER NUMBER COLON NAME EQUALS NAME DIVIDE NUMBER
                 | FOR NAME LOOP NUMBER NUMBER COLON NAME EQUALS NAME POWER NUMBER
                 | FOR NAME LOOP NUMBER NUMBER COLON NAME EQUALS NAME SQRT NUMBER'''
    for p[2] in range(p[4],p[5]):
        if p[10] == '+':
            names[p[7]] = names[p[9]] + p[11]
        elif p[10] == '-':
            names[p[7]] = names[p[9]] - p[11]
        elif p[10] == '*':
            names[p[7]] = names[p[9]] * p[11]
        elif p[10] == '/':
            names[p[7]] = names[p[9]] * p[11]
        elif p[10] == '^':
            names[p[7]] = names[p[9]] * p[11]
        elif p[10] == '**':
            names[p[7]] = names[p[9]] * p[11]
        
def p_statement_if(p):
    '''
    statement : IF comparison COLON NAME EQUALS expression 
              | IF comparison COLON NAME EQUALS expression ELSE COLON NAME EQUALS expression
    '''
    if p[2]:
        names[p[4]] = p[6]
    else:
        try:
            if p[11] is not None:
                names[p[9]]=p[11]
        except:
            pass
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
def p_term_power(p):
    'term : term POWER factor'
    p[0] = pow(p[1],p[3])
def p_term_cuberoot(p):
    'term : term SQRT factor'
    p[0] = pow(p[1],1/p[4])
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
def p_assign(p):
    'factor : NAME EQUALS factor'
    names[p[1]]=p[3]
def p_name(p): 
    'factor : NAME'   
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        

def p_comparison(p):
    '''comparison : factor EQQUAL factor
                  | factor NOTEQ factor
                  | factor LARGE factor
                  | factor SMALL factor 
                  | factor LRGEQ factor 
                  | factor SMLEQ factor
            '''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]


def p_error(p):
    print("Syntax error in input!")
    
parser=yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
