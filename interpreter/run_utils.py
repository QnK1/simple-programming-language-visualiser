from dataclasses import dataclass
from enum import Enum

class Statement:
    def __init__(self, line_start: int, column_start: int):
        self.line_start: int = line_start
        self.column_start: int = column_start

class ScopeType(Enum):
    GLOBAL = 1
    FUNCTION = 2

class VariableDefinitionStatement(Statement):
    def __init__(self, line_start: int, column_start: int, name: str, type: str, final_val, rhs_exp: "Expression", scope: ScopeType):
        super().__init__(line_start, column_start)
        self.name: str = name
        self.type: str = type
        self.final_val: str = final_val
        self.rhs_exp: "Expression" = rhs_exp
        self.scope = scope


class VariableAssignmentStatement(Statement):
    def __init__(self, line_start: int, column_start: int, name: str, type: str, final_val, rhs_exp: "Expression", scope: ScopeType, is_list_indexing: bool, index_exp: "Expression", final_index: str):
        super().__init__(line_start, column_start)
        self.name: str = name
        self.type: str = type
        self.final_val: str = final_val
        self.rhs_exp: "Expression" = rhs_exp
        self.scope = scope
        self.is_list_indexing = is_list_indexing
        self.index_exp = index_exp
        self.final_index = final_index


class FunctionDefinitionStatement(Statement):
    def __init__(self, line_start: int, column_start: int, args: list["Argument"], return_type: str, name: str):
        super().__init__(line_start, column_start)
        self.args = args
        self.return_type = return_type
        self.name = name


class ReturnStatement(Statement):
    def __init__(self, line_start: int, column_start: int, function_name: str, return_exp: "Expression", return_val):
        super().__init__(line_start, column_start)
        self.function_name = function_name
        self.return_val = return_val


class FunctionCallStatement(Statement):
    def __init__(self, line_start: int, column_start: int, function_name: str, arg_expressions: list["Expression"], arg_values: list):
        super().__init__(line_start, column_start)
        self.function_name = function_name
        self.arg_expressions = arg_expressions
        self.arg_values = arg_values


class IfStatement(Statement):
    def __init__(self, line_start: int, column_start: int, condition_exp: "Expression", final_cond_val, has_else: bool):
        super().__init__(line_start, column_start)
        self.condition_exp = condition_exp
        self.final_cond_val = final_cond_val
        self.has_else = has_else


# represents one time a while statement is reached and evaluated
class WhileStatement(Statement):
    def __init__(self, line_start: int, column_start: int, condition_exp: "Expression", final_cond_val):
        super().__init__(line_start, column_start)
        self.condition_exp = condition_exp
        self.final_cond_val = final_cond_val


class LoopStatement(Statement):
    def __init__(self, line_start: int, column_start: int, iterator_name: str, iterator_type: str, current_iterator_val: str, iterated_exp: "Expression", iterated_exp_final_val, current_iterator_index: int):
        super().__init__(line_start, column_start)
        self.iterator_name = iterator_name
        self.iterator_type = iterator_type
        self.current_iterator_val = current_iterator_val
        self.iterated_exp = iterated_exp
        self.iterated_exp_final_val = iterated_exp_final_val
        self.current_iterator_index = current_iterator_index


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
        print(type(other))
        
        if isinstance(other, IntValue):
            return IntValue(self.value + other.value)
        elif isinstance(other, ListValue):
            return other + self
        elif isinstance(other, FloatValue):
            return FloatValue(self.value + other.value)
        
        raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value - other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value - other.value)
        
        raise NotImplementedError()

    def __mul__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value * other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value * other.value)

        raise NotImplementedError()
    
    def __truediv__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value / other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value / other.value)

        raise NotImplementedError()
    
    def __mod__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value % other.value)

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
    
    def __sub__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value - other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value - other.value)
        
        raise NotImplementedError()
    
    
    def __mul__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value * other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value * other.value)

        raise NotImplementedError()
    
    def __truediv__(self, other):
        if isinstance(other, IntValue):
            return IntValue(self.value / other.value)
        elif isinstance(other, FloatValue):
            return FloatValue(self.value / other.value)

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
        return f"{self.value}".lower()
    
    def __and__(self, other):
        if isinstance(other, IntValue):
            return BoolValue(self.value and other.value)

        raise NotImplementedError()
    
    def __or__(self, other):
        if isinstance(other, IntValue):
            return BoolValue(self.value or other.value)

        raise NotImplementedError()
    
    def __xor__(self, other):
        if isinstance(other, IntValue):
            return BoolValue(self.value ^ other.value)

        raise NotImplementedError()
    
    def __bool__(self):
        return self.value
    

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
    
    def __getitem__(self, i):
        if isinstance(i, slice):
            return ListValue(self.value[i.start.value:i.stop.value])
        else:
            return ListValue(self.value[i.value])
    
    def __setitem__(self, key, val):
        self.value[key.value] = val.value

    def __contains__(self, item):
        return BoolValue(item in self.value)

    
    def fromElementType(self, val):
        if isinstance(self.value[0], IntValue):
            return IntValue(val)
        elif isinstance(self.value[0], FloatValue):
            return FloatValue(val)
        elif isinstance(self.value[0], BoolValue):
            return BoolValue(val)
        elif isinstance(self.value[0], ListValue):
            return ListValue(val)
        elif isinstance(self.value[0], StringValue):
            return StringValue(val)


@dataclass
class Variable:
    type: str
    value: IntValue | FloatValue | StringValue | BoolValue | ListValue


class Scope:
    def __init__(self, fun_name: str = "$$global"):
        self.variables: dict[str, Variable] = {}
        self.fun_name: str = fun_name


@dataclass
class Argument:
    type: str
    name: str

@dataclass
class Function:
    args: list[Argument]
    return_type: str
    name: str
    content: list