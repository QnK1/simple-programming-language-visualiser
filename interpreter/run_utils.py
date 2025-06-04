from dataclasses import dataclass
from enum import Enum
import copy

class Statement:
    """
    A general statemnt class.
    It represents a single line or logical block of code.
    """
    def __init__(self, line_start: int, column_start: int):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
        """
        self.line_start: int = line_start
        self.column_start: int = column_start

class ScopeType(Enum):
    GLOBAL = 1
    FUNCTION = 2

class VariableDefinitionStatement(Statement):
    """
    Represents a variable definition, like 'int a = 5;'
    """
    def __init__(self, line_start: int, column_start: int, name: str, type: str, final_val, rhs_exp: "Expression", scope: ScopeType):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            name (str): Name of the variable being defined.
            type (str): Type of the variable being defined.
            rhs_exp (Expression): The right hand side expression being assigned to the variable.
            final_val: IntValue/FloatValue/etc. object representing the final calculated value of the rhs expression.
            scope (ScopeType): The scope in which the variable is being defined (GLOBAL or FUNCTION).
        """
        super().__init__(line_start, column_start)
        self.name: str = copy.deepcopy(name)
        self.type: str = copy.deepcopy(type)
        self.rhs_exp: "Expression" = copy.deepcopy(rhs_exp)
        self.final_val = copy.deepcopy(final_val)
        self.scope: ScopeType = copy.deepcopy(scope)


class VariableAssignmentStatement(Statement):
    """
    Represents variable assignment, like 'a = 5; or list[0] = 3;', distinguished by the is_list_indexing attribute.
    """
    def __init__(self, line_start: int, column_start: int, name: str, type: str, final_val, rhs_exp: "Expression", scope: ScopeType, is_list_indexing: bool, index_exps: list["Expression"], final_indices: list):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            name (str): Name of the variable that is being assigned a new value.
            type (str): Type of the variable that is being assigned a new value.
            rhs_exp (Expression): The right hand side expression being assigned to the variable.
            final_val: IntValue/FloatValue/etc. object representing the final calculated value of the rhs expression.
            scope (ScopeType): The scope in which the variable is being defined (GLOBAL or FUNCTION).
            is_list_indexing (bool): Indicates if it's simple variable assignment or assignment to a list at a given index.
            index_exps (list[Expression]): A list of the expressions for the indices, from left to right.
            final_indices (list[IntValue]): A list of the indices, for example for l[1][2][3] = 5 it its [1, 2, 3].
        """
        super().__init__(line_start, column_start)
        self.name: str = copy.deepcopy(name)
        self.type: str = copy.deepcopy(type)
        self.final_val = copy.deepcopy(final_val)
        self.rhs_exp: "Expression" = copy.deepcopy(rhs_exp)
        self.scope: ScopeType = copy.deepcopy(scope)
        self.is_list_indexing: bool = copy.deepcopy(is_list_indexing)
        self.index_exps: list["Expression"] = copy.deepcopy(index_exps)
        self.final_indices: list[IntValue] = copy.deepcopy(final_indices)


class FunctionDefinitionStatement(Statement):
    """
    Represents the moment a function is defined. 
    It is just the definition, NOT the moment the function is called.
    """
    def __init__(self, line_start: int, column_start: int, args: list["Argument"], return_type: str, name: str):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            args (list[Argument]): List of the arguments (names and types) the function takes.
            return_type (str): The type the function returns.
            name (str): Name of the defined function.
        """
        super().__init__(line_start, column_start)
        self.args: list["Argument"] = copy.deepcopy(args)
        self.return_type: str = copy.deepcopy(return_type)
        self.name = copy.deepcopy(name)


class ReturnStatement(Statement):
    """
    Marks the end of a function call.
    A function call begins with a FunctionCallStatement, then all the following statements are part
    of the function's body execution, until the ReturnStatement is reached, which marks the end of the function scope.
    Void functions end with a ReturnStatement as well, in that case return_val and return_exp are None.
    """
    def __init__(self, line_start: int, column_start: int, function_name: str, return_exp: "Expression", return_val):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            function_name (str): Name of the function that the return statement is a part of.
            return_val: IntValue/FloatValue/etc. object containing the returned value.
            return_exp (Expression): The expression that gives the returned value.
        """
        super().__init__(line_start, column_start)
        self.function_name = copy.deepcopy(function_name)
        self.return_val = copy.deepcopy(return_val)
        self.return_exp: "Expression" = copy.deepcopy(return_exp)


class FunctionCallStatement(Statement):
    """
    Marks the beginning of a function call and its scope.
    A function call begins with a FunctionCallStatement, then all the following statements are part
    of the function's body execution, until the ReturnStatement is reached, which marks the end of the function scope.
    IMPORTANT: the statements inside the function are not part of the FunctionCallStatement, the are just next in the list,
    between the FunctionCallStatement and the ReturnStatement.
    Void functions end with a ReturnStatement as well, in that case return_val and return_exp are None.
    """
    def __init__(self, line_start: int, column_start: int, function_name: str, arg_expressions: list["Expression"], arg_values: list):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            function_name (str): Name of the function that is being called.
            arg_expressions (list[Expression]): A list of the expressions passed as the parameters, from left to right.
            arg_values: List of objects containing the final values of the parameters, from left to right.
        """
        super().__init__(line_start, column_start)
        self.function_name = copy.deepcopy(function_name)
        self.arg_expressions: list["Expression"] = copy.deepcopy(arg_expressions)
        self.arg_values = copy.deepcopy(arg_values)


class IfStatement(Statement):
    """
    Marks the moment an if statement's condition is evaluated.
    It is present whether the condition is true or not, as indicated by the final_cond_val atttribute.
    If the condition is true, the statements inside the 'if' block are executed next.
    If the condition is false, the next statement is just the first statement after the 'if' block or inside the 'else' block, if present.
    """
    def __init__(self, line_start: int, column_start: int, condition_exp: "Expression", final_cond_val, has_else: bool):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            condition_exp (Expression): The expression evaluated in the condition.
            final_cond_val (BoolValue): The final value of the condition expression.
            has_else (bool): Indicates whether an else block is present. It is true if the else block is in the code, not if it is reached.
        """
        super().__init__(line_start, column_start)
        self.condition_exp: "Expression" = copy.deepcopy(condition_exp)
        self.final_cond_val: "BoolValue" = copy.deepcopy(final_cond_val)
        self.has_else: bool = copy.deepcopy(has_else)


# represents one time a while statement is reached and evaluated
class WhileStatement(Statement):
    """
    Marks the moment a while statement's condition is evaluated.
    It is present whether the condition is true or not, as indicated by the final_cond_val atttribute.
    If the condition is true, the statements inside the 'while' block are executed next.
    If the condition is false, the next statement is just the first statement after the 'while' block.
    """
    def __init__(self, line_start: int, column_start: int, condition_exp: "Expression", final_cond_val):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            condition_exp (Expression): The expression evaluated in the condition.
            final_cond_val (BoolValue): The final value of the condition expression.
        """
        super().__init__(line_start, column_start)
        self.condition_exp: "Expression" = copy.deepcopy(condition_exp)
        self.final_cond_val: "BoolValue" = copy.deepcopy(final_cond_val)


class LoopStatement(Statement):
    """
    Marks the moment a loop statement's iterator gets the next value assigned to it.
    Unlike WhileStatement, it is not present one more time after the final iteration to evaluate the condition,
    with the exception of something like 'lop(int i in [])', when the first time it's reached is indicated.
    """
    def __init__(self, line_start: int, column_start: int, iterator_name: str, iterator_type: str, current_iterator_val: str, iterated_exp: "Expression", iterated_exp_final_val, current_iterator_index: int):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            iterator_name (str): Name of the iterator variable.
            iterator_type (str): Type of the iterator variable.
            current_iterator_val: Value assigned to the iterator in the current iteration.
            iterated_exp (Expression): The expression being iterated, for example for 'lop(int in in [1, 2])' it would be an Expression object for [1, 2]
            iterated_exp_final_val: The evaluated expression being iterated.
            current_iterator_index (int): Current index in the iterated expression.
        """
        super().__init__(line_start, column_start)
        self.iterator_name:str = copy.deepcopy(iterator_name)
        self.iterator_type = copy.deepcopy(iterator_type)
        self.current_iterator_val = copy.deepcopy(current_iterator_val)
        self.iterated_exp: "Expression" = copy.deepcopy(iterated_exp)
        self.iterated_exp_final_val = copy.deepcopy(iterated_exp_final_val)
        self.current_iterator_index: int = copy.deepcopy(current_iterator_index)


class Error(Statement):
    """
    Represents a runtime error, like a zero division or and out of bounds list index.
    """
    def __init__(self, line_start: int, column_start: int, message: str):
        """
        Attributes:
            line_start (int): Number of the line in the original code where the statement starts, including all whitespace.
            column_start (int): Number of the column in the original code where the statement starts, including all whitespace.
            message (str): The error message to display to the user.
        """
        super().__init__(line_start, column_start)
        self.message = message


class Expression:
    """
    Represents an expression, with all the stages leading to its final evaluation.
    """
    class Stage:
        """
        Represents a stage of an expression's evaluation.
        Can be a string, a value (for the final step) or a list of statements, when a function is called.
        """
        def __init__(self, c: str | list[Statement], is_function_call: bool = False):
            self.content: str | list[Statement] = c
            self.is_function_call = is_function_call
    
    def __init__(self):
        """
        Attributes:
            stages (list[Expression.Stage]): List of the stages of the expression's evaluation.
        """
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
        elif isinstance(other, str):
            return StringValue(self.value + other)
        
        raise NotImplementedError()
    
    def __getitem__(self, i):
        if isinstance(i, int):
            return self.value[i]
        elif isinstance(i, IntValue):
            return self.value[i.value]


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
            if isinstance(i, int):
                return self.value[i]
            elif isinstance(i, IntValue):
                return self.value[i.value]
                
    
    def __setitem__(self, key, val):
        self.value[key.value] = val

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