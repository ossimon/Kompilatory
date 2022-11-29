#!/usr/bin/python

import scanner
import ply.yacc as yacc
import numpy as np

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'IF'),
    ('nonassoc', 'SMALLER', 'LARGER', 'SMALLEREQ', 'LARGEREQ', 'NOTEQ', 'EQ', 'ELSE'),
    ('left', 'ADD', 'SUB', 'DOTADD', 'DOTSUB'),
    ('left', 'MUL', 'DIV', 'DOTMUL', 'DOTDIV'),
    ('left', 'UMINUS'),
    ('right', 'TRANSPOSE') # ????
)

start = 'program'
error = False


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")
    error = True


def p_program(p):
    """program : instructions"""


def p_instructions(p):
    """instructions : instructions instruction
                    | instruction"""


def p_instruction(p):
    """instruction : assignment SEMICOLON
                   | call SEMICOLON
                   | loop
                   | branch
                   | LCURLBRACK instructions RCURLBRACK"""


def p_assignment(p):
    """assignment : ID assignment_operator expression
                  | ID matrix assignment_operator expression"""


def p_assignment_operator(p):
    """assignment_operator : ASSIGN
                           | ADDASSIGN
                           | SUBASSIGN
                           | MULASSIGN
                           | DIVASSIGN"""


def p_expression(p):
    """expression : term
                  | LPARENT expression RPARENT"""


def p_num_expression_binary(p):
    """expression : expression ADD expression %prec ADD
                  | expression SUB expression %prec SUB
                  | expression MUL expression %prec MUL
                  | expression DIV expression %prec DIV
                  | expression DOTADD expression %prec ADD
                  | expression DOTSUB expression %prec SUB
                  | expression DOTMUL expression %prec MUL
                  | expression DOTDIV expression %prec DIV"""


def p_expression_negation(p):
    """expression : SUB expression %prec UMINUS"""


def p_expression_transpose(p):
    """expression : expression TRANSPOSE"""
    p[0] = np.transpose(p[1])


def p_comparison(p):
    """comparison : expression comparison_operator expression"""


def p_comparison_operator(p):
    """comparison_operator : SMALLER
                          | LARGER
                          | SMALLEREQ
                          | LARGEREQ
                          | NOTEQ
                          | EQ"""


def p_call(p):
    """call : BREAK
            | CONTINUE
            | RETURN expression
            | PRINT print_inputs"""


def p_print_inputs(p):
    """print_inputs : print_inputs COMMA print_input
                    | print_input"""


def p_print_input(p):
    """print_input : STRING
                   | ID"""


def p_matrix_fun(p):
    """matrix_fun : fun_name LPARENT expression RPARENT"""


def p_fun_name(p):
    """fun_name : EYE
                | ZEROS
                | ONES"""


def p_loop(p):
    """loop : for
            | while"""


def p_for(p):
    """for : FOR for_expression instruction"""


def p_for_expression(p):
    """for_expression : ID ASSIGN range"""


def p_while(p):
    """while : WHILE LPARENT comparison RPARENT instruction"""


def p_branch(p):
    """branch : IF LPARENT comparison RPARENT instruction %prec IF
              | IF LPARENT comparison RPARENT instruction ELSE instruction"""


def p_range(p):
    """range : num_term COLON num_term"""


def p_term(p):
    """term : ID
            | number
            | matrix
            | string"""


def p_num_term(p):
    """num_term : ID
                | number"""


def p_number(p):
    """number : INT
              | FLOAT"""


def p_string(p):
    """string : STRING"""


def p_matrix(p):
    """matrix : LSQBRACK vectors RSQBRACK
              | vector
              | matrix_fun"""


def p_vectors(p):
    """vectors : vectors COMMA vector
               | vector"""


def p_vector(p):
    """vector : LSQBRACK numbers RSQBRACK"""


def p_vector_contents(p):
    """numbers : numbers COMMA number
               | num_term"""


parser = yacc.yacc()
