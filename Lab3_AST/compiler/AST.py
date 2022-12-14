
class Node(object):
    pass


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instructions):
        if hasattr(instructions, '__len__'):
            self.instructions = instructions
        else:
            self.instructions = [instructions]


class Variable(Node):
    def __init__(self, name):
        self.name = name


class Value(Node):
    def __init__(self, value):
        self.value = value


class Operator(Node):
    def __init__(self, op):
        self.op = op


class BinExpr(Node):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right


class UnExpr(Node):
    def __init__(self, value, expr):
        self.value = value
        self.expr = expr


class CompOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Ref(Node):
    def __init__(self, name, val1, val2=None):
        self.name = name
        self.val1 = val1
        self.val2 = val2


class Assign(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class IfElse(Node):
    def __init__(self, condition, if_, else_=None):
        self.condition = condition
        self.if_ = if_
        self.else_ = else_


class For(Node):
    def __init__(self, for_expr, instruction):
        self.for_expr = for_expr
        self.instruction = instruction


class ForExpr(Node):
    def __init__(self, variable, for_range):
        self.variable = variable
        self.range = for_range


class ForRange(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class While(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions


class SysCall(Node):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value # optional, only for 'return value;'


class PrintInputs(Node):
    def __init__(self, inputs):
        if hasattr(inputs, '__len__'):
            self.inputs = inputs
        else:
            self.inputs = [inputs]


class MatrixFun(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Matrix(Node):
    def __init__(self, vectors):
        if hasattr(vectors, '__len__'):
            self.vectors = vectors
        else:
            self.vectors = [vectors]


class Vector(Node):
    def __init__(self, values):
        if hasattr(values, '__len__'):
            self.values = values
        else:
            self.values = [values]
