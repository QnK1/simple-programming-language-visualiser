from dataclasses import dataclass

class Statement:
    def __init__(self, line_start: int, column_start: int):
        self.line_start: int = line_start
        self.column_start: int = column_start


class VariableDefinitionStatement(Statement):
    def __init__(self, line_start: int, column_start: int, name: str, type: str, final_val: str, rhs_exp: "Expression"):
        super().__init__(line_start, column_start)
        self.name: str = name
        self.type: str = type
        self.final_val: str = final_val
        self.rhs_exp: "Expression" = rhs_exp


class VariableAssignmentStatement(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class FunctionDefinitionStatement(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class FunctionCallStatement(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class IfStatement(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class WhileStatement(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class LoopStatement(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class Error(Statement):
    def __init__(self, line_start: int, column_start: int):
        super().__init__(line_start, column_start)


class Expression:
    class Stage:
        def __init__(self, c: str | FunctionCallStatement):
            self.content: str | FunctionCallStatement = c
    
    def __init__(self):
        self.stages: list[Expression.Stage] = []


@dataclass(order=True)
class IntValue:
    value: int

    def __str__(self):
        return f"{self.value}"

    def __add__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value + other.value)
        elif isinstance(other, ListValue):
            return other + self
        elif isinstance(other, FloatValue):
            return FloatValue(self.value + other.value)
        
        raise NotImplementedError()


    def __mul__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value * other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value * other.value)

        raise NotImplementedError()


@dataclass(order=True)
class FloatValue:
    value: float

    def __str__(self):
        return f"{self.value}"
    
    def __add__(self, other):
        if isinstance(other, FloatValue):
            return FloatValue(self.value + other.value)
        elif isinstance(other, ListValue):
            return other + self
        elif isinstance(other, IntValue):
            return FloatValue(self.value + other.value)
        
        raise NotImplementedError()
    
    
    def __mul__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value * other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value * other.value)

        raise NotImplementedError()
        

@dataclass(order=True)
class StringValue:
    value: str

    def __str__(self):
        return f"\"{self.value}\""

    def __add__(self, other):
        if isinstance(other, StringValue):
            return StringValue(self.value + other.value)
        elif isinstance(other, ListValue):
            return other + self
        
        raise NotImplementedError()

@dataclass
class BoolValue:
    value: bool

    def __str__(self):
        return f"\"{self.value}\"".lower()
    

@dataclass
class ListValue:
    value: list

    def __str__(self):
        return f"[{','.join([e.__str__() for e in self.value])}]"
    
    def __add__(self, other):
        if isinstance(other, ListValue):
            return ListValue(self.value + other.value)
        else:
            res = ListValue(self.value)
            res.value.append(other)
            print(other)
            return res
