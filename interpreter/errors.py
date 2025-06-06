from dataclasses import dataclass

@dataclass
class CompilationError:
    line: int
    column: int
    msg: str

    def __str__(self):
        return f"(line {self.line}, column {self.column}) {self.msg}"


# compile time
class DeclarationException(Exception):
    def __init__(self, message, line, column):            
        self.msg = message
        self.line = line
        self.column = column


class ReturnException(Exception):
    def __init__(self, message, line, column):            
        self.msg = message
        self.line = line
        self.column = column


class TypeException(Exception):
    def __init__(self, message, line, column):            
        self.msg = message
        self.line = line
        self.column = column

###
# runtime
###

class IndexOutOfBoundsException(Exception):
    def __init__(self, message, line, column):            
        self.msg = message
        self.line = line
        self.column = column


class ZeroDivisionException(Exception):
    def __init__(self, message, line, column):
        self.msg = message
        self.line = line
        self.column = column