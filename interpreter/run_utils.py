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
        def __init__(self, c: str | Statement):
            self.content: str | Statement = c
    
    def __init__(self):
        self.stages: list[Expression.Stage] = []


