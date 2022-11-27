#!/usr/bin/python

import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ("left", 'ADD', 'SUB'),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : program block
               | block"""


def p_block(p):
    """block : LCURLBRACK block RCURLBRACK
             | block instruction
             | instruction
             | empty"""


def p_empty(p):
    """empty :"""
    pass


def instruction(p):
    """instruction : assignment
                   | call
                   | loop
                   | branch"""


parser = yacc.yacc()
