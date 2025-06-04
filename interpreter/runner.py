from antlr4 import *

from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor
from .run_utils import *
from .errors import ZeroDivisionException, IndexOutOfBoundsException


class Runner(SPLVParserVisitor):
    def __init__(self):
        self.result: list[Statement] = []
        self.scopes: list[Scope] = [Scope()]
        self.functions: dict[str, Function] = {}

    def visitProgram(self, ctx:SPLVParser.ProgramContext):
        try:
            self.visitChildren(ctx)
        except (IndexOutOfBoundsException, ZeroDivisionException) as e:
            self.result.append(Error(e.line, e.column, e.msg))
        return self.result
    

    def executeStatement(self, ctx):
        if (isinstance(ctx, SPLVParser.StatementContext) or isinstance(ctx, SPLVParser.StatementInFunctionContext)) and ctx.variableDefinition() is not None:
            n, t, f, e, s = self.visitVariableDefinition(ctx.variableDefinition())
            
            self.result.append(VariableDefinitionStatement(ctx.start.line, ctx.start.column, n, t, f, e, s))
        elif (isinstance(ctx, SPLVParser.StatementContext) or isinstance(ctx, SPLVParser.StatementInControlBlockContext) or isinstance(ctx, SPLVParser.StatementInFunctionContext)) and ctx.variableAssignment() is not None:
            n, t, f, e, s, ii, ie, fi = self.visitVariableAssignment(ctx.variableAssignment())
            self.result.append(VariableAssignmentStatement(ctx.start.line, ctx.start.column, n, t, f, e, s, ii, ie, fi))
        elif isinstance(ctx, SPLVParser.StatementContext) and ctx.functionDefinition() is not None:
            self.visit(ctx.functionDefinition())
        elif ctx.functionCall() is not None:
            self.callFunction(ctx.functionCall())
        elif (isinstance(ctx, SPLVParser.StatementContext) or isinstance(ctx, SPLVParser.StatementInControlBlockContext)) and ctx.controlStatement().ifStatement() is not None:
            c, f, h, statements_to_execute = self.visitIfStatement(ctx.controlStatement().ifStatement())
            
            self.result.append(IfStatement(ctx.start.line, ctx.start.column, c, f, h))

            for s in statements_to_execute:
                self.executeStatement(s)
        elif (isinstance(ctx, SPLVParser.StatementContext) or isinstance(ctx, SPLVParser.StatementInControlBlockContext)) and ctx.controlStatement().whileStatement() is not None:
            self.visit(ctx.controlStatement().whileStatement())
            
        elif (isinstance(ctx, SPLVParser.StatementContext) or isinstance(ctx, SPLVParser.StatementInControlBlockContext)) and ctx.controlStatement().loopStatement() is not None:
            self.visit(ctx.controlStatement().loopStatement())
        elif isinstance(ctx, SPLVParser.StatementInFunctionContext) and ctx.controlStatementInsideFunction() is not None and ctx.controlStatementInsideFunction().ifStatementInsideFunction() is not None:
            c, f, h, statements_to_execute = self.visitIfStatementInsideFunction(ctx.controlStatementInsideFunction().ifStatementInsideFunction())
            
            self.result.append(IfStatement(ctx.start.line, ctx.start.column, c, f, h))

            for s in statements_to_execute:
                self.executeStatement(s)
        elif isinstance(ctx, SPLVParser.StatementInFunctionContext) and ctx.controlStatementInsideFunction() is not None and ctx.controlStatementInsideFunction().whileStatementInsideFunction() is not None:
            self.visit(ctx.controlStatementInsideFunction().whileStatementInsideFunction())
        elif isinstance(ctx, SPLVParser.StatementInFunctionContext) and ctx.controlStatementInsideFunction() is not None and ctx.controlStatementInsideFunction().loopStatementInsideFunction() is not None:
            self.visit(ctx.controlStatementInsideFunction().loopStatementInsideFunction())
        elif isinstance(ctx, SPLVParser.StatementInFunctionContext) and ctx.returnStatement() is not None:
            self.visitReturnStatement(ctx.returnStatement())


    def visitStatement(self, ctx:SPLVParser.StatementContext):
        self.executeStatement(ctx)
    

    def visitStatementInControlBlock(self, ctx:SPLVParser.StatementInControlBlockContext):
        self.executeStatement(ctx)
    

    def callFunction(self, ctx: SPLVParser.FunctionCallContext):
        function = self.functions[ctx.Identifier().getText()]
        
        self.scopes.append(Scope(function.name))

        arg_exps = []
        arg_values = []

        for a, param in zip(ctx.passedParametersList().expression(), function.args):
            calculator = ExpressionCalculator(self)
            arg_exp = calculator.calculate(a)
            final_val = arg_exp.stages[-1].content

            arg_exps.append(arg_exp)
            arg_values.append(final_val)

            self.scopes[-1].variables[param.name] = Variable(param.type, final_val)

        
        self.result.append(FunctionCallStatement(ctx.start.line, ctx.start.column, function.name, arg_exps, arg_values))

        for statement in function.content:
            self.executeStatement(statement)
            if isinstance(self.result[-1], ReturnStatement):
                break

        
        # handling of void functions without return statements
        if not isinstance(self.result[-1], ReturnStatement):
            self.result.append(ReturnStatement(-1, -1, function.name, None, None))

        self.scopes.pop()
    

    def visitReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        fun_name = self.scopes[-1].fun_name
        if self.functions[fun_name].return_type != "nul":
            exp = ctx.expression()
            calculator = ExpressionCalculator(self)
            return_exp = calculator.calculate(exp)
            final_val = return_exp.stages[-1].content
        else:
            return_exp = None
            final_val = None

        self.result.append(ReturnStatement(ctx.start.line, ctx.start.column, fun_name, return_exp, final_val))


    def visitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        args = [Argument(a.type_().getText(), a.Identifier().getText()) for a in ctx.functionArgumentList().functionArgument()]
        return_type = ctx.functionIdentifier().functionReturnType().getText()
        name = ctx.functionIdentifier().Identifier().getText()
        content = ctx.functionBlock().statementInFunction()

        self.functions[name] = Function(args, return_type, name, content)

        self.result.append(FunctionDefinitionStatement(ctx.start.line, ctx.start.column, args, return_type, name))
    

    def executeIfStatement(self, ctx):
        condition_ctx = ctx.expression()
        calculator = ExpressionCalculator(self)
        exp = calculator.calculate(condition_ctx)
        final_val = exp.stages[-1].content
        has_else = ctx.ElseKeyword() is not None
        statements = []


        if final_val.value:
            if isinstance(ctx, SPLVParser.IfStatementContext):
                statements = ctx.controlBlock()[0].statementInControlBlock()
            elif isinstance(ctx, SPLVParser.IfStatementInsideFunctionContext):
                statements = ctx.functionControlBlock()[0].statementInFunction()
        elif has_else:
            if isinstance(ctx, SPLVParser.IfStatementContext):
                statements = ctx.controlBlock()[1].statementInControlBlock()
            elif isinstance(ctx, SPLVParser.IfStatementInsideFunctionContext):
                statements = ctx.functionControlBlock()[1].statementInFunction()


        return exp, final_val, has_else, statements

    def visitIfStatement(self, ctx:SPLVParser.IfStatementContext):
        return self.executeIfStatement(ctx)


    def executeWhileStatement(self, ctx):
        condition_ctx = ctx.expression()
        calculator = ExpressionCalculator(self)

        exp = calculator.calculate(condition_ctx)
        val = exp.stages[-1].content


        while val.value:
            self.result.append(WhileStatement(ctx.start.line, ctx.start.column, exp, val))
            
            if isinstance(ctx, SPLVParser.WhileStatementContext):
                statements = ctx.controlBlock().statementInControlBlock()
            elif isinstance(ctx, SPLVParser.WhileStatementInsideFunctionContext):   
                statements = ctx.functionControlBlock().statementInFunction()

            for s in statements:
                self.executeStatement(s)
            
            calculator = ExpressionCalculator(self)
            exp = calculator.calculate(condition_ctx)
            val = exp.stages[-1].content

        self.result.append(WhileStatement(ctx.start.line, ctx.start.column, exp, val))

    def visitWhileStatement(self, ctx:SPLVParser.WhileStatementContext):
        self.executeWhileStatement(ctx)
    

    def executeLoopStatement(self, ctx):
        self.scopes.append(Scope())

        iterator_name = ctx.loopStatementIterator().Identifier().getText()
        iterator_type = ctx.loopStatementIterator().type_().getText()
        self.scopes[-1].variables[iterator_name] = Variable(iterator_type, None)

        iterated_exp_ctx = ctx.loopStatementIterator().expression()
        calculator = ExpressionCalculator(self)
        iterated_exp = calculator.calculate(iterated_exp_ctx)
        iterated_exp_final_val = iterated_exp.stages[-1].content

        iteration_started = False
        for index, i in enumerate(iterated_exp_final_val.value):
            iteration_started = True

            self.setVariableValue(iterator_name, i)

            self.result.append(LoopStatement(ctx.start.line, ctx.start.column, iterator_name, iterator_type, i, iterated_exp, iterated_exp_final_val, index))

            if isinstance(ctx, SPLVParser.LoopStatementContext):
                statements = ctx.controlBlock().statementInControlBlock()
            elif isinstance(ctx, SPLVParser.LoopStatementInsideFunctionContext):
                statements = ctx.functionControlBlock().statementInFunction()

            for s in statements:
                self.executeStatement(s)
        
        if not iteration_started:
            self.result.append(LoopStatement(ctx.start.line, ctx.start.column, iterator_name, iterator_type, None, iterated_exp, iterated_exp_final_val, None))
        
        self.scopes.pop()

    def visitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.executeLoopStatement(ctx)


    def visitIfStatementInsideFunction(self, ctx:SPLVParser.IfStatementInsideFunctionContext):
        return self.executeIfStatement(ctx)


    def visitWhileStatementInsideFunction(self, ctx:SPLVParser.WhileStatementInsideFunctionContext):
        self.executeWhileStatement(ctx)

    def visitLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        self.executeLoopStatement(ctx)

    def visitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        rhs_exp = ctx.expression()

        calculator = ExpressionCalculator(self)
        exp = calculator.calculate(rhs_exp)

        name = ctx.Identifier().getText()
        t = ctx.type_().getText()
        final_val = exp.stages[-1].content

        if ctx.GlobalTypeModifier() is None and len(self.scopes) > 1:
            self.scopes[-1].variables[name] = Variable(t, final_val)
            scope = ScopeType.FUNCTION
        else:
            self.scopes[0].variables[name] = Variable(t, final_val)
            scope = ScopeType.GLOBAL

        return name, t, final_val, exp, scope
    

    # Visit a parse tree produced by SPLVParser#variableAssignment.
    def visitVariableAssignment(self, ctx:SPLVParser.VariableAssignmentContext):
        rhs_exp = ctx.expression()
        calculator = ExpressionCalculator(self)
        exp = calculator.calculate(rhs_exp)
        final_val = exp.stages[-1].content

        lvalue = ctx.lValue()

        name = lvalue
        while name.Identifier() is None:
            name = name.lValue()

        name = name.Identifier().getText()     

        t = self.getVariableType(name)

        is_list_indexing = False
        final_indices = []
        index_exps = []

        if lvalue.expression() is None:
            self.setVariableValue(name, final_val)
        else:
            is_list_indexing = True
            index_exp_ctx = []
            while lvalue.expression() is not None:
                index_exp_ctx.append(lvalue.expression())
                lvalue = lvalue.lValue()
            
            for e in index_exp_ctx:
                calculator = ExpressionCalculator(self)
                index_exps.append(calculator.calculate(e))
                final_indices.append(index_exps[-1].stages[-1].content)

            try:
                self.setListElement(name, final_val, final_indices)
            except IndexError:
                raise IndexOutOfBoundsException("Index out of bounds", ctx.start.line, ctx.start.column)
        
        return name, t, final_val, exp, self.getVariableScope(name), is_list_indexing, index_exps, final_indices


    def getVariableValue(self, name, i = None):
        for scope in self.scopes[::-1]:
            if name in scope.variables:
                if i is None:
                    return scope.variables[name].value
                else:
                    return scope.variables[name].value[i]
    

    def setVariableValue(self, name, value):
        for scope in self.scopes[::-1]:
            if name in scope.variables:
                scope.variables[name].value = value
                return

    def setListElement(self, name, value, indices):
        for scope in self.scopes[::-1]:
            if name in scope.variables:
                var = scope.variables[name].value

                
                for i in indices[::-1][0:-1]:
                    var = var[i]
                
                i = indices[::-1][-1]
                
                var[i] = value
                return
    

    def getVariableType(self, name):
        for scope in self.scopes[::-1]:
            if name in scope.variables:
                return scope.variables[name].type
    

    def getVariableScope(self, name):
        for i, scope in enumerate(self.scopes[::-1]):
            if name in scope.variables:
                if i != 0 or i == 0 and len(self.scopes) == 1:
                    return ScopeType.GLOBAL
                else:
                    return ScopeType.FUNCTION
    


class ExpressionCalculator(SPLVParserVisitor):
    def __init__(self, runner):
        self.original_expression = None
        self.depth = None
        self.starting_depth = None
        self.runner: Runner = runner
        self.res = Expression()
        self.func_results = {}
    
    def calculate(self, exp):
        self.original_expression = exp.getText()

        counter = ExpressionCounter()
        self.starting_depth = counter.visit(exp)

        while self.starting_depth >= 0:
            self.depth = self.starting_depth
            self.res.stages.append(Expression.Stage(self.visit(exp)))
            self.starting_depth = self.starting_depth - 1
        
        print("Stages:")
        for stage in self.res.stages:
            if isinstance(stage, Expression.Stage):
                print(stage.content)
            else:
                print(stage)
        
        return self.res

    
    # Visit a parse tree produced by SPLVParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        content = self.visit(ctx.expression())
        
        if start_depth > 0:
            return f"({content})"
        else:
            return content



    # Visit a parse tree produced by SPLVParser#inOperatorExpression.
    def visitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        

        if start_depth > 0:
            return f"{left_content} in {right_content}"
        else:
            return right_content.__contains__(left_content)


    # Visit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def visitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        
        operator = ctx.AdditiveOperator().getText()

        if operator == "+":
            if start_depth > 0:
                return f"{left_content}+{right_content}"
            else:
                return left_content + right_content
        elif operator == "-":
            if start_depth > 0:
                return f"{left_content}-{right_content}"
            else:
                return left_content - right_content


    # Visit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def visitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        
        operator = ctx.ComparisonOperator().getText()

        if operator == "==":
            if start_depth > 0:
                return f"{left_content}=={right_content}"
            else:
                return BoolValue(left_content == right_content)
        elif operator == "!=":
            if start_depth > 0:
                return f"{left_content}!={right_content}"
            else:
                return BoolValue(left_content != right_content)
        elif operator == "<=":
            if start_depth > 0:
                return f"{left_content}<={right_content}"
            else:
                return BoolValue(left_content <= right_content)
        elif operator == "<":
            if start_depth > 0:
                return f"{left_content}<{right_content}"
            else:
                return BoolValue(left_content < right_content)
        elif operator == ">=":
            if start_depth > 0:
                return f"{left_content}>={right_content}"
            else:
                return BoolValue(left_content >= right_content)
        elif operator == ">":
            if start_depth > 0:
                return f"{left_content}>{right_content}"
            else:
                return BoolValue(left_content > right_content)


    # Visit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def visitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        
        operator = ctx.MultiplicativeOperator().getText()

        if operator == "*":
            if start_depth > 0:
                return f"{left_content}*{right_content}"
            else:
                return left_content * right_content
        elif operator == "/":
            if start_depth > 0:
                return f"{left_content}/{right_content}"
            else:
                try:
                    ret = left_content / right_content
                except ZeroDivisionError:
                    raise ZeroDivisionException("Index out of bounds excepiton", ctx.start.line, ctx.start.column)
                return ret
        elif operator == "%":
            if start_depth > 0:
                return f"{left_content}%{right_content}"
            else:
                return left_content % right_content
        


    # Visit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def visitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        
        operator = ctx.BooleanOperator().getText()

        if operator == "and":
            if start_depth > 0:
                return f"{left_content} and {right_content}"
            else:
                return left_content and right_content
        elif operator == "or":
            if start_depth > 0:
                return f"{left_content} or {right_content}"
            else:
                return left_content or right_content
        elif operator == "xor":
            if start_depth > 0:
                return f"{left_content} xor {right_content}"
            else:
                return left_content ^ right_content


    # Visit a parse tree produced by SPLVParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        name = ctx.Identifier().getText()


        if start_depth > 0:
                return f"{name}"
        else:
            try:
                ret = self.runner.getVariableValue(name)
            except IndexError:
                raise IndexOutOfBoundsException("Index out of bounds", ctx.start.line, ctx.start.column)
            return ret


    # Visit a parse tree produced by SPLVParser#listSlicingExpression.
    def visitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1


        list_exp = ctx.expression()[0]
        left_exp = ctx.left_exp
        right_exp = ctx.right_exp

        list_content = self.visit(list_exp)
        
        if start_depth > 0:
            if isinstance(ctx.expression()[0], SPLVParser.IdentifierExpressionContext):
                list_content = ctx.expression()[0].Identifier().getText()
            return f"{list_content}[{self.visit(left_exp)}:{self.visit(right_exp)}]"
        else:
            try:
                ret = list_content[self.visit(left_exp):self.visit(right_exp)]
            except IndexError:
                raise IndexOutOfBoundsException("Index out of bounds", ctx.start.line, ctx.start.column)
            return ret


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        arg_exps = ctx.functionCall().passedParametersList().expression()
        arg_contents = [self.visit(exp) for exp in arg_exps]

        fun_name = ctx.functionCall().Identifier().getText()

        if start_depth > 0:
            return f"{fun_name}({','.join([a.__str__() for a in arg_contents])})"
        else:
            if (ctx.start.line, ctx.start.column) not in self.func_results.keys():
                starting_len = len(self.runner.result)
                self.runner.executeStatement(ctx)

                contents = self.runner.result[starting_len:]
                self.runner.result = self.runner.result[:starting_len]

                
                self.res.stages.append(Expression.Stage(contents, True))

                val = contents[-1].return_val

                self.func_results[(ctx.start.line, ctx.start.column)] = val
            else:
                val = self.func_results[(ctx.start.line, ctx.start.column)]

            return val


    # Visit a parse tree produced by SPLVParser#notOperatorExpression.
    def visitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        exp = ctx.expression()

        content = self.visit(exp)
        
        if start_depth > 0:
            return f"not {content}"
        else:
            return not content
        


    # Visit a parse tree produced by SPLVParser#listIndexingExpression.
    def visitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        list_exp = ctx.expression()[0]
        index_exp = ctx.expression()[1]


        list_content = self.visit(list_exp)
        index_content = self.visit(index_exp)

        
        if start_depth > 0:
            if isinstance(ctx.expression()[0], SPLVParser.IdentifierExpressionContext):
                list_content = ctx.expression()[0].Identifier().getText()
            return f"{list_content}[{index_content}]"
        else:
            try:
                ret = list_content[index_content]
            except IndexError:
                raise IndexOutOfBoundsException("Index out of bounds", ctx.start.line, ctx.start.column)
            return ret


    # Visit a parse tree produced by SPLVParser#literalExpression.
    def visitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        if ctx.literal().listLiteral() is None:
            # print(f"start depth: {self.depth}, return val: {self._getLiteralValue(ctx.literal())}")
            return self._getLiteralValue(ctx.literal())
        
        if isinstance(ctx.literal().listLiteral(), SPLVParser.EmptyListLiteralContext):
            return ListValue([])
        elif isinstance(ctx.literal().listLiteral(), SPLVParser.ListFromElementsLiteralContext):
            start_depth = self.depth

            exps = ctx.literal().listLiteral().expression()
            content = [self.visit(e) for e in exps]

            if start_depth > 0:
                return f"{ListValue(content)}"
            else:
                return ListValue(content)
        elif isinstance(ctx.literal().listLiteral(), SPLVParser.ListFromRangeLiteralContext):
            start_depth = self.depth

            exp1 = ctx.literal().listLiteral().expression()[0]
            exp2 = ctx.literal().listLiteral().expression()[1]
            
            content1 = self.visit(exp1)
            content2 = self.visit(exp2)

            if start_depth > 0:
                return f"[{content1}..{content2}]"
            else:
                return ListValue([IntValue(i) for i in range(content1.value, content2.value)])


    

    def _getLiteralValue(self, ctx):
        if ctx.IntLiteral() is not None:
            literal = ctx.IntLiteral()
            val = IntValue(int(literal.getText()))
        elif ctx.FloatLiteral() is not None:
            literal = ctx.FloatLiteral()
            val = FloatValue(float(literal.getText()))
        elif ctx.StringLiteral() is not None:
            literal = ctx.StringLiteral()
            val = StringValue(literal.getText()[1:-1])
        elif ctx.BoolLiteral() is not None:
            literal = ctx.BoolLiteral()
            val = BoolValue(True if literal.getText().lower() == "true" else False)
        
        return val



class ExpressionCounter(SPLVParserVisitor):
    # Visit a parse tree produced by SPLVParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        return 1 + self.visit(ctx.expression())


    # Visit a parse tree produced by SPLVParser#inOperatorExpression.
    def visitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def visitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def visitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def visitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def visitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        return 1


    # Visit a parse tree produced by SPLVParser#listSlicingExpression.
    def visitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        exps = ctx.expression()
        list_exp = exps[0]
        ind_exp1 = exps[1] if len(exps) >= 2 else None
        ind_exp2 = exps[2] if len(exps) == 3 else None

        count1 = self.visit(ind_exp1) if ind_exp1 is not None else 0
        count2 = self.visit(ind_exp2) if ind_exp2 is not None else 0

        return 1 + self.visit(list_exp) + count1 + count2 - (1 if type(list_exp) == SPLVParser.IdentifierExpressionContext else 0)


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        exps = ctx.functionCall().passedParametersList().expression()

        return 1 + sum([self.visit(e) for e in exps])


    # Visit a parse tree produced by SPLVParser#notOperatorExpression.
    def visitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        return 1 + self.visit(ctx.expression())


    # Visit a parse tree produced by SPLVParser#listIndexingExpression.
    def visitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        exps = ctx.expression()


        return 1 + sum([self.visit(e) for e in exps]) - (1 if type(exps[0]) == SPLVParser.IdentifierExpressionContext else 0)


    # Visit a parse tree produced by SPLVParser#literalExpression.
    def visitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        res = 0
        if ctx.literal().listLiteral() is not None and type(ctx.literal().listLiteral()) != SPLVParser.EmptyListLiteralContext:
            res += sum([self.visit(e) for e in ctx.literal().listLiteral().expression()])

        
        return res