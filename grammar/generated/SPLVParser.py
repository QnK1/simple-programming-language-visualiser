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
        4,1,32,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        3,1,56,8,1,1,2,1,2,1,2,3,2,61,8,2,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,
        1,4,1,4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,86,8,5,10,5,12,5,89,9,5,1,5,3,5,92,8,5,1,5,1,5,1,5,1,5,3,5,
        98,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,110,8,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,135,8,6,1,6,1,6,3,6,139,8,6,1,6,5,6,142,
        8,6,10,6,12,6,145,9,6,1,7,1,7,1,7,1,7,1,7,5,7,152,8,7,10,7,12,7,
        155,9,7,1,7,3,7,158,8,7,3,7,160,8,7,1,7,1,7,1,8,3,8,165,8,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,180,8,10,
        10,10,12,10,183,9,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,191,8,11,
        10,11,12,11,194,9,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,
        204,8,12,10,12,12,12,207,9,12,1,12,1,12,1,12,1,12,1,13,1,13,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,
        228,8,15,10,15,12,15,231,9,15,1,15,3,15,234,8,15,3,15,236,8,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,250,
        8,15,10,15,12,15,253,9,15,1,15,3,15,256,8,15,3,15,258,8,15,1,15,
        1,15,3,15,262,8,15,1,16,1,16,1,16,3,16,267,8,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,0,1,12,20,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,0,0,316,0,45,1,0,0,0,2,55,1,0,0,0,4,60,
        1,0,0,0,6,66,1,0,0,0,8,73,1,0,0,0,10,97,1,0,0,0,12,109,1,0,0,0,14,
        146,1,0,0,0,16,164,1,0,0,0,18,171,1,0,0,0,20,175,1,0,0,0,22,186,
        1,0,0,0,24,199,1,0,0,0,26,212,1,0,0,0,28,214,1,0,0,0,30,261,1,0,
        0,0,32,266,1,0,0,0,34,268,1,0,0,0,36,274,1,0,0,0,38,280,1,0,0,0,
        40,41,3,2,1,0,41,42,5,23,0,0,42,44,1,0,0,0,43,40,1,0,0,0,44,47,1,
        0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,
        49,5,0,0,1,49,1,1,0,0,0,50,56,3,16,8,0,51,56,3,18,9,0,52,56,3,30,
        15,0,53,56,3,14,7,0,54,56,3,32,16,0,55,50,1,0,0,0,55,51,1,0,0,0,
        55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,3,1,0,0,0,57,61,3,18,
        9,0,58,61,3,14,7,0,59,61,3,32,16,0,60,57,1,0,0,0,60,58,1,0,0,0,60,
        59,1,0,0,0,61,5,1,0,0,0,62,67,3,18,9,0,63,67,3,14,7,0,64,67,3,16,
        8,0,65,67,3,32,16,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,
        65,1,0,0,0,67,7,1,0,0,0,68,74,5,4,0,0,69,74,5,5,0,0,70,74,5,7,0,
        0,71,74,5,6,0,0,72,74,3,10,5,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,
        1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,9,1,0,0,0,75,76,5,27,0,0,
        76,77,3,12,6,0,77,78,5,26,0,0,78,79,3,12,6,0,79,80,5,28,0,0,80,98,
        1,0,0,0,81,82,5,27,0,0,82,87,3,12,6,0,83,84,5,25,0,0,84,86,3,12,
        6,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,
        1,0,0,0,89,87,1,0,0,0,90,92,5,25,0,0,91,90,1,0,0,0,91,92,1,0,0,0,
        92,93,1,0,0,0,93,94,5,28,0,0,94,98,1,0,0,0,95,96,5,27,0,0,96,98,
        5,28,0,0,97,75,1,0,0,0,97,81,1,0,0,0,97,95,1,0,0,0,98,11,1,0,0,0,
        99,100,6,6,-1,0,100,110,3,8,4,0,101,110,5,3,0,0,102,110,3,14,7,0,
        103,104,5,31,0,0,104,105,3,12,6,0,105,106,5,32,0,0,106,110,1,0,0,
        0,107,108,5,12,0,0,108,110,3,12,6,4,109,99,1,0,0,0,109,101,1,0,0,
        0,109,102,1,0,0,0,109,103,1,0,0,0,109,107,1,0,0,0,110,143,1,0,0,
        0,111,112,10,8,0,0,112,113,5,8,0,0,113,142,3,12,6,9,114,115,10,7,
        0,0,115,116,5,9,0,0,116,142,3,12,6,8,117,118,10,6,0,0,118,119,5,
        11,0,0,119,142,3,12,6,7,120,121,10,5,0,0,121,122,5,10,0,0,122,142,
        3,12,6,6,123,124,10,3,0,0,124,125,5,14,0,0,125,142,3,12,6,4,126,
        127,10,2,0,0,127,128,5,27,0,0,128,129,3,12,6,0,129,130,5,28,0,0,
        130,142,1,0,0,0,131,132,10,1,0,0,132,134,5,27,0,0,133,135,3,12,6,
        0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,138,5,24,0,
        0,137,139,3,12,6,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,
        0,140,142,5,28,0,0,141,111,1,0,0,0,141,114,1,0,0,0,141,117,1,0,0,
        0,141,120,1,0,0,0,141,123,1,0,0,0,141,126,1,0,0,0,141,131,1,0,0,
        0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,13,1,0,0,0,
        145,143,1,0,0,0,146,147,5,3,0,0,147,159,5,31,0,0,148,153,3,12,6,
        0,149,150,5,25,0,0,150,152,3,12,6,0,151,149,1,0,0,0,152,155,1,0,
        0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,157,1,0,0,0,155,153,1,0,
        0,0,156,158,5,25,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,160,1,0,
        0,0,159,148,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,162,5,32,
        0,0,162,15,1,0,0,0,163,165,5,22,0,0,164,163,1,0,0,0,164,165,1,0,
        0,0,165,166,1,0,0,0,166,167,5,20,0,0,167,168,5,3,0,0,168,169,5,13,
        0,0,169,170,3,12,6,0,170,17,1,0,0,0,171,172,5,3,0,0,172,173,5,13,
        0,0,173,174,3,12,6,0,174,19,1,0,0,0,175,181,5,29,0,0,176,177,3,4,
        2,0,177,178,5,23,0,0,178,180,1,0,0,0,179,176,1,0,0,0,180,183,1,0,
        0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,181,1,0,
        0,0,184,185,5,30,0,0,185,21,1,0,0,0,186,192,5,29,0,0,187,188,3,6,
        3,0,188,189,5,23,0,0,189,191,1,0,0,0,190,187,1,0,0,0,191,194,1,0,
        0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,192,1,0,
        0,0,195,196,3,28,14,0,196,197,5,23,0,0,197,198,5,30,0,0,198,23,1,
        0,0,0,199,205,5,29,0,0,200,201,3,6,3,0,201,202,5,23,0,0,202,204,
        1,0,0,0,203,200,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,
        1,0,0,0,206,208,1,0,0,0,207,205,1,0,0,0,208,209,3,26,13,0,209,210,
        5,23,0,0,210,211,5,30,0,0,211,25,1,0,0,0,212,213,5,19,0,0,213,27,
        1,0,0,0,214,215,5,19,0,0,215,216,3,12,6,0,216,29,1,0,0,0,217,218,
        5,18,0,0,218,219,5,20,0,0,219,220,5,24,0,0,220,221,5,3,0,0,221,235,
        5,31,0,0,222,223,5,20,0,0,223,229,5,3,0,0,224,225,5,25,0,0,225,226,
        5,20,0,0,226,228,5,3,0,0,227,224,1,0,0,0,228,231,1,0,0,0,229,227,
        1,0,0,0,229,230,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,232,234,
        5,25,0,0,233,232,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,222,
        1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,238,5,32,0,0,238,262,
        3,22,11,0,239,240,5,18,0,0,240,241,5,21,0,0,241,242,5,24,0,0,242,
        243,5,3,0,0,243,257,5,31,0,0,244,245,5,20,0,0,245,251,5,3,0,0,246,
        247,5,25,0,0,247,248,5,20,0,0,248,250,5,3,0,0,249,246,1,0,0,0,250,
        253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,255,1,0,0,0,253,
        251,1,0,0,0,254,256,5,25,0,0,255,254,1,0,0,0,255,256,1,0,0,0,256,
        258,1,0,0,0,257,244,1,0,0,0,257,258,1,0,0,0,258,259,1,0,0,0,259,
        260,5,32,0,0,260,262,3,24,12,0,261,217,1,0,0,0,261,239,1,0,0,0,262,
        31,1,0,0,0,263,267,3,34,17,0,264,267,3,36,18,0,265,267,3,38,19,0,
        266,263,1,0,0,0,266,264,1,0,0,0,266,265,1,0,0,0,267,33,1,0,0,0,268,
        269,5,15,0,0,269,270,5,31,0,0,270,271,3,12,6,0,271,272,5,32,0,0,
        272,273,3,20,10,0,273,35,1,0,0,0,274,275,5,17,0,0,275,276,5,31,0,
        0,276,277,3,12,6,0,277,278,5,32,0,0,278,279,3,20,10,0,279,37,1,0,
        0,0,280,281,5,16,0,0,281,282,5,31,0,0,282,283,5,20,0,0,283,284,5,
        3,0,0,284,285,5,14,0,0,285,286,3,12,6,0,286,287,5,32,0,0,287,288,
        3,20,10,0,288,39,1,0,0,0,28,45,55,60,66,73,87,91,97,109,134,138,
        141,143,153,157,159,164,181,192,205,229,233,235,251,255,257,261,
        266
    ]

class SPLVParser ( Parser ):

    grammarFileName = "SPLVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'!'", "'='", "'in'", "'if'", "'lop'", "'whl'", "'fun'", 
                     "'ret'", "<INVALID>", "'nul'", "'glo'", "';'", "':'", 
                     "','", "'..'", "'['", "']'", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "Comment", "Identifier", "IntLiteral", 
                      "FloatLiteral", "BoolLiteral", "StringLiteral", "AdditiveOperator", 
                      "MultiplicativeOperator", "ComparisonOperator", "BooleanOperator", 
                      "NOTOperator", "AssignmentOperator", "InOperator", 
                      "IfKeyword", "LoopKeyword", "WhileKeyword", "FunctionKeyword", 
                      "ReturnKeyword", "Type", "VoidType", "GlobalTypeModifier", 
                      "Semicolon", "Colon", "Comma", "DoubleDot", "BracketLeft", 
                      "BracketRight", "CurlyLeft", "CurlyRight", "ParenLeft", 
                      "ParenRight" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementInblock = 2
    RULE_statementInFunction = 3
    RULE_literal = 4
    RULE_listLiteral = 5
    RULE_expression = 6
    RULE_functionCall = 7
    RULE_variableDefinition = 8
    RULE_variableAssignment = 9
    RULE_block = 10
    RULE_functionBlock = 11
    RULE_voidFunctionBlock = 12
    RULE_voidReturnStatement = 13
    RULE_returnStatement = 14
    RULE_functionDefinition = 15
    RULE_controlStatement = 16
    RULE_ifStatement = 17
    RULE_whileStatement = 18
    RULE_loopStatement = 19

    ruleNames =  [ "program", "statement", "statementInblock", "statementInFunction", 
                   "literal", "listLiteral", "expression", "functionCall", 
                   "variableDefinition", "variableAssignment", "block", 
                   "functionBlock", "voidFunctionBlock", "voidReturnStatement", 
                   "returnStatement", "functionDefinition", "controlStatement", 
                   "ifStatement", "whileStatement", "loopStatement" ]

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
    VoidType=21
    GlobalTypeModifier=22
    Semicolon=23
    Colon=24
    Comma=25
    DoubleDot=26
    BracketLeft=27
    BracketRight=28
    CurlyLeft=29
    CurlyRight=30
    ParenLeft=31
    ParenRight=32

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
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5734408) != 0):
                self.state = 40
                self.statement()
                self.state = 41
                self.match(SPLVParser.Semicolon)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.variableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.variableAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.controlStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementInblockContext(ParserRuleContext):
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
            return SPLVParser.RULE_statementInblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementInblock" ):
                listener.enterStatementInblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementInblock" ):
                listener.exitStatementInblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementInblock" ):
                return visitor.visitStatementInblock(self)
            else:
                return visitor.visitChildren(self)




    def statementInblock(self):

        localctx = SPLVParser.StatementInblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementInblock)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.variableAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.controlStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementInFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableAssignment(self):
            return self.getTypedRuleContext(SPLVParser.VariableAssignmentContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(SPLVParser.VariableDefinitionContext,0)


        def controlStatement(self):
            return self.getTypedRuleContext(SPLVParser.ControlStatementContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_statementInFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementInFunction" ):
                listener.enterStatementInFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementInFunction" ):
                listener.exitStatementInFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementInFunction" ):
                return visitor.visitStatementInFunction(self)
            else:
                return visitor.visitChildren(self)




    def statementInFunction(self):

        localctx = SPLVParser.StatementInFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statementInFunction)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.variableAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.variableDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
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

        def BoolLiteral(self):
            return self.getToken(SPLVParser.BoolLiteral, 0)

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
        self.enterRule(localctx, 8, self.RULE_literal)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(SPLVParser.BoolLiteral)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
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


        def DoubleDot(self):
            return self.getToken(SPLVParser.DoubleDot, 0)

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
        self.enterRule(localctx, 10, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(SPLVParser.BracketLeft)
                self.state = 76
                self.expression(0)
                self.state = 77
                self.match(SPLVParser.DoubleDot)
                self.state = 78
                self.expression(0)
                self.state = 79
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(SPLVParser.BracketLeft)
                self.state = 82
                self.expression(0)
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 83
                        self.match(SPLVParser.Comma)
                        self.state = 84
                        self.expression(0) 
                    self.state = 89
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 90
                    self.match(SPLVParser.Comma)


                self.state = 93
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(SPLVParser.BracketLeft)
                self.state = 96
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

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)

        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def Colon(self):
            return self.getToken(SPLVParser.Colon, 0)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 100
                self.literal()
                pass

            elif la_ == 2:
                self.state = 101
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 3:
                self.state = 102
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 103
                self.match(SPLVParser.ParenLeft)
                self.state = 104
                self.expression(0)
                self.state = 105
                self.match(SPLVParser.ParenRight)
                pass

            elif la_ == 5:
                self.state = 107
                self.match(SPLVParser.NOTOperator)
                self.state = 108
                self.expression(4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 141
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 112
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 113
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 114
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 115
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 116
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 117
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 118
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 119
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 120
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 121
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 122
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 124
                        self.match(SPLVParser.InOperator)
                        self.state = 125
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 127
                        self.match(SPLVParser.BracketLeft)
                        self.state = 128
                        self.expression(0)
                        self.state = 129
                        self.match(SPLVParser.BracketRight)
                        pass

                    elif la_ == 7:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 132
                        self.match(SPLVParser.BracketLeft)
                        self.state = 134
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2281705720) != 0):
                            self.state = 133
                            self.expression(0)


                        self.state = 136
                        self.match(SPLVParser.Colon)
                        self.state = 138
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2281705720) != 0):
                            self.state = 137
                            self.expression(0)


                        self.state = 140
                        self.match(SPLVParser.BracketRight)
                        pass

             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(SPLVParser.Identifier)
            self.state = 147
            self.match(SPLVParser.ParenLeft)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2281705720) != 0):
                self.state = 148
                self.expression(0)
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 149
                        self.match(SPLVParser.Comma)
                        self.state = 150
                        self.expression(0) 
                    self.state = 155
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 156
                    self.match(SPLVParser.Comma)




            self.state = 161
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
        self.enterRule(localctx, 16, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 163
                self.match(SPLVParser.GlobalTypeModifier)


            self.state = 166
            self.match(SPLVParser.Type)
            self.state = 167
            self.match(SPLVParser.Identifier)
            self.state = 168
            self.match(SPLVParser.AssignmentOperator)
            self.state = 169
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
        self.enterRule(localctx, 18, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(SPLVParser.Identifier)
            self.state = 172
            self.match(SPLVParser.AssignmentOperator)
            self.state = 173
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

        def CurlyRight(self):
            return self.getToken(SPLVParser.CurlyRight, 0)

        def statementInblock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.StatementInblockContext)
            else:
                return self.getTypedRuleContext(SPLVParser.StatementInblockContext,i)


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
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(SPLVParser.CurlyLeft)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 229384) != 0):
                self.state = 176
                self.statementInblock()
                self.state = 177
                self.match(SPLVParser.Semicolon)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(SPLVParser.CurlyRight)
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

        def returnStatement(self):
            return self.getTypedRuleContext(SPLVParser.ReturnStatementContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Semicolon)
            else:
                return self.getToken(SPLVParser.Semicolon, i)

        def CurlyRight(self):
            return self.getToken(SPLVParser.CurlyRight, 0)

        def statementInFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.StatementInFunctionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.StatementInFunctionContext,i)


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
        self.enterRule(localctx, 22, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(SPLVParser.CurlyLeft)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5472264) != 0):
                self.state = 187
                self.statementInFunction()
                self.state = 188
                self.match(SPLVParser.Semicolon)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.returnStatement()
            self.state = 196
            self.match(SPLVParser.Semicolon)
            self.state = 197
            self.match(SPLVParser.CurlyRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidFunctionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CurlyLeft(self):
            return self.getToken(SPLVParser.CurlyLeft, 0)

        def voidReturnStatement(self):
            return self.getTypedRuleContext(SPLVParser.VoidReturnStatementContext,0)


        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Semicolon)
            else:
                return self.getToken(SPLVParser.Semicolon, i)

        def CurlyRight(self):
            return self.getToken(SPLVParser.CurlyRight, 0)

        def statementInFunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.StatementInFunctionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.StatementInFunctionContext,i)


        def getRuleIndex(self):
            return SPLVParser.RULE_voidFunctionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidFunctionBlock" ):
                listener.enterVoidFunctionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidFunctionBlock" ):
                listener.exitVoidFunctionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidFunctionBlock" ):
                return visitor.visitVoidFunctionBlock(self)
            else:
                return visitor.visitChildren(self)




    def voidFunctionBlock(self):

        localctx = SPLVParser.VoidFunctionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_voidFunctionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(SPLVParser.CurlyLeft)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5472264) != 0):
                self.state = 200
                self.statementInFunction()
                self.state = 201
                self.match(SPLVParser.Semicolon)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.voidReturnStatement()
            self.state = 209
            self.match(SPLVParser.Semicolon)
            self.state = 210
            self.match(SPLVParser.CurlyRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ReturnKeyword(self):
            return self.getToken(SPLVParser.ReturnKeyword, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_voidReturnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidReturnStatement" ):
                listener.enterVoidReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidReturnStatement" ):
                listener.exitVoidReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidReturnStatement" ):
                return visitor.visitVoidReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def voidReturnStatement(self):

        localctx = SPLVParser.VoidReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_voidReturnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(SPLVParser.ReturnKeyword)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ReturnKeyword(self):
            return self.getToken(SPLVParser.ReturnKeyword, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = SPLVParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(SPLVParser.ReturnKeyword)
            self.state = 215
            self.expression(0)
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


        def getRuleIndex(self):
            return SPLVParser.RULE_functionDefinition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VoidFunctionContext(FunctionDefinitionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.FunctionDefinitionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FunctionKeyword(self):
            return self.getToken(SPLVParser.FunctionKeyword, 0)
        def VoidType(self):
            return self.getToken(SPLVParser.VoidType, 0)
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
        def voidFunctionBlock(self):
            return self.getTypedRuleContext(SPLVParser.VoidFunctionBlockContext,0)

        def Type(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Type)
            else:
                return self.getToken(SPLVParser.Type, i)
        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Comma)
            else:
                return self.getToken(SPLVParser.Comma, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidFunction" ):
                listener.enterVoidFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidFunction" ):
                listener.exitVoidFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidFunction" ):
                return visitor.visitVoidFunction(self)
            else:
                return visitor.visitChildren(self)


    class ReturningFunctionContext(FunctionDefinitionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.FunctionDefinitionContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturningFunction" ):
                listener.enterReturningFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturningFunction" ):
                listener.exitReturningFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturningFunction" ):
                return visitor.visitReturningFunction(self)
            else:
                return visitor.visitChildren(self)



    def functionDefinition(self):

        localctx = SPLVParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = SPLVParser.ReturningFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(SPLVParser.FunctionKeyword)
                self.state = 218
                self.match(SPLVParser.Type)
                self.state = 219
                self.match(SPLVParser.Colon)
                self.state = 220
                self.match(SPLVParser.Identifier)
                self.state = 221
                self.match(SPLVParser.ParenLeft)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 222
                    self.match(SPLVParser.Type)
                    self.state = 223
                    self.match(SPLVParser.Identifier)
                    self.state = 229
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 224
                            self.match(SPLVParser.Comma)
                            self.state = 225
                            self.match(SPLVParser.Type)
                            self.state = 226
                            self.match(SPLVParser.Identifier) 
                        self.state = 231
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==25:
                        self.state = 232
                        self.match(SPLVParser.Comma)




                self.state = 237
                self.match(SPLVParser.ParenRight)
                self.state = 238
                self.functionBlock()
                pass

            elif la_ == 2:
                localctx = SPLVParser.VoidFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(SPLVParser.FunctionKeyword)
                self.state = 240
                self.match(SPLVParser.VoidType)
                self.state = 241
                self.match(SPLVParser.Colon)
                self.state = 242
                self.match(SPLVParser.Identifier)
                self.state = 243
                self.match(SPLVParser.ParenLeft)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 244
                    self.match(SPLVParser.Type)
                    self.state = 245
                    self.match(SPLVParser.Identifier)
                    self.state = 251
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 246
                            self.match(SPLVParser.Comma)
                            self.state = 247
                            self.match(SPLVParser.Type)
                            self.state = 248
                            self.match(SPLVParser.Identifier) 
                        self.state = 253
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==25:
                        self.state = 254
                        self.match(SPLVParser.Comma)




                self.state = 259
                self.match(SPLVParser.ParenRight)
                self.state = 260
                self.voidFunctionBlock()
                pass


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
        self.enterRule(localctx, 32, self.RULE_controlStatement)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
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
        self.enterRule(localctx, 34, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(SPLVParser.IfKeyword)
            self.state = 269
            self.match(SPLVParser.ParenLeft)
            self.state = 270
            self.expression(0)
            self.state = 271
            self.match(SPLVParser.ParenRight)
            self.state = 272
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
        self.enterRule(localctx, 36, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(SPLVParser.WhileKeyword)
            self.state = 275
            self.match(SPLVParser.ParenLeft)
            self.state = 276
            self.expression(0)
            self.state = 277
            self.match(SPLVParser.ParenRight)
            self.state = 278
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
        self.enterRule(localctx, 38, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(SPLVParser.LoopKeyword)
            self.state = 281
            self.match(SPLVParser.ParenLeft)
            self.state = 282
            self.match(SPLVParser.Type)
            self.state = 283
            self.match(SPLVParser.Identifier)
            self.state = 284
            self.match(SPLVParser.InOperator)
            self.state = 285
            self.expression(0)
            self.state = 286
            self.match(SPLVParser.ParenRight)
            self.state = 287
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
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




