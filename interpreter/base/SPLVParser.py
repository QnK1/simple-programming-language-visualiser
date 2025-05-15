# Generated from d:/Desktop/tkik_new/simple_programming_language_visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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
        4,1,37,346,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,4,0,56,8,0,11,0,12,0,57,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,85,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,100,8,3,1,4,1,4,1,4,1,4,1,4,3,4,107,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,119,8,5,10,5,12,5,122,9,5,1,5,3,5,125,8,
        5,1,5,1,5,1,5,1,5,3,5,131,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,142,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,154,8,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,179,8,7,1,7,1,7,3,7,183,8,7,1,
        7,5,7,186,8,7,10,7,12,7,189,9,7,1,8,1,8,1,8,1,8,1,8,5,8,196,8,8,
        10,8,12,8,199,9,8,1,8,3,8,202,8,8,3,8,204,8,8,1,8,1,8,1,9,3,9,209,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,217,8,9,1,9,1,9,1,9,3,9,222,8,9,
        1,10,1,10,1,10,1,10,1,11,1,11,4,11,230,8,11,11,11,12,11,231,1,11,
        1,11,1,12,1,12,4,12,238,8,12,11,12,12,12,239,1,12,1,12,1,13,1,13,
        1,13,3,13,247,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,263,8,14,1,15,1,15,1,15,5,15,268,8,
        15,10,15,12,15,271,9,15,1,15,3,15,274,8,15,3,15,276,8,15,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,3,16,285,8,16,1,17,1,17,1,17,1,18,1,
        18,1,18,3,18,293,8,18,1,19,1,19,1,19,3,19,298,8,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,3,20,307,8,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        327,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,26,1,26,0,1,14,27,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,0,375,
        0,55,1,0,0,0,2,72,1,0,0,0,4,84,1,0,0,0,6,99,1,0,0,0,8,106,1,0,0,
        0,10,130,1,0,0,0,12,141,1,0,0,0,14,153,1,0,0,0,16,190,1,0,0,0,18,
        221,1,0,0,0,20,223,1,0,0,0,22,227,1,0,0,0,24,235,1,0,0,0,26,246,
        1,0,0,0,28,262,1,0,0,0,30,275,1,0,0,0,32,284,1,0,0,0,34,286,1,0,
        0,0,36,292,1,0,0,0,38,297,1,0,0,0,40,299,1,0,0,0,42,308,1,0,0,0,
        44,314,1,0,0,0,46,320,1,0,0,0,48,328,1,0,0,0,50,334,1,0,0,0,52,340,
        1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,
        57,58,1,0,0,0,58,59,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,62,3,18,
        9,0,62,63,5,28,0,0,63,73,1,0,0,0,64,65,3,20,10,0,65,66,5,28,0,0,
        66,73,1,0,0,0,67,73,3,28,14,0,68,69,3,16,8,0,69,70,5,28,0,0,70,73,
        1,0,0,0,71,73,3,36,18,0,72,61,1,0,0,0,72,64,1,0,0,0,72,67,1,0,0,
        0,72,68,1,0,0,0,72,71,1,0,0,0,73,3,1,0,0,0,74,75,3,20,10,0,75,76,
        5,28,0,0,76,85,1,0,0,0,77,78,3,18,9,0,78,79,5,28,0,0,79,85,1,0,0,
        0,80,81,3,16,8,0,81,82,5,28,0,0,82,85,1,0,0,0,83,85,3,36,18,0,84,
        74,1,0,0,0,84,77,1,0,0,0,84,80,1,0,0,0,84,83,1,0,0,0,85,5,1,0,0,
        0,86,87,3,20,10,0,87,88,5,28,0,0,88,100,1,0,0,0,89,90,3,16,8,0,90,
        91,5,28,0,0,91,100,1,0,0,0,92,93,3,18,9,0,93,94,5,28,0,0,94,100,
        1,0,0,0,95,100,3,36,18,0,96,97,3,26,13,0,97,98,5,28,0,0,98,100,1,
        0,0,0,99,86,1,0,0,0,99,89,1,0,0,0,99,92,1,0,0,0,99,95,1,0,0,0,99,
        96,1,0,0,0,100,7,1,0,0,0,101,107,5,3,0,0,102,107,5,4,0,0,103,107,
        5,6,0,0,104,107,5,5,0,0,105,107,3,10,5,0,106,101,1,0,0,0,106,102,
        1,0,0,0,106,103,1,0,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,9,1,
        0,0,0,108,109,5,32,0,0,109,110,3,14,7,0,110,111,5,31,0,0,111,112,
        3,14,7,0,112,113,5,33,0,0,113,131,1,0,0,0,114,115,5,32,0,0,115,120,
        3,14,7,0,116,117,5,30,0,0,117,119,3,14,7,0,118,116,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,124,1,0,0,0,122,120,
        1,0,0,0,123,125,5,30,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,126,
        1,0,0,0,126,127,5,33,0,0,127,131,1,0,0,0,128,129,5,32,0,0,129,131,
        5,33,0,0,130,108,1,0,0,0,130,114,1,0,0,0,130,128,1,0,0,0,131,11,
        1,0,0,0,132,142,5,20,0,0,133,142,5,21,0,0,134,142,5,22,0,0,135,142,
        5,23,0,0,136,137,5,24,0,0,137,138,5,32,0,0,138,139,3,12,6,0,139,
        140,5,33,0,0,140,142,1,0,0,0,141,132,1,0,0,0,141,133,1,0,0,0,141,
        134,1,0,0,0,141,135,1,0,0,0,141,136,1,0,0,0,142,13,1,0,0,0,143,144,
        6,7,-1,0,144,154,5,27,0,0,145,154,3,8,4,0,146,154,3,16,8,0,147,148,
        5,11,0,0,148,154,3,14,7,4,149,150,5,36,0,0,150,151,3,14,7,0,151,
        152,5,37,0,0,152,154,1,0,0,0,153,143,1,0,0,0,153,145,1,0,0,0,153,
        146,1,0,0,0,153,147,1,0,0,0,153,149,1,0,0,0,154,187,1,0,0,0,155,
        156,10,7,0,0,156,157,5,8,0,0,157,186,3,14,7,8,158,159,10,6,0,0,159,
        160,5,7,0,0,160,186,3,14,7,7,161,162,10,5,0,0,162,163,5,13,0,0,163,
        186,3,14,7,6,164,165,10,3,0,0,165,166,5,9,0,0,166,186,3,14,7,4,167,
        168,10,2,0,0,168,169,5,10,0,0,169,186,3,14,7,3,170,171,10,10,0,0,
        171,172,5,32,0,0,172,173,3,14,7,0,173,174,5,33,0,0,174,186,1,0,0,
        0,175,176,10,9,0,0,176,178,5,32,0,0,177,179,3,14,7,0,178,177,1,0,
        0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,182,5,29,0,0,181,183,3,14,
        7,0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,186,5,33,
        0,0,185,155,1,0,0,0,185,158,1,0,0,0,185,161,1,0,0,0,185,164,1,0,
        0,0,185,167,1,0,0,0,185,170,1,0,0,0,185,175,1,0,0,0,186,189,1,0,
        0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,15,1,0,0,0,189,187,1,0,0,
        0,190,191,5,27,0,0,191,203,5,36,0,0,192,197,3,14,7,0,193,194,5,30,
        0,0,194,196,3,14,7,0,195,193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,
        0,0,197,198,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,200,202,5,30,
        0,0,201,200,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,192,1,0,
        0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,37,0,0,206,17,1,0,
        0,0,207,209,5,26,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,1,0,
        0,0,210,211,3,12,6,0,211,212,5,27,0,0,212,213,5,12,0,0,213,214,3,
        14,7,0,214,222,1,0,0,0,215,217,5,26,0,0,216,215,1,0,0,0,216,217,
        1,0,0,0,217,218,1,0,0,0,218,219,3,12,6,0,219,220,5,27,0,0,220,222,
        1,0,0,0,221,208,1,0,0,0,221,216,1,0,0,0,222,19,1,0,0,0,223,224,5,
        27,0,0,224,225,5,12,0,0,225,226,3,14,7,0,226,21,1,0,0,0,227,229,
        5,34,0,0,228,230,3,4,2,0,229,228,1,0,0,0,230,231,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,234,5,35,0,0,234,23,
        1,0,0,0,235,237,5,34,0,0,236,238,3,6,3,0,237,236,1,0,0,0,238,239,
        1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,242,
        5,35,0,0,242,25,1,0,0,0,243,244,5,19,0,0,244,247,3,14,7,0,245,247,
        5,19,0,0,246,243,1,0,0,0,246,245,1,0,0,0,247,27,1,0,0,0,248,249,
        5,18,0,0,249,250,3,32,16,0,250,251,5,36,0,0,251,252,3,30,15,0,252,
        253,5,37,0,0,253,254,3,24,12,0,254,263,1,0,0,0,255,256,5,18,0,0,
        256,257,3,32,16,0,257,258,5,36,0,0,258,259,3,30,15,0,259,260,5,37,
        0,0,260,261,3,24,12,0,261,263,1,0,0,0,262,248,1,0,0,0,262,255,1,
        0,0,0,263,29,1,0,0,0,264,269,3,34,17,0,265,266,5,30,0,0,266,268,
        3,34,17,0,267,265,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,
        1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,272,274,5,30,0,0,273,272,
        1,0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,275,264,1,0,0,0,275,276,
        1,0,0,0,276,31,1,0,0,0,277,278,3,12,6,0,278,279,5,29,0,0,279,280,
        5,27,0,0,280,285,1,0,0,0,281,282,5,25,0,0,282,283,5,29,0,0,283,285,
        5,27,0,0,284,277,1,0,0,0,284,281,1,0,0,0,285,33,1,0,0,0,286,287,
        3,12,6,0,287,288,5,27,0,0,288,35,1,0,0,0,289,293,3,40,20,0,290,293,
        3,42,21,0,291,293,3,44,22,0,292,289,1,0,0,0,292,290,1,0,0,0,292,
        291,1,0,0,0,293,37,1,0,0,0,294,298,3,46,23,0,295,298,3,48,24,0,296,
        298,3,50,25,0,297,294,1,0,0,0,297,295,1,0,0,0,297,296,1,0,0,0,298,
        39,1,0,0,0,299,300,5,14,0,0,300,301,5,36,0,0,301,302,3,14,7,0,302,
        303,5,37,0,0,303,306,3,22,11,0,304,305,5,15,0,0,305,307,3,22,11,
        0,306,304,1,0,0,0,306,307,1,0,0,0,307,41,1,0,0,0,308,309,5,17,0,
        0,309,310,5,36,0,0,310,311,3,14,7,0,311,312,5,37,0,0,312,313,3,22,
        11,0,313,43,1,0,0,0,314,315,5,16,0,0,315,316,5,36,0,0,316,317,3,
        52,26,0,317,318,5,37,0,0,318,319,3,22,11,0,319,45,1,0,0,0,320,321,
        5,14,0,0,321,322,5,36,0,0,322,323,3,14,7,0,323,326,5,37,0,0,324,
        325,5,15,0,0,325,327,3,24,12,0,326,324,1,0,0,0,326,327,1,0,0,0,327,
        47,1,0,0,0,328,329,5,17,0,0,329,330,5,36,0,0,330,331,3,14,7,0,331,
        332,5,37,0,0,332,333,3,24,12,0,333,49,1,0,0,0,334,335,5,16,0,0,335,
        336,5,36,0,0,336,337,3,52,26,0,337,338,5,37,0,0,338,339,3,24,12,
        0,339,51,1,0,0,0,340,341,3,12,6,0,341,342,5,27,0,0,342,343,5,13,
        0,0,343,344,3,14,7,0,344,53,1,0,0,0,32,57,72,84,99,106,120,124,130,
        141,153,178,182,185,187,197,201,203,208,216,221,231,239,246,262,
        269,273,275,284,292,297,306,326
    ]

class SPLVParser ( Parser ):

    grammarFileName = "SPLVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'not'", "'='", 
                     "'in'", "'if'", "'els'", "'lop'", "'whl'", "'fun'", 
                     "'ret'", "'int'", "'flo'", "'str'", "'bol'", "'lst'", 
                     "'nul'", "'glo'", "<INVALID>", "';'", "':'", "','", 
                     "'..'", "'['", "']'", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "Comment", "IntLiteral", "FloatLiteral", 
                      "BoolLiteral", "StringLiteral", "AdditiveOperator", 
                      "MultiplicativeOperator", "ComparisonOperator", "BooleanOperator", 
                      "NOTOperator", "AssignmentOperator", "InOperator", 
                      "IfKeyword", "ElseKeyword", "LoopKeyword", "WhileKeyword", 
                      "FunctionKeyword", "ReturnKeyword", "IntType", "FloatType", 
                      "StringType", "BoolType", "ListType", "VoidType", 
                      "GlobalTypeModifier", "Identifier", "Semicolon", "Colon", 
                      "Comma", "DoubleDot", "BracketLeft", "BracketRight", 
                      "CurlyLeft", "CurlyRight", "ParenLeft", "ParenRight" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementInControlBlock = 2
    RULE_statementInFunction = 3
    RULE_literal = 4
    RULE_listLiteral = 5
    RULE_type = 6
    RULE_expression = 7
    RULE_functionCall = 8
    RULE_variableDefinition = 9
    RULE_variableAssignment = 10
    RULE_controlBlock = 11
    RULE_functionBlock = 12
    RULE_returnStatement = 13
    RULE_functionDefinition = 14
    RULE_functionArgumentList = 15
    RULE_functionIdentifier = 16
    RULE_functionArgument = 17
    RULE_controlStatement = 18
    RULE_controlStatementInsideFunction = 19
    RULE_ifStatement = 20
    RULE_whileStatement = 21
    RULE_loopStatement = 22
    RULE_ifStatementInsideFunction = 23
    RULE_whileStatementInsideFunction = 24
    RULE_loopStatementInsideFunction = 25
    RULE_loopStatementIterator = 26

    ruleNames =  [ "program", "statement", "statementInControlBlock", "statementInFunction", 
                   "literal", "listLiteral", "type", "expression", "functionCall", 
                   "variableDefinition", "variableAssignment", "controlBlock", 
                   "functionBlock", "returnStatement", "functionDefinition", 
                   "functionArgumentList", "functionIdentifier", "functionArgument", 
                   "controlStatement", "controlStatementInsideFunction", 
                   "ifStatement", "whileStatement", "loopStatement", "ifStatementInsideFunction", 
                   "whileStatementInsideFunction", "loopStatementInsideFunction", 
                   "loopStatementIterator" ]

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
    ElseKeyword=15
    LoopKeyword=16
    WhileKeyword=17
    FunctionKeyword=18
    ReturnKeyword=19
    IntType=20
    FloatType=21
    StringType=22
    BoolType=23
    ListType=24
    VoidType=25
    GlobalTypeModifier=26
    Identifier=27
    Semicolon=28
    Colon=29
    Comma=30
    DoubleDot=31
    BracketLeft=32
    BracketRight=33
    CurlyLeft=34
    CurlyRight=35
    ParenLeft=36
    ParenRight=37

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
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.statement()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234307584) != 0)):
                    break

            self.state = 59
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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.variableDefinition()
                self.state = 62
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.variableAssignment()
                self.state = 65
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.functionCall()
                self.state = 69
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.variableAssignment()
                self.state = 75
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.variableDefinition()
                self.state = 78
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.functionCall()
                self.state = 81
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.variableAssignment()
                self.state = 87
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.functionCall()
                self.state = 90
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.variableDefinition()
                self.state = 93
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.controlStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.returnStatement()
                self.state = 97
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
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(SPLVParser.BoolLiteral)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(SPLVParser.BracketLeft)
                self.state = 109
                self.expression(0)
                self.state = 110
                self.match(SPLVParser.DoubleDot)
                self.state = 111
                self.expression(0)
                self.state = 112
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(SPLVParser.BracketLeft)
                self.state = 115
                self.expression(0)
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 116
                        self.match(SPLVParser.Comma)
                        self.state = 117
                        self.expression(0) 
                    self.state = 122
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 123
                    self.match(SPLVParser.Comma)


                self.state = 126
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.match(SPLVParser.BracketLeft)
                self.state = 129
                self.match(SPLVParser.BracketRight)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntType(self):
            return self.getToken(SPLVParser.IntType, 0)

        def FloatType(self):
            return self.getToken(SPLVParser.FloatType, 0)

        def StringType(self):
            return self.getToken(SPLVParser.StringType, 0)

        def BoolType(self):
            return self.getToken(SPLVParser.BoolType, 0)

        def ListType(self):
            return self.getToken(SPLVParser.ListType, 0)

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = SPLVParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(SPLVParser.IntType)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(SPLVParser.FloatType)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(SPLVParser.StringType)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(SPLVParser.BoolType)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.match(SPLVParser.ListType)
                self.state = 137
                self.match(SPLVParser.BracketLeft)
                self.state = 138
                self.type_()
                self.state = 139
                self.match(SPLVParser.BracketRight)
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SPLVParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesesExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)
        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)

        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesesExpression" ):
                listener.enterParenthesesExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesesExpression" ):
                listener.exitParenthesesExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesesExpression" ):
                return visitor.visitParenthesesExpression(self)
            else:
                return visitor.visitChildren(self)


    class InOperatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def InOperator(self):
            return self.getToken(SPLVParser.InOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInOperatorExpression" ):
                listener.enterInOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInOperatorExpression" ):
                listener.exitInOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInOperatorExpression" ):
                return visitor.visitInOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveOperatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def AdditiveOperator(self):
            return self.getToken(SPLVParser.AdditiveOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveOperatorExpression" ):
                listener.enterAdditiveOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveOperatorExpression" ):
                listener.exitAdditiveOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveOperatorExpression" ):
                return visitor.visitAdditiveOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonOperatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def ComparisonOperator(self):
            return self.getToken(SPLVParser.ComparisonOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperatorExpression" ):
                listener.enterComparisonOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperatorExpression" ):
                listener.exitComparisonOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperatorExpression" ):
                return visitor.visitComparisonOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeOperatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def MultiplicativeOperator(self):
            return self.getToken(SPLVParser.MultiplicativeOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeOperatorExpression" ):
                listener.enterMultiplicativeOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeOperatorExpression" ):
                listener.exitMultiplicativeOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeOperatorExpression" ):
                return visitor.visitMultiplicativeOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanOperatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def BooleanOperator(self):
            return self.getToken(SPLVParser.BooleanOperator, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanOperatorExpression" ):
                listener.enterBooleanOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanOperatorExpression" ):
                listener.exitBooleanOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanOperatorExpression" ):
                return visitor.visitBooleanOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class ListSlicingExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)
        def Colon(self):
            return self.getToken(SPLVParser.Colon, 0)
        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListSlicingExpression" ):
                listener.enterListSlicingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListSlicingExpression" ):
                listener.exitListSlicingExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListSlicingExpression" ):
                return visitor.visitListSlicingExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotOperatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTOperator(self):
            return self.getToken(SPLVParser.NOTOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotOperatorExpression" ):
                listener.enterNotOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotOperatorExpression" ):
                listener.exitNotOperatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotOperatorExpression" ):
                return visitor.visitNotOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class ListIndexingExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)
        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListIndexingExpression" ):
                listener.enterListIndexingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListIndexingExpression" ):
                listener.exitListIndexingExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIndexingExpression" ):
                return visitor.visitListIndexingExpression(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(SPLVParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpression" ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpression" ):
                listener.exitLiteralExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpression" ):
                return visitor.visitLiteralExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SPLVParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = SPLVParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 144
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 2:
                localctx = SPLVParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.literal()
                pass

            elif la_ == 3:
                localctx = SPLVParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = SPLVParser.NotOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(SPLVParser.NOTOperator)
                self.state = 148
                self.expression(4)
                pass

            elif la_ == 5:
                localctx = SPLVParser.ParenthesesExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(SPLVParser.ParenLeft)
                self.state = 150
                self.expression(0)
                self.state = 151
                self.match(SPLVParser.ParenRight)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.MultiplicativeOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 155
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 156
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 157
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.AdditiveOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 159
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 160
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.InOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 162
                        self.match(SPLVParser.InOperator)
                        self.state = 163
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ComparisonOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 165
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 166
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.BooleanOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 168
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 169
                        self.expression(3)
                        pass

                    elif la_ == 6:
                        localctx = SPLVParser.ListIndexingExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 171
                        self.match(SPLVParser.BracketLeft)
                        self.state = 172
                        self.expression(0)
                        self.state = 173
                        self.match(SPLVParser.BracketRight)
                        pass

                    elif la_ == 7:
                        localctx = SPLVParser.ListSlicingExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 176
                        self.match(SPLVParser.BracketLeft)
                        self.state = 178
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 177
                            self.expression(0)


                        self.state = 180
                        self.match(SPLVParser.Colon)
                        self.state = 182
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 181
                            self.expression(0)


                        self.state = 184
                        self.match(SPLVParser.BracketRight)
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(SPLVParser.Identifier)
            self.state = 191
            self.match(SPLVParser.ParenLeft)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                self.state = 192
                self.expression(0)
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 193
                        self.match(SPLVParser.Comma)
                        self.state = 194
                        self.expression(0) 
                    self.state = 199
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 200
                    self.match(SPLVParser.Comma)




            self.state = 205
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

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


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
        self.enterRule(localctx, 18, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 207
                    self.match(SPLVParser.GlobalTypeModifier)


                self.state = 210
                self.type_()
                self.state = 211
                self.match(SPLVParser.Identifier)
                self.state = 212
                self.match(SPLVParser.AssignmentOperator)
                self.state = 213
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 215
                    self.match(SPLVParser.GlobalTypeModifier)


                self.state = 218
                self.type_()
                self.state = 219
                self.match(SPLVParser.Identifier)
                pass


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
        self.enterRule(localctx, 20, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(SPLVParser.Identifier)
            self.state = 224
            self.match(SPLVParser.AssignmentOperator)
            self.state = 225
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
        self.enterRule(localctx, 22, self.RULE_controlBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(SPLVParser.CurlyLeft)
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 228
                self.statementInControlBlock()
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234045440) != 0)):
                    break

            self.state = 233
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
        self.enterRule(localctx, 24, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(SPLVParser.CurlyLeft)
            self.state = 237 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 236
                self.statementInFunction()
                self.state = 239 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234569728) != 0)):
                    break

            self.state = 241
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
        self.enterRule(localctx, 26, self.RULE_returnStatement)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(SPLVParser.ReturnKeyword)
                self.state = 244
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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

        def FunctionKeyword(self):
            return self.getToken(SPLVParser.FunctionKeyword, 0)

        def functionIdentifier(self):
            return self.getTypedRuleContext(SPLVParser.FunctionIdentifierContext,0)


        def ParenLeft(self):
            return self.getToken(SPLVParser.ParenLeft, 0)

        def functionArgumentList(self):
            return self.getTypedRuleContext(SPLVParser.FunctionArgumentListContext,0)


        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

        def functionBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionBlockContext,0)


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
        self.enterRule(localctx, 28, self.RULE_functionDefinition)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(SPLVParser.FunctionKeyword)
                self.state = 249
                self.functionIdentifier()
                self.state = 250
                self.match(SPLVParser.ParenLeft)
                self.state = 251
                self.functionArgumentList()
                self.state = 252
                self.match(SPLVParser.ParenRight)
                self.state = 253
                self.functionBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(SPLVParser.FunctionKeyword)
                self.state = 256
                self.functionIdentifier()
                self.state = 257
                self.match(SPLVParser.ParenLeft)
                self.state = 258
                self.functionArgumentList()
                self.state = 259
                self.match(SPLVParser.ParenRight)
                self.state = 260
                self.functionBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.FunctionArgumentContext)
            else:
                return self.getTypedRuleContext(SPLVParser.FunctionArgumentContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Comma)
            else:
                return self.getToken(SPLVParser.Comma, i)

        def getRuleIndex(self):
            return SPLVParser.RULE_functionArgumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgumentList" ):
                listener.enterFunctionArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgumentList" ):
                listener.exitFunctionArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgumentList" ):
                return visitor.visitFunctionArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def functionArgumentList(self):

        localctx = SPLVParser.FunctionArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0):
                self.state = 264
                self.functionArgument()
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 265
                        self.match(SPLVParser.Comma)
                        self.state = 266
                        self.functionArgument() 
                    self.state = 271
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 272
                    self.match(SPLVParser.Comma)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


        def Colon(self):
            return self.getToken(SPLVParser.Colon, 0)

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def VoidType(self):
            return self.getToken(SPLVParser.VoidType, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_functionIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionIdentifier" ):
                listener.enterFunctionIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionIdentifier" ):
                listener.exitFunctionIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionIdentifier" ):
                return visitor.visitFunctionIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def functionIdentifier(self):

        localctx = SPLVParser.FunctionIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionIdentifier)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.type_()
                self.state = 278
                self.match(SPLVParser.Colon)
                self.state = 279
                self.match(SPLVParser.Identifier)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(SPLVParser.VoidType)
                self.state = 282
                self.match(SPLVParser.Colon)
                self.state = 283
                self.match(SPLVParser.Identifier)
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


    class FunctionArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_functionArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgument" ):
                listener.enterFunctionArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgument" ):
                listener.exitFunctionArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgument" ):
                return visitor.visitFunctionArgument(self)
            else:
                return visitor.visitChildren(self)




    def functionArgument(self):

        localctx = SPLVParser.FunctionArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.type_()
            self.state = 287
            self.match(SPLVParser.Identifier)
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
        self.enterRule(localctx, 36, self.RULE_controlStatement)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
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
        self.enterRule(localctx, 38, self.RULE_controlStatementInsideFunction)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.ifStatementInsideFunction()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.whileStatementInsideFunction()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
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

        def controlBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ControlBlockContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ControlBlockContext,i)


        def ElseKeyword(self):
            return self.getToken(SPLVParser.ElseKeyword, 0)

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
        self.enterRule(localctx, 40, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(SPLVParser.IfKeyword)
            self.state = 300
            self.match(SPLVParser.ParenLeft)
            self.state = 301
            self.expression(0)
            self.state = 302
            self.match(SPLVParser.ParenRight)
            self.state = 303
            self.controlBlock()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 304
                self.match(SPLVParser.ElseKeyword)
                self.state = 305
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
        self.enterRule(localctx, 42, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(SPLVParser.WhileKeyword)
            self.state = 309
            self.match(SPLVParser.ParenLeft)
            self.state = 310
            self.expression(0)
            self.state = 311
            self.match(SPLVParser.ParenRight)
            self.state = 312
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

        def loopStatementIterator(self):
            return self.getTypedRuleContext(SPLVParser.LoopStatementIteratorContext,0)


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
        self.enterRule(localctx, 44, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(SPLVParser.LoopKeyword)
            self.state = 315
            self.match(SPLVParser.ParenLeft)
            self.state = 316
            self.loopStatementIterator()
            self.state = 317
            self.match(SPLVParser.ParenRight)
            self.state = 318
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

        def ElseKeyword(self):
            return self.getToken(SPLVParser.ElseKeyword, 0)

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
        self.enterRule(localctx, 46, self.RULE_ifStatementInsideFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(SPLVParser.IfKeyword)
            self.state = 321
            self.match(SPLVParser.ParenLeft)
            self.state = 322
            self.expression(0)
            self.state = 323
            self.match(SPLVParser.ParenRight)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 324
                self.match(SPLVParser.ElseKeyword)
                self.state = 325
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
        self.enterRule(localctx, 48, self.RULE_whileStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(SPLVParser.WhileKeyword)
            self.state = 329
            self.match(SPLVParser.ParenLeft)
            self.state = 330
            self.expression(0)
            self.state = 331
            self.match(SPLVParser.ParenRight)
            self.state = 332
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

        def loopStatementIterator(self):
            return self.getTypedRuleContext(SPLVParser.LoopStatementIteratorContext,0)


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
        self.enterRule(localctx, 50, self.RULE_loopStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(SPLVParser.LoopKeyword)
            self.state = 335
            self.match(SPLVParser.ParenLeft)
            self.state = 336
            self.loopStatementIterator()
            self.state = 337
            self.match(SPLVParser.ParenRight)
            self.state = 338
            self.functionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementIteratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def InOperator(self):
            return self.getToken(SPLVParser.InOperator, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SPLVParser.RULE_loopStatementIterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatementIterator" ):
                listener.enterLoopStatementIterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatementIterator" ):
                listener.exitLoopStatementIterator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatementIterator" ):
                return visitor.visitLoopStatementIterator(self)
            else:
                return visitor.visitChildren(self)




    def loopStatementIterator(self):

        localctx = SPLVParser.LoopStatementIteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_loopStatementIterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.type_()
            self.state = 341
            self.match(SPLVParser.Identifier)
            self.state = 342
            self.match(SPLVParser.InOperator)
            self.state = 343
            self.expression(0)
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
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         




