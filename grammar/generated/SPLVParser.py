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
        4,1,30,220,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,3,2,53,8,2,1,3,1,
        3,1,3,1,3,1,3,3,3,60,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,72,8,4,10,4,12,4,75,9,4,1,4,3,4,78,8,4,1,4,1,4,1,4,1,4,3,4,84,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,96,8,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,113,8,5,10,
        5,12,5,116,9,5,1,6,1,6,1,6,1,6,1,6,5,6,123,8,6,10,6,12,6,126,9,6,
        1,6,3,6,129,8,6,3,6,131,8,6,1,6,1,6,1,7,3,7,136,8,7,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,151,8,9,10,9,12,9,154,
        9,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,162,8,10,10,10,12,10,165,9,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,5,11,181,8,11,10,11,12,11,184,9,11,1,11,3,11,187,8,11,3,
        11,189,8,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,197,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,0,1,10,16,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,0,0,238,0,37,1,0,0,0,2,47,1,0,0,0,4,52,1,
        0,0,0,6,59,1,0,0,0,8,83,1,0,0,0,10,95,1,0,0,0,12,117,1,0,0,0,14,
        135,1,0,0,0,16,142,1,0,0,0,18,146,1,0,0,0,20,157,1,0,0,0,22,170,
        1,0,0,0,24,196,1,0,0,0,26,198,1,0,0,0,28,204,1,0,0,0,30,210,1,0,
        0,0,32,33,3,2,1,0,33,34,5,22,0,0,34,36,1,0,0,0,35,32,1,0,0,0,36,
        39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,
        0,40,41,5,0,0,1,41,1,1,0,0,0,42,48,3,14,7,0,43,48,3,16,8,0,44,48,
        3,22,11,0,45,48,3,12,6,0,46,48,3,24,12,0,47,42,1,0,0,0,47,43,1,0,
        0,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,3,1,0,0,0,49,53,
        3,16,8,0,50,53,3,12,6,0,51,53,3,24,12,0,52,49,1,0,0,0,52,50,1,0,
        0,0,52,51,1,0,0,0,53,5,1,0,0,0,54,60,5,4,0,0,55,60,5,5,0,0,56,60,
        5,7,0,0,57,60,5,11,0,0,58,60,3,8,4,0,59,54,1,0,0,0,59,55,1,0,0,0,
        59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,7,1,0,0,0,61,62,5,25,
        0,0,62,63,3,10,5,0,63,64,5,23,0,0,64,65,3,10,5,0,65,66,5,26,0,0,
        66,84,1,0,0,0,67,68,5,25,0,0,68,73,3,10,5,0,69,70,5,24,0,0,70,72,
        3,10,5,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,
        74,77,1,0,0,0,75,73,1,0,0,0,76,78,5,24,0,0,77,76,1,0,0,0,77,78,1,
        0,0,0,78,79,1,0,0,0,79,80,5,26,0,0,80,84,1,0,0,0,81,82,5,25,0,0,
        82,84,5,26,0,0,83,61,1,0,0,0,83,67,1,0,0,0,83,81,1,0,0,0,84,9,1,
        0,0,0,85,86,6,5,-1,0,86,96,3,6,3,0,87,96,5,3,0,0,88,96,3,12,6,0,
        89,90,5,29,0,0,90,91,3,10,5,0,91,92,5,30,0,0,92,96,1,0,0,0,93,94,
        5,12,0,0,94,96,3,10,5,2,95,85,1,0,0,0,95,87,1,0,0,0,95,88,1,0,0,
        0,95,89,1,0,0,0,95,93,1,0,0,0,96,114,1,0,0,0,97,98,10,6,0,0,98,99,
        5,8,0,0,99,113,3,10,5,7,100,101,10,5,0,0,101,102,5,9,0,0,102,113,
        3,10,5,6,103,104,10,4,0,0,104,105,5,11,0,0,105,113,3,10,5,5,106,
        107,10,3,0,0,107,108,5,10,0,0,108,113,3,10,5,4,109,110,10,1,0,0,
        110,111,5,14,0,0,111,113,3,10,5,2,112,97,1,0,0,0,112,100,1,0,0,0,
        112,103,1,0,0,0,112,106,1,0,0,0,112,109,1,0,0,0,113,116,1,0,0,0,
        114,112,1,0,0,0,114,115,1,0,0,0,115,11,1,0,0,0,116,114,1,0,0,0,117,
        118,5,3,0,0,118,130,5,29,0,0,119,124,3,10,5,0,120,121,5,24,0,0,121,
        123,3,10,5,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,127,129,5,24,0,0,128,
        127,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,119,1,0,0,0,130,
        131,1,0,0,0,131,132,1,0,0,0,132,133,5,30,0,0,133,13,1,0,0,0,134,
        136,5,21,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,
        138,5,20,0,0,138,139,5,3,0,0,139,140,5,13,0,0,140,141,3,10,5,0,141,
        15,1,0,0,0,142,143,5,3,0,0,143,144,5,13,0,0,144,145,3,10,5,0,145,
        17,1,0,0,0,146,152,5,27,0,0,147,148,3,4,2,0,148,149,5,22,0,0,149,
        151,1,0,0,0,150,147,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,
        153,1,0,0,0,153,155,1,0,0,0,154,152,1,0,0,0,155,156,5,28,0,0,156,
        19,1,0,0,0,157,163,5,27,0,0,158,159,3,4,2,0,159,160,5,22,0,0,160,
        162,1,0,0,0,161,158,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,
        164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,5,19,0,0,167,
        168,5,22,0,0,168,169,5,28,0,0,169,21,1,0,0,0,170,171,5,18,0,0,171,
        172,5,20,0,0,172,173,5,23,0,0,173,174,5,3,0,0,174,188,5,29,0,0,175,
        176,5,20,0,0,176,182,5,3,0,0,177,178,5,24,0,0,178,179,5,20,0,0,179,
        181,5,3,0,0,180,177,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,
        183,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,185,187,5,24,0,0,186,
        185,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,175,1,0,0,0,188,
        189,1,0,0,0,189,190,1,0,0,0,190,191,5,30,0,0,191,192,3,20,10,0,192,
        23,1,0,0,0,193,197,3,26,13,0,194,197,3,28,14,0,195,197,3,30,15,0,
        196,193,1,0,0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,25,1,0,0,0,198,
        199,5,15,0,0,199,200,5,29,0,0,200,201,3,10,5,0,201,202,5,30,0,0,
        202,203,3,18,9,0,203,27,1,0,0,0,204,205,5,17,0,0,205,206,5,29,0,
        0,206,207,3,10,5,0,207,208,5,30,0,0,208,209,3,18,9,0,209,29,1,0,
        0,0,210,211,5,16,0,0,211,212,5,29,0,0,212,213,5,20,0,0,213,214,5,
        3,0,0,214,215,5,14,0,0,215,216,3,10,5,0,216,217,5,30,0,0,217,218,
        3,18,9,0,218,31,1,0,0,0,20,37,47,52,59,73,77,83,95,112,114,124,128,
        130,135,152,163,182,186,188,196
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
    RULE_functionBlock = 10
    RULE_functionDefinition = 11
    RULE_controlStatement = 12
    RULE_ifStatement = 13
    RULE_whileStatement = 14
    RULE_loopStatement = 15

    ruleNames =  [ "program", "statement", "innerStatement", "literal", 
                   "listLiteral", "expression", "functionCall", "variableDefinition", 
                   "variableAssignment", "block", "functionBlock", "functionDefinition", 
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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3637256) != 0):
                self.state = 32
                self.statement()
                self.state = 33
                self.match(SPLVParser.Semicolon)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.variableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.variableAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.variableAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
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
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(SPLVParser.BooleanOperator)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(SPLVParser.BracketLeft)
                self.state = 62
                self.expression(0)
                self.state = 63
                self.match(SPLVParser.Colon)
                self.state = 64
                self.expression(0)
                self.state = 65
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(SPLVParser.BracketLeft)
                self.state = 68
                self.expression(0)
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 69
                        self.match(SPLVParser.Comma)
                        self.state = 70
                        self.expression(0) 
                    self.state = 75
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 76
                    self.match(SPLVParser.Comma)


                self.state = 79
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(SPLVParser.BracketLeft)
                self.state = 82
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 86
                self.literal()
                pass

            elif la_ == 2:
                self.state = 87
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 3:
                self.state = 88
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 89
                self.match(SPLVParser.ParenLeft)
                self.state = 90
                self.expression(0)
                self.state = 91
                self.match(SPLVParser.ParenRight)
                pass

            elif la_ == 5:
                self.state = 93
                self.match(SPLVParser.NOTOperator)
                self.state = 94
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 112
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 97
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 98
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 99
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 100
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 101
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 102
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 103
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 104
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 105
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 106
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 107
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 108
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 109
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 110
                        self.match(SPLVParser.InOperator)
                        self.state = 111
                        self.expression(2)
                        pass

             
                self.state = 116
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
            self.state = 117
            self.match(SPLVParser.Identifier)
            self.state = 118
            self.match(SPLVParser.ParenLeft)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 570431672) != 0):
                self.state = 119
                self.expression(0)
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 120
                        self.match(SPLVParser.Comma)
                        self.state = 121
                        self.expression(0) 
                    self.state = 126
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 127
                    self.match(SPLVParser.Comma)




            self.state = 132
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
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 134
                self.match(SPLVParser.GlobalTypeModifier)


            self.state = 137
            self.match(SPLVParser.Type)
            self.state = 138
            self.match(SPLVParser.Identifier)
            self.state = 139
            self.match(SPLVParser.AssignmentOperator)
            self.state = 140
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
            self.state = 142
            self.match(SPLVParser.Identifier)
            self.state = 143
            self.match(SPLVParser.AssignmentOperator)
            self.state = 144
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
            self.state = 146
            self.match(SPLVParser.CurlyLeft)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 229384) != 0):
                self.state = 147
                self.innerStatement()
                self.state = 148
                self.match(SPLVParser.Semicolon)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(SPLVParser.CurlRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CurlyLeft(self):
            return self.getToken(SPLVParser.CurlyLeft, 0)

        def ReturnKeyword(self):
            return self.getToken(SPLVParser.ReturnKeyword, 0)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Semicolon)
            else:
                return self.getToken(SPLVParser.Semicolon, i)

        def CurlRight(self):
            return self.getToken(SPLVParser.CurlRight, 0)

        def innerStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.InnerStatementContext)
            else:
                return self.getTypedRuleContext(SPLVParser.InnerStatementContext,i)


        def getRuleIndex(self):
            return SPLVParser.RULE_functionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBlock" ):
                listener.enterFunctionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBlock" ):
                listener.exitFunctionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBlock" ):
                return visitor.visitFunctionBlock(self)
            else:
                return visitor.visitChildren(self)




    def functionBlock(self):

        localctx = SPLVParser.FunctionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(SPLVParser.CurlyLeft)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 229384) != 0):
                self.state = 158
                self.innerStatement()
                self.state = 159
                self.match(SPLVParser.Semicolon)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(SPLVParser.ReturnKeyword)
            self.state = 167
            self.match(SPLVParser.Semicolon)
            self.state = 168
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

        def functionBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionBlockContext,0)


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
        self.enterRule(localctx, 22, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SPLVParser.FunctionKeyword)
            self.state = 171
            self.match(SPLVParser.Type)
            self.state = 172
            self.match(SPLVParser.Colon)
            self.state = 173
            self.match(SPLVParser.Identifier)
            self.state = 174
            self.match(SPLVParser.ParenLeft)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 175
                self.match(SPLVParser.Type)
                self.state = 176
                self.match(SPLVParser.Identifier)
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 177
                        self.match(SPLVParser.Comma)
                        self.state = 178
                        self.match(SPLVParser.Type)
                        self.state = 179
                        self.match(SPLVParser.Identifier) 
                    self.state = 184
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 185
                    self.match(SPLVParser.Comma)




            self.state = 190
            self.match(SPLVParser.ParenRight)
            self.state = 191
            self.functionBlock()
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
        self.enterRule(localctx, 24, self.RULE_controlStatement)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
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
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(SPLVParser.IfKeyword)
            self.state = 199
            self.match(SPLVParser.ParenLeft)
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
        self.enterRule(localctx, 28, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(SPLVParser.WhileKeyword)
            self.state = 205
            self.match(SPLVParser.ParenLeft)
            self.state = 206
            self.expression(0)
            self.state = 207
            self.match(SPLVParser.ParenRight)
            self.state = 208
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
        self.enterRule(localctx, 30, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(SPLVParser.LoopKeyword)
            self.state = 211
            self.match(SPLVParser.ParenLeft)
            self.state = 212
            self.match(SPLVParser.Type)
            self.state = 213
            self.match(SPLVParser.Identifier)
            self.state = 214
            self.match(SPLVParser.InOperator)
            self.state = 215
            self.expression(0)
            self.state = 216
            self.match(SPLVParser.ParenRight)
            self.state = 217
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
         




