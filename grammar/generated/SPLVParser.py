# Generated from d:/Desktop/SPLV/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,3,2,51,8,2,1,3,1,3,1,3,1,3,
        1,3,3,3,58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,70,8,
        4,10,4,12,4,73,9,4,1,4,3,4,76,8,4,1,4,1,4,1,4,1,4,3,4,82,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,94,8,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,111,8,5,10,5,12,5,
        114,9,5,1,6,1,6,1,6,1,6,1,6,5,6,121,8,6,10,6,12,6,124,9,6,1,6,3,
        6,127,8,6,3,6,129,8,6,1,6,1,6,1,7,3,7,134,8,7,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,149,8,9,10,9,12,9,152,9,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,166,
        8,10,10,10,12,10,169,9,10,1,10,3,10,172,8,10,3,10,174,8,10,1,10,
        1,10,1,10,1,11,1,11,1,11,3,11,182,8,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,0,1,10,15,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,0,0,223,0,35,1,0,0,0,2,45,1,0,0,0,4,50,1,0,0,0,6,57,1,0,0,
        0,8,81,1,0,0,0,10,93,1,0,0,0,12,115,1,0,0,0,14,133,1,0,0,0,16,140,
        1,0,0,0,18,144,1,0,0,0,20,155,1,0,0,0,22,181,1,0,0,0,24,183,1,0,
        0,0,26,189,1,0,0,0,28,195,1,0,0,0,30,31,3,2,1,0,31,32,5,22,0,0,32,
        34,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,
        0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,46,3,
        14,7,0,41,46,3,16,8,0,42,46,3,20,10,0,43,46,3,12,6,0,44,46,3,22,
        11,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,
        44,1,0,0,0,46,3,1,0,0,0,47,51,3,16,8,0,48,51,3,12,6,0,49,51,3,22,
        11,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,5,1,0,0,0,52,58,
        5,4,0,0,53,58,5,5,0,0,54,58,5,7,0,0,55,58,5,11,0,0,56,58,3,8,4,0,
        57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,
        0,0,0,58,7,1,0,0,0,59,60,5,25,0,0,60,61,3,10,5,0,61,62,5,23,0,0,
        62,63,3,10,5,0,63,64,5,26,0,0,64,82,1,0,0,0,65,66,5,25,0,0,66,71,
        3,10,5,0,67,68,5,24,0,0,68,70,3,10,5,0,69,67,1,0,0,0,70,73,1,0,0,
        0,71,69,1,0,0,0,71,72,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,74,76,
        5,24,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,26,0,
        0,78,82,1,0,0,0,79,80,5,25,0,0,80,82,5,26,0,0,81,59,1,0,0,0,81,65,
        1,0,0,0,81,79,1,0,0,0,82,9,1,0,0,0,83,84,6,5,-1,0,84,94,3,6,3,0,
        85,94,5,3,0,0,86,94,3,12,6,0,87,88,5,29,0,0,88,89,3,10,5,0,89,90,
        5,30,0,0,90,94,1,0,0,0,91,92,5,12,0,0,92,94,3,10,5,2,93,83,1,0,0,
        0,93,85,1,0,0,0,93,86,1,0,0,0,93,87,1,0,0,0,93,91,1,0,0,0,94,112,
        1,0,0,0,95,96,10,6,0,0,96,97,5,8,0,0,97,111,3,10,5,7,98,99,10,5,
        0,0,99,100,5,9,0,0,100,111,3,10,5,6,101,102,10,4,0,0,102,103,5,11,
        0,0,103,111,3,10,5,5,104,105,10,3,0,0,105,106,5,10,0,0,106,111,3,
        10,5,4,107,108,10,1,0,0,108,109,5,14,0,0,109,111,3,10,5,2,110,95,
        1,0,0,0,110,98,1,0,0,0,110,101,1,0,0,0,110,104,1,0,0,0,110,107,1,
        0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,11,1,0,
        0,0,114,112,1,0,0,0,115,116,5,3,0,0,116,128,5,29,0,0,117,122,3,10,
        5,0,118,119,5,24,0,0,119,121,3,10,5,0,120,118,1,0,0,0,121,124,1,
        0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,126,1,0,0,0,124,122,1,
        0,0,0,125,127,5,24,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,129,1,
        0,0,0,128,117,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,5,
        30,0,0,131,13,1,0,0,0,132,134,5,21,0,0,133,132,1,0,0,0,133,134,1,
        0,0,0,134,135,1,0,0,0,135,136,5,20,0,0,136,137,5,3,0,0,137,138,5,
        13,0,0,138,139,3,10,5,0,139,15,1,0,0,0,140,141,5,3,0,0,141,142,5,
        13,0,0,142,143,3,10,5,0,143,17,1,0,0,0,144,150,5,27,0,0,145,146,
        3,4,2,0,146,147,5,22,0,0,147,149,1,0,0,0,148,145,1,0,0,0,149,152,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,
        1,0,0,0,153,154,5,28,0,0,154,19,1,0,0,0,155,156,5,18,0,0,156,157,
        5,20,0,0,157,158,5,23,0,0,158,159,5,3,0,0,159,173,5,29,0,0,160,161,
        5,20,0,0,161,167,5,3,0,0,162,163,5,24,0,0,163,164,5,20,0,0,164,166,
        5,3,0,0,165,162,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,170,172,5,24,0,0,171,170,
        1,0,0,0,171,172,1,0,0,0,172,174,1,0,0,0,173,160,1,0,0,0,173,174,
        1,0,0,0,174,175,1,0,0,0,175,176,5,30,0,0,176,177,3,18,9,0,177,21,
        1,0,0,0,178,182,3,24,12,0,179,182,3,26,13,0,180,182,3,28,14,0,181,
        178,1,0,0,0,181,179,1,0,0,0,181,180,1,0,0,0,182,23,1,0,0,0,183,184,
        5,15,0,0,184,185,5,29,0,0,185,186,3,10,5,0,186,187,5,30,0,0,187,
        188,3,18,9,0,188,25,1,0,0,0,189,190,5,17,0,0,190,191,5,29,0,0,191,
        192,3,10,5,0,192,193,5,30,0,0,193,194,3,18,9,0,194,27,1,0,0,0,195,
        196,5,16,0,0,196,197,5,29,0,0,197,198,5,20,0,0,198,199,5,3,0,0,199,
        200,5,14,0,0,200,201,3,10,5,0,201,202,5,30,0,0,202,203,3,18,9,0,
        203,29,1,0,0,0,19,35,45,50,57,71,75,81,93,110,112,122,126,128,133,
        150,167,171,173,181
    ]

class SPLVParser ( Parser ):

    grammarFileName = "SPLVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'!'", "'='", "'in'", "'if'", "'lop'", "'while'", "'fun'", 
                     "'ret'", "<INVALID>", "'glob'", "';'", "':'", "','", 
                     "'['", "']'", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "Comment", "Identifier", "IntLiteral", 
                      "FloatLiteral", "BoolLiteral", "StringLiteral", "AdditiveOperator", 
                      "MultiplicativeOperator", "ComparisonOperator", "BooleanOperator", 
                      "NOTOperator", "AssignmentOperator", "InOperator", 
                      "IfKeyword", "LoopKeyword", "WhileKeyword", "FunctionKeyword", 
                      "ReturnKeyword", "Type", "GlobalTypeModifier", "Semicolon", 
                      "Colon", "Comma", "BracketLeft", "BracketRight", "CurlyLeft", 
                      "CurlRight", "ParenLeft", "ParenRight" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_innerStatement = 2
    RULE_literal = 3
    RULE_listLiteral = 4
    RULE_expression = 5
    RULE_functionCall = 6
    RULE_variableDefinition = 7
    RULE_variableAssignment = 8
    RULE_block = 9
    RULE_functionDefinition = 10
    RULE_controlStatement = 11
    RULE_ifStatement = 12
    RULE_whileStatement = 13
    RULE_loopStatement = 14

    ruleNames =  [ "program", "statement", "innerStatement", "literal", 
                   "listLiteral", "expression", "functionCall", "variableDefinition", 
                   "variableAssignment", "block", "functionDefinition", 
                   "controlStatement", "ifStatement", "whileStatement", 
                   "loopStatement" ]

    EOF = Token.EOF
    WS=1
    Comment=2
    Identifier=3
    IntLiteral=4
    FloatLiteral=5
    BoolLiteral=6
    StringLiteral=7
    AdditiveOperator=8
    MultiplicativeOperator=9
    ComparisonOperator=10
    BooleanOperator=11
    NOTOperator=12
    AssignmentOperator=13
    InOperator=14
    IfKeyword=15
    LoopKeyword=16
    WhileKeyword=17
    FunctionKeyword=18
    ReturnKeyword=19
    Type=20
    GlobalTypeModifier=21
    Semicolon=22
    Colon=23
    Comma=24
    BracketLeft=25
    BracketRight=26
    CurlyLeft=27
    CurlRight=28
    ParenLeft=29
    ParenRight=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SPLVParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.StatementContext)
            else:
                return self.getTypedRuleContext(SPLVParser.StatementContext,i)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Semicolon)
            else:
                return self.getToken(SPLVParser.Semicolon, i)

        def getRuleIndex(self):
            return SPLVParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SPLVParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3637256) != 0):
                self.state = 30
                self.statement()
                self.state = 31
                self.match(SPLVParser.Semicolon)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(SPLVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(SPLVParser.VariableDefinitionContext,0)


        def variableAssignment(self):
            return self.getTypedRuleContext(SPLVParser.VariableAssignmentContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(SPLVParser.FunctionDefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def controlStatement(self):
            return self.getTypedRuleContext(SPLVParser.ControlStatementContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SPLVParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.variableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.variableAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.controlStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableAssignment(self):
            return self.getTypedRuleContext(SPLVParser.VariableAssignmentContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def controlStatement(self):
            return self.getTypedRuleContext(SPLVParser.ControlStatementContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_innerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInnerStatement" ):
                listener.enterInnerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInnerStatement" ):
                listener.exitInnerStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerStatement" ):
                return visitor.visitInnerStatement(self)
            else:
                return visitor.visitChildren(self)




    def innerStatement(self):

        localctx = SPLVParser.InnerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_innerStatement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.variableAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.controlStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntLiteral(self):
            return self.getToken(SPLVParser.IntLiteral, 0)

        def FloatLiteral(self):
            return self.getToken(SPLVParser.FloatLiteral, 0)

        def StringLiteral(self):
            return self.getToken(SPLVParser.StringLiteral, 0)

        def BooleanOperator(self):
            return self.getToken(SPLVParser.BooleanOperator, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(SPLVParser.ListLiteralContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SPLVParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(SPLVParser.BooleanOperator)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.listLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)


        def Colon(self):
            return self.getToken(SPLVParser.Colon, 0)

        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Comma)
            else:
                return self.getToken(SPLVParser.Comma, i)

        def getRuleIndex(self):
            return SPLVParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = SPLVParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(SPLVParser.BracketLeft)
                self.state = 60
                self.expression(0)
                self.state = 61
                self.match(SPLVParser.Colon)
                self.state = 62
                self.expression(0)
                self.state = 63
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(SPLVParser.BracketLeft)
                self.state = 66
                self.expression(0)
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 67
                        self.match(SPLVParser.Comma)
                        self.state = 68
                        self.expression(0) 
                    self.state = 73
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 74
                    self.match(SPLVParser.Comma)


                self.state = 77
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(SPLVParser.BracketLeft)
                self.state = 80
                self.match(SPLVParser.BracketRight)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(SPLVParser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)


        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def NOTOperator(self):
            return self.getToken(SPLVParser.NOTOperator, 0)

        def AdditiveOperator(self):
            return self.getToken(SPLVParser.AdditiveOperator, 0)

        def MultiplicativeOperator(self):
            return self.getToken(SPLVParser.MultiplicativeOperator, 0)

        def BooleanOperator(self):
            return self.getToken(SPLVParser.BooleanOperator, 0)

        def ComparisonOperator(self):
            return self.getToken(SPLVParser.ComparisonOperator, 0)

        def InOperator(self):
            return self.getToken(SPLVParser.InOperator, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SPLVParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 84
                self.literal()
                pass

            elif la_ == 2:
                self.state = 85
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 3:
                self.state = 86
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 87
                self.match(SPLVParser.ParenLeft)
                self.state = 88
                self.expression(0)
                self.state = 89
                self.match(SPLVParser.ParenRight)
                pass

            elif la_ == 5:
                self.state = 91
                self.match(SPLVParser.NOTOperator)
                self.state = 92
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 95
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 96
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 97
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 99
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 100
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 102
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 103
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 105
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 106
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 108
                        self.match(SPLVParser.InOperator)
                        self.state = 109
                        self.expression(2)
                        pass

             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Comma)
            else:
                return self.getToken(SPLVParser.Comma, i)

        def getRuleIndex(self):
            return SPLVParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = SPLVParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(SPLVParser.Identifier)
            self.state = 116
            self.match(SPLVParser.ParenLeft)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 570431672) != 0):
                self.state = 117
                self.expression(0)
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 118
                        self.match(SPLVParser.Comma)
                        self.state = 119
                        self.expression(0) 
                    self.state = 124
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 125
                    self.match(SPLVParser.Comma)




            self.state = 130
            self.match(SPLVParser.ParenRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(SPLVParser.Type, 0)

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def AssignmentOperator(self):
            return self.getToken(SPLVParser.AssignmentOperator, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def GlobalTypeModifier(self):
            return self.getToken(SPLVParser.GlobalTypeModifier, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDefinition" ):
                return visitor.visitVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def variableDefinition(self):

        localctx = SPLVParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 132
                self.match(SPLVParser.GlobalTypeModifier)


            self.state = 135
            self.match(SPLVParser.Type)
            self.state = 136
            self.match(SPLVParser.Identifier)
            self.state = 137
            self.match(SPLVParser.AssignmentOperator)
            self.state = 138
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def AssignmentOperator(self):
            return self.getToken(SPLVParser.AssignmentOperator, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_variableAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAssignment" ):
                listener.enterVariableAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAssignment" ):
                listener.exitVariableAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAssignment" ):
                return visitor.visitVariableAssignment(self)
            else:
                return visitor.visitChildren(self)




    def variableAssignment(self):

        localctx = SPLVParser.VariableAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(SPLVParser.Identifier)
            self.state = 141
            self.match(SPLVParser.AssignmentOperator)
            self.state = 142
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CurlyLeft(self):
            return self.getToken(SPLVParser.CurlyLeft, 0)

        def CurlRight(self):
            return self.getToken(SPLVParser.CurlRight, 0)

        def innerStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.InnerStatementContext)
            else:
                return self.getTypedRuleContext(SPLVParser.InnerStatementContext,i)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Semicolon)
            else:
                return self.getToken(SPLVParser.Semicolon, i)

        def getRuleIndex(self):
            return SPLVParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SPLVParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(SPLVParser.CurlyLeft)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 229384) != 0):
                self.state = 145
                self.innerStatement()
                self.state = 146
                self.match(SPLVParser.Semicolon)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(SPLVParser.CurlRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FunctionKeyword(self):
            return self.getToken(SPLVParser.FunctionKeyword, 0)

        def Type(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Type)
            else:
                return self.getToken(SPLVParser.Type, i)

        def Colon(self):
            return self.getToken(SPLVParser.Colon, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Identifier)
            else:
                return self.getToken(SPLVParser.Identifier, i)

        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def block(self):
            return self.getTypedRuleContext(SPLVParser.BlockContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Comma)
            else:
                return self.getToken(SPLVParser.Comma, i)

        def getRuleIndex(self):
            return SPLVParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = SPLVParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(SPLVParser.FunctionKeyword)
            self.state = 156
            self.match(SPLVParser.Type)
            self.state = 157
            self.match(SPLVParser.Colon)
            self.state = 158
            self.match(SPLVParser.Identifier)
            self.state = 159
            self.match(SPLVParser.ParenLeft)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 160
                self.match(SPLVParser.Type)
                self.state = 161
                self.match(SPLVParser.Identifier)
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 162
                        self.match(SPLVParser.Comma)
                        self.state = 163
                        self.match(SPLVParser.Type)
                        self.state = 164
                        self.match(SPLVParser.Identifier) 
                    self.state = 169
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 170
                    self.match(SPLVParser.Comma)




            self.state = 175
            self.match(SPLVParser.ParenRight)
            self.state = 176
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(SPLVParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(SPLVParser.WhileStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(SPLVParser.LoopStatementContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_controlStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlStatement" ):
                listener.enterControlStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlStatement" ):
                listener.exitControlStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlStatement" ):
                return visitor.visitControlStatement(self)
            else:
                return visitor.visitChildren(self)




    def controlStatement(self):

        localctx = SPLVParser.ControlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_controlStatement)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.loopStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IfKeyword(self):
            return self.getToken(SPLVParser.IfKeyword, 0)

        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def block(self):
            return self.getTypedRuleContext(SPLVParser.BlockContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SPLVParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(SPLVParser.IfKeyword)
            self.state = 184
            self.match(SPLVParser.ParenLeft)
            self.state = 185
            self.expression(0)
            self.state = 186
            self.match(SPLVParser.ParenRight)
            self.state = 187
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WhileKeyword(self):
            return self.getToken(SPLVParser.WhileKeyword, 0)

        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def block(self):
            return self.getTypedRuleContext(SPLVParser.BlockContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SPLVParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(SPLVParser.WhileKeyword)
            self.state = 190
            self.match(SPLVParser.ParenLeft)
            self.state = 191
            self.expression(0)
            self.state = 192
            self.match(SPLVParser.ParenRight)
            self.state = 193
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LoopKeyword(self):
            return self.getToken(SPLVParser.LoopKeyword, 0)

        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def Type(self):
            return self.getToken(SPLVParser.Type, 0)

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def InOperator(self):
            return self.getToken(SPLVParser.InOperator, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def block(self):
            return self.getTypedRuleContext(SPLVParser.BlockContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = SPLVParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(SPLVParser.LoopKeyword)
            self.state = 196
            self.match(SPLVParser.ParenLeft)
            self.state = 197
            self.match(SPLVParser.Type)
            self.state = 198
            self.match(SPLVParser.Identifier)
            self.state = 199
            self.match(SPLVParser.InOperator)
            self.state = 200
            self.expression(0)
            self.state = 201
            self.match(SPLVParser.ParenRight)
            self.state = 202
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




