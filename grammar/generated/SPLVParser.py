# Generated from d:/Users/Kacper/Desktop/tkik/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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
        4,1,40,15,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,
        1,1,1,1,1,1,0,0,2,0,2,0,0,13,0,7,1,0,0,0,2,12,1,0,0,0,4,6,3,2,1,
        0,5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,0,0,0,9,
        7,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,5,16,0,0,13,3,1,0,0,0,
        1,7
    ]

class SPLVParser ( Parser ):

    grammarFileName = "SPLVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'>='", "'<'", "'<='", 
                     "'=='", "'!='", "'!'", "'='", "'in'", "'if'", "'lop'", 
                     "'while'", "'fun'", "'ret'", "'int'", "'flo'", "'str'", 
                     "'bol'", "'lst'", "'glob'", "';'", "':'", "','", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "Comment", "Identifier", "IntLiteral", 
                      "FloatLiteral", "BoolLiteral", "StringLiteral", "PlusOperator", 
                      "MinusOperator", "StarOperator", "SlashOperator", 
                      "GTOperator", "GEOperator", "LTOperator", "LEOperator", 
                      "EQOperator", "NEQOperator", "NOTOperator", "AssignmentOperator", 
                      "InOperator", "IfKeyword", "LoopKeyword", "WhileKeyword", 
                      "FunctionKeyword", "ReturnKeyword", "IntType", "FloatType", 
                      "StringType", "BooleanType", "ListType", "GlobalTypeModifier", 
                      "Semicolon", "Colon", "Comma", "BracketLeft", "BracketRight", 
                      "CurlyLeft", "CurlRight", "ParenLeft", "ParenRight" ]

    RULE_program = 0
    RULE_statement = 1

    ruleNames =  [ "program", "statement" ]

    EOF = Token.EOF
    WS=1
    Comment=2
    Identifier=3
    IntLiteral=4
    FloatLiteral=5
    BoolLiteral=6
    StringLiteral=7
    PlusOperator=8
    MinusOperator=9
    StarOperator=10
    SlashOperator=11
    GTOperator=12
    GEOperator=13
    LTOperator=14
    LEOperator=15
    EQOperator=16
    NEQOperator=17
    NOTOperator=18
    AssignmentOperator=19
    InOperator=20
    IfKeyword=21
    LoopKeyword=22
    WhileKeyword=23
    FunctionKeyword=24
    ReturnKeyword=25
    IntType=26
    FloatType=27
    StringType=28
    BooleanType=29
    ListType=30
    GlobalTypeModifier=31
    Semicolon=32
    Colon=33
    Comma=34
    BracketLeft=35
    BracketRight=36
    CurlyLeft=37
    CurlRight=38
    ParenLeft=39
    ParenRight=40

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
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 4
                self.statement()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
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

        def EQOperator(self):
            return self.getToken(SPLVParser.EQOperator, 0)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(SPLVParser.EQOperator)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





