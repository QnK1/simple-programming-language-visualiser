# Generated from d:/Desktop/tkik_new/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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
        4,1,32,318,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,63,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,75,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,90,8,3,1,4,1,4,1,4,1,4,1,4,3,4,97,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,109,8,5,10,5,12,5,112,9,5,1,
        5,3,5,115,8,5,1,5,1,5,1,5,1,5,3,5,121,8,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,133,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,158,
        8,6,1,6,1,6,3,6,162,8,6,1,6,5,6,165,8,6,10,6,12,6,168,9,6,1,7,1,
        7,1,7,1,7,1,7,5,7,175,8,7,10,7,12,7,178,9,7,1,7,3,7,181,8,7,3,7,
        183,8,7,1,7,1,7,1,8,3,8,188,8,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,10,1,10,4,10,201,8,10,11,10,12,10,202,1,10,1,10,1,11,1,11,
        4,11,209,8,11,11,11,12,11,210,1,11,1,11,1,12,1,12,1,12,3,12,218,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,230,
        8,13,10,13,12,13,233,9,13,1,13,3,13,236,8,13,3,13,238,8,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,252,
        8,13,10,13,12,13,255,9,13,1,13,3,13,258,8,13,3,13,260,8,13,1,13,
        1,13,3,13,264,8,13,1,14,1,14,1,14,3,14,269,8,14,1,15,1,15,1,15,3,
        15,274,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,0,1,12,22,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,0,0,346,0,45,1,0,0,0,2,62,
        1,0,0,0,4,74,1,0,0,0,6,89,1,0,0,0,8,96,1,0,0,0,10,120,1,0,0,0,12,
        132,1,0,0,0,14,169,1,0,0,0,16,187,1,0,0,0,18,194,1,0,0,0,20,198,
        1,0,0,0,22,206,1,0,0,0,24,217,1,0,0,0,26,263,1,0,0,0,28,268,1,0,
        0,0,30,273,1,0,0,0,32,275,1,0,0,0,34,281,1,0,0,0,36,287,1,0,0,0,
        38,296,1,0,0,0,40,302,1,0,0,0,42,308,1,0,0,0,44,46,3,2,1,0,45,44,
        1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,
        49,50,5,0,0,1,50,1,1,0,0,0,51,52,3,16,8,0,52,53,5,23,0,0,53,63,1,
        0,0,0,54,55,3,18,9,0,55,56,5,23,0,0,56,63,1,0,0,0,57,63,3,26,13,
        0,58,59,3,14,7,0,59,60,5,23,0,0,60,63,1,0,0,0,61,63,3,28,14,0,62,
        51,1,0,0,0,62,54,1,0,0,0,62,57,1,0,0,0,62,58,1,0,0,0,62,61,1,0,0,
        0,63,3,1,0,0,0,64,65,3,18,9,0,65,66,5,23,0,0,66,75,1,0,0,0,67,68,
        3,16,8,0,68,69,5,23,0,0,69,75,1,0,0,0,70,71,3,14,7,0,71,72,5,23,
        0,0,72,75,1,0,0,0,73,75,3,28,14,0,74,64,1,0,0,0,74,67,1,0,0,0,74,
        70,1,0,0,0,74,73,1,0,0,0,75,5,1,0,0,0,76,77,3,18,9,0,77,78,5,23,
        0,0,78,90,1,0,0,0,79,80,3,14,7,0,80,81,5,23,0,0,81,90,1,0,0,0,82,
        83,3,16,8,0,83,84,5,23,0,0,84,90,1,0,0,0,85,90,3,28,14,0,86,87,3,
        24,12,0,87,88,5,23,0,0,88,90,1,0,0,0,89,76,1,0,0,0,89,79,1,0,0,0,
        89,82,1,0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,90,7,1,0,0,0,91,97,5,3,
        0,0,92,97,5,4,0,0,93,97,5,6,0,0,94,97,5,5,0,0,95,97,3,10,5,0,96,
        91,1,0,0,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,
        0,97,9,1,0,0,0,98,99,5,27,0,0,99,100,3,12,6,0,100,101,5,26,0,0,101,
        102,3,12,6,0,102,103,5,28,0,0,103,121,1,0,0,0,104,105,5,27,0,0,105,
        110,3,12,6,0,106,107,5,25,0,0,107,109,3,12,6,0,108,106,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,113,115,5,25,0,0,114,113,1,0,0,0,114,115,1,0,0,0,115,
        116,1,0,0,0,116,117,5,28,0,0,117,121,1,0,0,0,118,119,5,27,0,0,119,
        121,5,28,0,0,120,98,1,0,0,0,120,104,1,0,0,0,120,118,1,0,0,0,121,
        11,1,0,0,0,122,123,6,6,-1,0,123,133,3,8,4,0,124,133,5,22,0,0,125,
        133,3,14,7,0,126,127,5,31,0,0,127,128,3,12,6,0,128,129,5,32,0,0,
        129,133,1,0,0,0,130,131,5,11,0,0,131,133,3,12,6,6,132,122,1,0,0,
        0,132,124,1,0,0,0,132,125,1,0,0,0,132,126,1,0,0,0,132,130,1,0,0,
        0,133,166,1,0,0,0,134,135,10,5,0,0,135,136,5,10,0,0,136,165,3,12,
        6,6,137,138,10,4,0,0,138,139,5,9,0,0,139,165,3,12,6,5,140,141,10,
        3,0,0,141,142,5,8,0,0,142,165,3,12,6,4,143,144,10,2,0,0,144,145,
        5,7,0,0,145,165,3,12,6,3,146,147,10,1,0,0,147,148,5,13,0,0,148,165,
        3,12,6,2,149,150,10,9,0,0,150,151,5,27,0,0,151,152,3,12,6,0,152,
        153,5,28,0,0,153,165,1,0,0,0,154,155,10,8,0,0,155,157,5,27,0,0,156,
        158,3,12,6,0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,
        161,5,24,0,0,160,162,3,12,6,0,161,160,1,0,0,0,161,162,1,0,0,0,162,
        163,1,0,0,0,163,165,5,28,0,0,164,134,1,0,0,0,164,137,1,0,0,0,164,
        140,1,0,0,0,164,143,1,0,0,0,164,146,1,0,0,0,164,149,1,0,0,0,164,
        154,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,
        13,1,0,0,0,168,166,1,0,0,0,169,170,5,22,0,0,170,182,5,31,0,0,171,
        176,3,12,6,0,172,173,5,25,0,0,173,175,3,12,6,0,174,172,1,0,0,0,175,
        178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,180,1,0,0,0,178,
        176,1,0,0,0,179,181,5,25,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,
        183,1,0,0,0,182,171,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,
        185,5,32,0,0,185,15,1,0,0,0,186,188,5,21,0,0,187,186,1,0,0,0,187,
        188,1,0,0,0,188,189,1,0,0,0,189,190,5,19,0,0,190,191,5,22,0,0,191,
        192,5,12,0,0,192,193,3,12,6,0,193,17,1,0,0,0,194,195,5,22,0,0,195,
        196,5,12,0,0,196,197,3,12,6,0,197,19,1,0,0,0,198,200,5,29,0,0,199,
        201,3,4,2,0,200,199,1,0,0,0,201,202,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,204,1,0,0,0,204,205,5,30,0,0,205,21,1,0,0,0,206,
        208,5,29,0,0,207,209,3,6,3,0,208,207,1,0,0,0,209,210,1,0,0,0,210,
        208,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,213,5,30,0,0,213,
        23,1,0,0,0,214,215,5,18,0,0,215,218,3,12,6,0,216,218,5,18,0,0,217,
        214,1,0,0,0,217,216,1,0,0,0,218,25,1,0,0,0,219,220,5,17,0,0,220,
        221,5,19,0,0,221,222,5,24,0,0,222,223,5,22,0,0,223,237,5,31,0,0,
        224,225,5,19,0,0,225,231,5,22,0,0,226,227,5,25,0,0,227,228,5,19,
        0,0,228,230,5,22,0,0,229,226,1,0,0,0,230,233,1,0,0,0,231,229,1,0,
        0,0,231,232,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,234,236,5,25,
        0,0,235,234,1,0,0,0,235,236,1,0,0,0,236,238,1,0,0,0,237,224,1,0,
        0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,32,0,0,240,264,3,22,
        11,0,241,242,5,17,0,0,242,243,5,20,0,0,243,244,5,24,0,0,244,245,
        5,22,0,0,245,259,5,31,0,0,246,247,5,19,0,0,247,253,5,22,0,0,248,
        249,5,25,0,0,249,250,5,19,0,0,250,252,5,22,0,0,251,248,1,0,0,0,252,
        255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,257,1,0,0,0,255,
        253,1,0,0,0,256,258,5,25,0,0,257,256,1,0,0,0,257,258,1,0,0,0,258,
        260,1,0,0,0,259,246,1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,
        262,5,32,0,0,262,264,3,22,11,0,263,219,1,0,0,0,263,241,1,0,0,0,264,
        27,1,0,0,0,265,269,3,32,16,0,266,269,3,34,17,0,267,269,3,36,18,0,
        268,265,1,0,0,0,268,266,1,0,0,0,268,267,1,0,0,0,269,29,1,0,0,0,270,
        274,3,38,19,0,271,274,3,40,20,0,272,274,3,42,21,0,273,270,1,0,0,
        0,273,271,1,0,0,0,273,272,1,0,0,0,274,31,1,0,0,0,275,276,5,14,0,
        0,276,277,5,31,0,0,277,278,3,12,6,0,278,279,5,32,0,0,279,280,3,20,
        10,0,280,33,1,0,0,0,281,282,5,16,0,0,282,283,5,31,0,0,283,284,3,
        12,6,0,284,285,5,32,0,0,285,286,3,20,10,0,286,35,1,0,0,0,287,288,
        5,15,0,0,288,289,5,31,0,0,289,290,5,19,0,0,290,291,5,22,0,0,291,
        292,5,13,0,0,292,293,3,12,6,0,293,294,5,32,0,0,294,295,3,20,10,0,
        295,37,1,0,0,0,296,297,5,14,0,0,297,298,5,31,0,0,298,299,3,12,6,
        0,299,300,5,32,0,0,300,301,3,22,11,0,301,39,1,0,0,0,302,303,5,16,
        0,0,303,304,5,31,0,0,304,305,3,12,6,0,305,306,5,32,0,0,306,307,3,
        22,11,0,307,41,1,0,0,0,308,309,5,15,0,0,309,310,5,31,0,0,310,311,
        5,19,0,0,311,312,5,22,0,0,312,313,5,13,0,0,313,314,3,12,6,0,314,
        315,5,32,0,0,315,316,3,22,11,0,316,43,1,0,0,0,29,47,62,74,89,96,
        110,114,120,132,157,161,164,166,176,180,182,187,202,210,217,231,
        235,237,253,257,259,263,268,273
    ]

class SPLVParser ( Parser ):

    grammarFileName = "SPLVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'not'", "'='", 
                     "'in'", "'if'", "'lop'", "'whl'", "'fun'", "'ret'", 
                     "<INVALID>", "'nul'", "'glo'", "<INVALID>", "';'", 
                     "':'", "','", "'..'", "'['", "']'", "'{'", "'}'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "Comment", "IntLiteral", "FloatLiteral", 
                      "BoolLiteral", "StringLiteral", "AdditiveOperator", 
                      "MultiplicativeOperator", "ComparisonOperator", "BooleanOperator", 
                      "NOTOperator", "AssignmentOperator", "InOperator", 
                      "IfKeyword", "LoopKeyword", "WhileKeyword", "FunctionKeyword", 
                      "ReturnKeyword", "Type", "VoidType", "GlobalTypeModifier", 
                      "Identifier", "Semicolon", "Colon", "Comma", "DoubleDot", 
                      "BracketLeft", "BracketRight", "CurlyLeft", "CurlyRight", 
                      "ParenLeft", "ParenRight" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementInControlBlock = 2
    RULE_statementInFunction = 3
    RULE_literal = 4
    RULE_listLiteral = 5
    RULE_expression = 6
    RULE_functionCall = 7
    RULE_variableDefinition = 8
    RULE_variableAssignment = 9
    RULE_controlBlock = 10
    RULE_functionBlock = 11
    RULE_returnStatement = 12
    RULE_functionDefinition = 13
    RULE_controlStatement = 14
    RULE_controlStatementInsideFunction = 15
    RULE_ifStatement = 16
    RULE_whileStatement = 17
    RULE_loopStatement = 18
    RULE_ifStatementInsideFunction = 19
    RULE_whileStatementInsideFunction = 20
    RULE_loopStatementInsideFunction = 21

    ruleNames =  [ "program", "statement", "statementInControlBlock", "statementInFunction", 
                   "literal", "listLiteral", "expression", "functionCall", 
                   "variableDefinition", "variableAssignment", "controlBlock", 
                   "functionBlock", "returnStatement", "functionDefinition", 
                   "controlStatement", "controlStatementInsideFunction", 
                   "ifStatement", "whileStatement", "loopStatement", "ifStatementInsideFunction", 
                   "whileStatementInsideFunction", "loopStatementInsideFunction" ]

    EOF = Token.EOF
    WS=1
    Comment=2
    IntLiteral=3
    FloatLiteral=4
    BoolLiteral=5
    StringLiteral=6
    AdditiveOperator=7
    MultiplicativeOperator=8
    ComparisonOperator=9
    BooleanOperator=10
    NOTOperator=11
    AssignmentOperator=12
    InOperator=13
    IfKeyword=14
    LoopKeyword=15
    WhileKeyword=16
    FunctionKeyword=17
    ReturnKeyword=18
    Type=19
    VoidType=20
    GlobalTypeModifier=21
    Identifier=22
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
            while True:
                self.state = 44
                self.statement()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7061504) != 0)):
                    break

            self.state = 49
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


        def Semicolon(self):
            return self.getToken(SPLVParser.Semicolon, 0)

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
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.variableDefinition()
                self.state = 52
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.variableAssignment()
                self.state = 55
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.functionCall()
                self.state = 59
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.controlStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementInControlBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableAssignment(self):
            return self.getTypedRuleContext(SPLVParser.VariableAssignmentContext,0)


        def Semicolon(self):
            return self.getToken(SPLVParser.Semicolon, 0)

        def variableDefinition(self):
            return self.getTypedRuleContext(SPLVParser.VariableDefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def controlStatement(self):
            return self.getTypedRuleContext(SPLVParser.ControlStatementContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_statementInControlBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementInControlBlock" ):
                listener.enterStatementInControlBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementInControlBlock" ):
                listener.exitStatementInControlBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementInControlBlock" ):
                return visitor.visitStatementInControlBlock(self)
            else:
                return visitor.visitChildren(self)




    def statementInControlBlock(self):

        localctx = SPLVParser.StatementInControlBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementInControlBlock)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.variableAssignment()
                self.state = 65
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.variableDefinition()
                self.state = 68
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.functionCall()
                self.state = 71
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
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


        def Semicolon(self):
            return self.getToken(SPLVParser.Semicolon, 0)

        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(SPLVParser.VariableDefinitionContext,0)


        def controlStatement(self):
            return self.getTypedRuleContext(SPLVParser.ControlStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(SPLVParser.ReturnStatementContext,0)


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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.variableAssignment()
                self.state = 77
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.functionCall()
                self.state = 80
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.variableDefinition()
                self.state = 83
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.controlStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.returnStatement()
                self.state = 87
                self.match(SPLVParser.Semicolon)
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
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.match(SPLVParser.BoolLiteral)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(SPLVParser.BracketLeft)
                self.state = 99
                self.expression(0)
                self.state = 100
                self.match(SPLVParser.DoubleDot)
                self.state = 101
                self.expression(0)
                self.state = 102
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(SPLVParser.BracketLeft)
                self.state = 105
                self.expression(0)
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 106
                        self.match(SPLVParser.Comma)
                        self.state = 107
                        self.expression(0) 
                    self.state = 112
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 113
                    self.match(SPLVParser.Comma)


                self.state = 116
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(SPLVParser.BracketLeft)
                self.state = 119
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

        def BooleanOperator(self):
            return self.getToken(SPLVParser.BooleanOperator, 0)

        def ComparisonOperator(self):
            return self.getToken(SPLVParser.ComparisonOperator, 0)

        def MultiplicativeOperator(self):
            return self.getToken(SPLVParser.MultiplicativeOperator, 0)

        def AdditiveOperator(self):
            return self.getToken(SPLVParser.AdditiveOperator, 0)

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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 123
                self.literal()
                pass

            elif la_ == 2:
                self.state = 124
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 3:
                self.state = 125
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 126
                self.match(SPLVParser.ParenLeft)
                self.state = 127
                self.expression(0)
                self.state = 128
                self.match(SPLVParser.ParenRight)
                pass

            elif la_ == 5:
                self.state = 130
                self.match(SPLVParser.NOTOperator)
                self.state = 131
                self.expression(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 134
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 135
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 136
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 137
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 138
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 139
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 140
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 141
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 142
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 143
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 144
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 145
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 146
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 147
                        self.match(SPLVParser.InOperator)
                        self.state = 148
                        self.expression(2)
                        pass

                    elif la_ == 6:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 149
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 150
                        self.match(SPLVParser.BracketLeft)
                        self.state = 151
                        self.expression(0)
                        self.state = 152
                        self.match(SPLVParser.BracketRight)
                        pass

                    elif la_ == 7:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 155
                        self.match(SPLVParser.BracketLeft)
                        self.state = 157
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2285897848) != 0):
                            self.state = 156
                            self.expression(0)


                        self.state = 159
                        self.match(SPLVParser.Colon)
                        self.state = 161
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2285897848) != 0):
                            self.state = 160
                            self.expression(0)


                        self.state = 163
                        self.match(SPLVParser.BracketRight)
                        pass

             
                self.state = 168
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
            self.state = 169
            self.match(SPLVParser.Identifier)
            self.state = 170
            self.match(SPLVParser.ParenLeft)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2285897848) != 0):
                self.state = 171
                self.expression(0)
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 172
                        self.match(SPLVParser.Comma)
                        self.state = 173
                        self.expression(0) 
                    self.state = 178
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 179
                    self.match(SPLVParser.Comma)




            self.state = 184
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
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 186
                self.match(SPLVParser.GlobalTypeModifier)


            self.state = 189
            self.match(SPLVParser.Type)
            self.state = 190
            self.match(SPLVParser.Identifier)
            self.state = 191
            self.match(SPLVParser.AssignmentOperator)
            self.state = 192
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
            self.state = 194
            self.match(SPLVParser.Identifier)
            self.state = 195
            self.match(SPLVParser.AssignmentOperator)
            self.state = 196
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CurlyLeft(self):
            return self.getToken(SPLVParser.CurlyLeft, 0)

        def CurlyRight(self):
            return self.getToken(SPLVParser.CurlyRight, 0)

        def statementInControlBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.StatementInControlBlockContext)
            else:
                return self.getTypedRuleContext(SPLVParser.StatementInControlBlockContext,i)


        def getRuleIndex(self):
            return SPLVParser.RULE_controlBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlBlock" ):
                listener.enterControlBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlBlock" ):
                listener.exitControlBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlBlock" ):
                return visitor.visitControlBlock(self)
            else:
                return visitor.visitChildren(self)




    def controlBlock(self):

        localctx = SPLVParser.ControlBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_controlBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(SPLVParser.CurlyLeft)
            self.state = 200 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 199
                self.statementInControlBlock()
                self.state = 202 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6930432) != 0)):
                    break

            self.state = 204
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
            self.state = 206
            self.match(SPLVParser.CurlyLeft)
            self.state = 208 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 207
                self.statementInFunction()
                self.state = 210 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7192576) != 0)):
                    break

            self.state = 212
            self.match(SPLVParser.CurlyRight)
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
        self.enterRule(localctx, 24, self.RULE_returnStatement)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(SPLVParser.ReturnKeyword)
                self.state = 215
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(SPLVParser.ReturnKeyword)
                pass


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
        def functionBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionBlockContext,0)

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
        self.enterRule(localctx, 26, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = SPLVParser.ReturningFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(SPLVParser.FunctionKeyword)
                self.state = 220
                self.match(SPLVParser.Type)
                self.state = 221
                self.match(SPLVParser.Colon)
                self.state = 222
                self.match(SPLVParser.Identifier)
                self.state = 223
                self.match(SPLVParser.ParenLeft)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 224
                    self.match(SPLVParser.Type)
                    self.state = 225
                    self.match(SPLVParser.Identifier)
                    self.state = 231
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 226
                            self.match(SPLVParser.Comma)
                            self.state = 227
                            self.match(SPLVParser.Type)
                            self.state = 228
                            self.match(SPLVParser.Identifier) 
                        self.state = 233
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==25:
                        self.state = 234
                        self.match(SPLVParser.Comma)




                self.state = 239
                self.match(SPLVParser.ParenRight)
                self.state = 240
                self.functionBlock()
                pass

            elif la_ == 2:
                localctx = SPLVParser.VoidFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(SPLVParser.FunctionKeyword)
                self.state = 242
                self.match(SPLVParser.VoidType)
                self.state = 243
                self.match(SPLVParser.Colon)
                self.state = 244
                self.match(SPLVParser.Identifier)
                self.state = 245
                self.match(SPLVParser.ParenLeft)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 246
                    self.match(SPLVParser.Type)
                    self.state = 247
                    self.match(SPLVParser.Identifier)
                    self.state = 253
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 248
                            self.match(SPLVParser.Comma)
                            self.state = 249
                            self.match(SPLVParser.Type)
                            self.state = 250
                            self.match(SPLVParser.Identifier) 
                        self.state = 255
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==25:
                        self.state = 256
                        self.match(SPLVParser.Comma)




                self.state = 261
                self.match(SPLVParser.ParenRight)
                self.state = 262
                self.functionBlock()
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
        self.enterRule(localctx, 28, self.RULE_controlStatement)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.ifStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.whileStatement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
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


    class ControlStatementInsideFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatementInsideFunction(self):
            return self.getTypedRuleContext(SPLVParser.IfStatementInsideFunctionContext,0)


        def whileStatementInsideFunction(self):
            return self.getTypedRuleContext(SPLVParser.WhileStatementInsideFunctionContext,0)


        def loopStatementInsideFunction(self):
            return self.getTypedRuleContext(SPLVParser.LoopStatementInsideFunctionContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_controlStatementInsideFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlStatementInsideFunction" ):
                listener.enterControlStatementInsideFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlStatementInsideFunction" ):
                listener.exitControlStatementInsideFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlStatementInsideFunction" ):
                return visitor.visitControlStatementInsideFunction(self)
            else:
                return visitor.visitChildren(self)




    def controlStatementInsideFunction(self):

        localctx = SPLVParser.ControlStatementInsideFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_controlStatementInsideFunction)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.ifStatementInsideFunction()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.whileStatementInsideFunction()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.loopStatementInsideFunction()
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

        def controlBlock(self):
            return self.getTypedRuleContext(SPLVParser.ControlBlockContext,0)


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
        self.enterRule(localctx, 32, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(SPLVParser.IfKeyword)
            self.state = 276
            self.match(SPLVParser.ParenLeft)
            self.state = 277
            self.expression(0)
            self.state = 278
            self.match(SPLVParser.ParenRight)
            self.state = 279
            self.controlBlock()
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

        def controlBlock(self):
            return self.getTypedRuleContext(SPLVParser.ControlBlockContext,0)


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
        self.enterRule(localctx, 34, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(SPLVParser.WhileKeyword)
            self.state = 282
            self.match(SPLVParser.ParenLeft)
            self.state = 283
            self.expression(0)
            self.state = 284
            self.match(SPLVParser.ParenRight)
            self.state = 285
            self.controlBlock()
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

        def controlBlock(self):
            return self.getTypedRuleContext(SPLVParser.ControlBlockContext,0)


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
        self.enterRule(localctx, 36, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(SPLVParser.LoopKeyword)
            self.state = 288
            self.match(SPLVParser.ParenLeft)
            self.state = 289
            self.match(SPLVParser.Type)
            self.state = 290
            self.match(SPLVParser.Identifier)
            self.state = 291
            self.match(SPLVParser.InOperator)
            self.state = 292
            self.expression(0)
            self.state = 293
            self.match(SPLVParser.ParenRight)
            self.state = 294
            self.controlBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementInsideFunctionContext(ParserRuleContext):
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

        def functionBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionBlockContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_ifStatementInsideFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatementInsideFunction" ):
                listener.enterIfStatementInsideFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatementInsideFunction" ):
                listener.exitIfStatementInsideFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatementInsideFunction" ):
                return visitor.visitIfStatementInsideFunction(self)
            else:
                return visitor.visitChildren(self)




    def ifStatementInsideFunction(self):

        localctx = SPLVParser.IfStatementInsideFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(SPLVParser.IfKeyword)
            self.state = 297
            self.match(SPLVParser.ParenLeft)
            self.state = 298
            self.expression(0)
            self.state = 299
            self.match(SPLVParser.ParenRight)
            self.state = 300
            self.functionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementInsideFunctionContext(ParserRuleContext):
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

        def functionBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionBlockContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_whileStatementInsideFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatementInsideFunction" ):
                listener.enterWhileStatementInsideFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatementInsideFunction" ):
                listener.exitWhileStatementInsideFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatementInsideFunction" ):
                return visitor.visitWhileStatementInsideFunction(self)
            else:
                return visitor.visitChildren(self)




    def whileStatementInsideFunction(self):

        localctx = SPLVParser.WhileStatementInsideFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_whileStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(SPLVParser.WhileKeyword)
            self.state = 303
            self.match(SPLVParser.ParenLeft)
            self.state = 304
            self.expression(0)
            self.state = 305
            self.match(SPLVParser.ParenRight)
            self.state = 306
            self.functionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementInsideFunctionContext(ParserRuleContext):
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

        def functionBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionBlockContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_loopStatementInsideFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatementInsideFunction" ):
                listener.enterLoopStatementInsideFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatementInsideFunction" ):
                listener.exitLoopStatementInsideFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatementInsideFunction" ):
                return visitor.visitLoopStatementInsideFunction(self)
            else:
                return visitor.visitChildren(self)




    def loopStatementInsideFunction(self):

        localctx = SPLVParser.LoopStatementInsideFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_loopStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(SPLVParser.LoopKeyword)
            self.state = 309
            self.match(SPLVParser.ParenLeft)
            self.state = 310
            self.match(SPLVParser.Type)
            self.state = 311
            self.match(SPLVParser.Identifier)
            self.state = 312
            self.match(SPLVParser.InOperator)
            self.state = 313
            self.expression(0)
            self.state = 314
            self.match(SPLVParser.ParenRight)
            self.state = 315
            self.functionBlock()
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




