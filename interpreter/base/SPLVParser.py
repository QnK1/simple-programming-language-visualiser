# Generated from d:/Users/Kacper/Desktop/SPLV/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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
        4,1,37,345,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,4,0,54,
        8,0,11,0,12,0,55,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,71,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,83,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,98,8,3,
        1,4,1,4,1,4,1,4,1,4,3,4,105,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,5,5,117,8,5,10,5,12,5,120,9,5,1,5,3,5,123,8,5,1,5,1,5,1,
        5,1,5,3,5,129,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,140,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,152,8,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,177,8,7,1,7,1,7,3,7,181,8,7,1,7,5,7,184,8,
        7,10,7,12,7,187,9,7,1,8,1,8,1,8,1,8,1,8,5,8,194,8,8,10,8,12,8,197,
        9,8,1,8,3,8,200,8,8,3,8,202,8,8,1,8,1,8,1,9,3,9,207,8,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,215,8,9,1,9,1,9,1,9,3,9,220,8,9,1,10,1,10,1,
        10,1,10,1,11,1,11,4,11,228,8,11,11,11,12,11,229,1,11,1,11,1,12,1,
        12,4,12,236,8,12,11,12,12,12,237,1,12,1,12,1,13,1,13,1,13,3,13,245,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,3,14,261,8,14,1,15,1,15,1,15,5,15,266,8,15,10,15,12,15,
        269,9,15,1,15,3,15,272,8,15,3,15,274,8,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,3,16,283,8,16,1,17,1,17,1,17,1,18,1,18,1,18,3,18,291,
        8,18,1,19,1,19,1,19,3,19,296,8,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,305,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        328,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,0,1,14,26,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,0,375,0,53,1,0,0,0,2,
        70,1,0,0,0,4,82,1,0,0,0,6,97,1,0,0,0,8,104,1,0,0,0,10,128,1,0,0,
        0,12,139,1,0,0,0,14,151,1,0,0,0,16,188,1,0,0,0,18,219,1,0,0,0,20,
        221,1,0,0,0,22,225,1,0,0,0,24,233,1,0,0,0,26,244,1,0,0,0,28,260,
        1,0,0,0,30,273,1,0,0,0,32,282,1,0,0,0,34,284,1,0,0,0,36,290,1,0,
        0,0,38,295,1,0,0,0,40,297,1,0,0,0,42,306,1,0,0,0,44,312,1,0,0,0,
        46,321,1,0,0,0,48,329,1,0,0,0,50,335,1,0,0,0,52,54,3,2,1,0,53,52,
        1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,
        57,58,5,0,0,1,58,1,1,0,0,0,59,60,3,18,9,0,60,61,5,28,0,0,61,71,1,
        0,0,0,62,63,3,20,10,0,63,64,5,28,0,0,64,71,1,0,0,0,65,71,3,28,14,
        0,66,67,3,16,8,0,67,68,5,28,0,0,68,71,1,0,0,0,69,71,3,36,18,0,70,
        59,1,0,0,0,70,62,1,0,0,0,70,65,1,0,0,0,70,66,1,0,0,0,70,69,1,0,0,
        0,71,3,1,0,0,0,72,73,3,20,10,0,73,74,5,28,0,0,74,83,1,0,0,0,75,76,
        3,18,9,0,76,77,5,28,0,0,77,83,1,0,0,0,78,79,3,16,8,0,79,80,5,28,
        0,0,80,83,1,0,0,0,81,83,3,36,18,0,82,72,1,0,0,0,82,75,1,0,0,0,82,
        78,1,0,0,0,82,81,1,0,0,0,83,5,1,0,0,0,84,85,3,20,10,0,85,86,5,28,
        0,0,86,98,1,0,0,0,87,88,3,16,8,0,88,89,5,28,0,0,89,98,1,0,0,0,90,
        91,3,18,9,0,91,92,5,28,0,0,92,98,1,0,0,0,93,98,3,36,18,0,94,95,3,
        26,13,0,95,96,5,28,0,0,96,98,1,0,0,0,97,84,1,0,0,0,97,87,1,0,0,0,
        97,90,1,0,0,0,97,93,1,0,0,0,97,94,1,0,0,0,98,7,1,0,0,0,99,105,5,
        3,0,0,100,105,5,4,0,0,101,105,5,6,0,0,102,105,5,5,0,0,103,105,3,
        10,5,0,104,99,1,0,0,0,104,100,1,0,0,0,104,101,1,0,0,0,104,102,1,
        0,0,0,104,103,1,0,0,0,105,9,1,0,0,0,106,107,5,32,0,0,107,108,3,14,
        7,0,108,109,5,31,0,0,109,110,3,14,7,0,110,111,5,33,0,0,111,129,1,
        0,0,0,112,113,5,32,0,0,113,118,3,14,7,0,114,115,5,30,0,0,115,117,
        3,14,7,0,116,114,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,121,123,5,30,0,0,122,121,
        1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,5,33,0,0,125,129,
        1,0,0,0,126,127,5,32,0,0,127,129,5,33,0,0,128,106,1,0,0,0,128,112,
        1,0,0,0,128,126,1,0,0,0,129,11,1,0,0,0,130,140,5,20,0,0,131,140,
        5,21,0,0,132,140,5,22,0,0,133,140,5,23,0,0,134,135,5,24,0,0,135,
        136,5,32,0,0,136,137,3,12,6,0,137,138,5,33,0,0,138,140,1,0,0,0,139,
        130,1,0,0,0,139,131,1,0,0,0,139,132,1,0,0,0,139,133,1,0,0,0,139,
        134,1,0,0,0,140,13,1,0,0,0,141,142,6,7,-1,0,142,152,3,8,4,0,143,
        152,3,16,8,0,144,152,5,27,0,0,145,146,5,36,0,0,146,147,3,14,7,0,
        147,148,5,37,0,0,148,152,1,0,0,0,149,150,5,11,0,0,150,152,3,14,7,
        6,151,141,1,0,0,0,151,143,1,0,0,0,151,144,1,0,0,0,151,145,1,0,0,
        0,151,149,1,0,0,0,152,185,1,0,0,0,153,154,10,5,0,0,154,155,5,9,0,
        0,155,184,3,14,7,6,156,157,10,4,0,0,157,158,5,10,0,0,158,184,3,14,
        7,5,159,160,10,3,0,0,160,161,5,8,0,0,161,184,3,14,7,4,162,163,10,
        2,0,0,163,164,5,7,0,0,164,184,3,14,7,3,165,166,10,1,0,0,166,167,
        5,13,0,0,167,184,3,14,7,2,168,169,10,9,0,0,169,170,5,32,0,0,170,
        171,3,14,7,0,171,172,5,33,0,0,172,184,1,0,0,0,173,174,10,8,0,0,174,
        176,5,32,0,0,175,177,3,14,7,0,176,175,1,0,0,0,176,177,1,0,0,0,177,
        178,1,0,0,0,178,180,5,29,0,0,179,181,3,14,7,0,180,179,1,0,0,0,180,
        181,1,0,0,0,181,182,1,0,0,0,182,184,5,33,0,0,183,153,1,0,0,0,183,
        156,1,0,0,0,183,159,1,0,0,0,183,162,1,0,0,0,183,165,1,0,0,0,183,
        168,1,0,0,0,183,173,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,
        186,1,0,0,0,186,15,1,0,0,0,187,185,1,0,0,0,188,189,5,27,0,0,189,
        201,5,36,0,0,190,195,3,14,7,0,191,192,5,30,0,0,192,194,3,14,7,0,
        193,191,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,
        196,199,1,0,0,0,197,195,1,0,0,0,198,200,5,30,0,0,199,198,1,0,0,0,
        199,200,1,0,0,0,200,202,1,0,0,0,201,190,1,0,0,0,201,202,1,0,0,0,
        202,203,1,0,0,0,203,204,5,37,0,0,204,17,1,0,0,0,205,207,5,26,0,0,
        206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,209,3,12,6,0,
        209,210,5,27,0,0,210,211,5,12,0,0,211,212,3,14,7,0,212,220,1,0,0,
        0,213,215,5,26,0,0,214,213,1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,
        0,216,217,3,12,6,0,217,218,5,27,0,0,218,220,1,0,0,0,219,206,1,0,
        0,0,219,214,1,0,0,0,220,19,1,0,0,0,221,222,5,27,0,0,222,223,5,12,
        0,0,223,224,3,14,7,0,224,21,1,0,0,0,225,227,5,34,0,0,226,228,3,4,
        2,0,227,226,1,0,0,0,228,229,1,0,0,0,229,227,1,0,0,0,229,230,1,0,
        0,0,230,231,1,0,0,0,231,232,5,35,0,0,232,23,1,0,0,0,233,235,5,34,
        0,0,234,236,3,6,3,0,235,234,1,0,0,0,236,237,1,0,0,0,237,235,1,0,
        0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,35,0,0,240,25,1,0,
        0,0,241,242,5,19,0,0,242,245,3,14,7,0,243,245,5,19,0,0,244,241,1,
        0,0,0,244,243,1,0,0,0,245,27,1,0,0,0,246,247,5,18,0,0,247,248,3,
        32,16,0,248,249,5,36,0,0,249,250,3,30,15,0,250,251,5,37,0,0,251,
        252,3,24,12,0,252,261,1,0,0,0,253,254,5,18,0,0,254,255,3,32,16,0,
        255,256,5,36,0,0,256,257,3,30,15,0,257,258,5,37,0,0,258,259,3,24,
        12,0,259,261,1,0,0,0,260,246,1,0,0,0,260,253,1,0,0,0,261,29,1,0,
        0,0,262,267,3,34,17,0,263,264,5,30,0,0,264,266,3,34,17,0,265,263,
        1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,271,
        1,0,0,0,269,267,1,0,0,0,270,272,5,30,0,0,271,270,1,0,0,0,271,272,
        1,0,0,0,272,274,1,0,0,0,273,262,1,0,0,0,273,274,1,0,0,0,274,31,1,
        0,0,0,275,276,3,12,6,0,276,277,5,29,0,0,277,278,5,27,0,0,278,283,
        1,0,0,0,279,280,5,25,0,0,280,281,5,29,0,0,281,283,5,27,0,0,282,275,
        1,0,0,0,282,279,1,0,0,0,283,33,1,0,0,0,284,285,3,12,6,0,285,286,
        5,27,0,0,286,35,1,0,0,0,287,291,3,40,20,0,288,291,3,42,21,0,289,
        291,3,44,22,0,290,287,1,0,0,0,290,288,1,0,0,0,290,289,1,0,0,0,291,
        37,1,0,0,0,292,296,3,46,23,0,293,296,3,48,24,0,294,296,3,50,25,0,
        295,292,1,0,0,0,295,293,1,0,0,0,295,294,1,0,0,0,296,39,1,0,0,0,297,
        298,5,14,0,0,298,299,5,36,0,0,299,300,3,14,7,0,300,301,5,37,0,0,
        301,304,3,22,11,0,302,303,5,15,0,0,303,305,3,22,11,0,304,302,1,0,
        0,0,304,305,1,0,0,0,305,41,1,0,0,0,306,307,5,17,0,0,307,308,5,36,
        0,0,308,309,3,14,7,0,309,310,5,37,0,0,310,311,3,22,11,0,311,43,1,
        0,0,0,312,313,5,16,0,0,313,314,5,36,0,0,314,315,3,12,6,0,315,316,
        5,27,0,0,316,317,5,13,0,0,317,318,3,14,7,0,318,319,5,37,0,0,319,
        320,3,22,11,0,320,45,1,0,0,0,321,322,5,14,0,0,322,323,5,36,0,0,323,
        324,3,14,7,0,324,327,5,37,0,0,325,326,5,15,0,0,326,328,3,24,12,0,
        327,325,1,0,0,0,327,328,1,0,0,0,328,47,1,0,0,0,329,330,5,17,0,0,
        330,331,5,36,0,0,331,332,3,14,7,0,332,333,5,37,0,0,333,334,3,24,
        12,0,334,49,1,0,0,0,335,336,5,16,0,0,336,337,5,36,0,0,337,338,3,
        12,6,0,338,339,5,27,0,0,339,340,5,13,0,0,340,341,3,14,7,0,341,342,
        5,37,0,0,342,343,3,24,12,0,343,51,1,0,0,0,32,55,70,82,97,104,118,
        122,128,139,151,176,180,183,185,195,199,201,206,214,219,229,237,
        244,260,267,271,273,282,290,295,304,327
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

    ruleNames =  [ "program", "statement", "statementInControlBlock", "statementInFunction", 
                   "literal", "listLiteral", "type", "expression", "functionCall", 
                   "variableDefinition", "variableAssignment", "controlBlock", 
                   "functionBlock", "returnStatement", "functionDefinition", 
                   "functionArgumentList", "functionIdentifier", "functionArgument", 
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
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.statement()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234307584) != 0)):
                    break

            self.state = 57
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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.variableDefinition()
                self.state = 60
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.variableAssignment()
                self.state = 63
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.functionCall()
                self.state = 67
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.variableAssignment()
                self.state = 73
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.variableDefinition()
                self.state = 76
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.functionCall()
                self.state = 79
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
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
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.variableAssignment()
                self.state = 85
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.functionCall()
                self.state = 88
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.variableDefinition()
                self.state = 91
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.controlStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.returnStatement()
                self.state = 95
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
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(SPLVParser.BoolLiteral)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 103
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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(SPLVParser.BracketLeft)
                self.state = 107
                self.expression(0)
                self.state = 108
                self.match(SPLVParser.DoubleDot)
                self.state = 109
                self.expression(0)
                self.state = 110
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(SPLVParser.BracketLeft)
                self.state = 113
                self.expression(0)
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 114
                        self.match(SPLVParser.Comma)
                        self.state = 115
                        self.expression(0) 
                    self.state = 120
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 121
                    self.match(SPLVParser.Comma)


                self.state = 124
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(SPLVParser.BracketLeft)
                self.state = 127
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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(SPLVParser.IntType)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(SPLVParser.FloatType)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(SPLVParser.StringType)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.match(SPLVParser.BoolType)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.match(SPLVParser.ListType)
                self.state = 135
                self.match(SPLVParser.BracketLeft)
                self.state = 136
                self.type_()
                self.state = 137
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

        def literal(self):
            return self.getTypedRuleContext(SPLVParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SPLVParser.FunctionCallContext,0)


        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

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

        def ComparisonOperator(self):
            return self.getToken(SPLVParser.ComparisonOperator, 0)

        def BooleanOperator(self):
            return self.getToken(SPLVParser.BooleanOperator, 0)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 142
                self.literal()
                pass

            elif la_ == 2:
                self.state = 143
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 144
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 4:
                self.state = 145
                self.match(SPLVParser.ParenLeft)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(SPLVParser.ParenRight)
                pass

            elif la_ == 5:
                self.state = 149
                self.match(SPLVParser.NOTOperator)
                self.state = 150
                self.expression(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 183
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 153
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 154
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 155
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 156
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 157
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 158
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 159
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 160
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 161
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 163
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 164
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 166
                        self.match(SPLVParser.InOperator)
                        self.state = 167
                        self.expression(2)
                        pass

                    elif la_ == 6:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 169
                        self.match(SPLVParser.BracketLeft)
                        self.state = 170
                        self.expression(0)
                        self.state = 171
                        self.match(SPLVParser.BracketRight)
                        pass

                    elif la_ == 7:
                        localctx = SPLVParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 174
                        self.match(SPLVParser.BracketLeft)
                        self.state = 176
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 175
                            self.expression(0)


                        self.state = 178
                        self.match(SPLVParser.Colon)
                        self.state = 180
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 179
                            self.expression(0)


                        self.state = 182
                        self.match(SPLVParser.BracketRight)
                        pass

             
                self.state = 187
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
            self.state = 188
            self.match(SPLVParser.Identifier)
            self.state = 189
            self.match(SPLVParser.ParenLeft)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                self.state = 190
                self.expression(0)
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 191
                        self.match(SPLVParser.Comma)
                        self.state = 192
                        self.expression(0) 
                    self.state = 197
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 198
                    self.match(SPLVParser.Comma)




            self.state = 203
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
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 205
                    self.match(SPLVParser.GlobalTypeModifier)


                self.state = 208
                self.type_()
                self.state = 209
                self.match(SPLVParser.Identifier)
                self.state = 210
                self.match(SPLVParser.AssignmentOperator)
                self.state = 211
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 213
                    self.match(SPLVParser.GlobalTypeModifier)


                self.state = 216
                self.type_()
                self.state = 217
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
            self.state = 221
            self.match(SPLVParser.Identifier)
            self.state = 222
            self.match(SPLVParser.AssignmentOperator)
            self.state = 223
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
            self.state = 225
            self.match(SPLVParser.CurlyLeft)
            self.state = 227 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 226
                self.statementInControlBlock()
                self.state = 229 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234045440) != 0)):
                    break

            self.state = 231
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
            self.state = 233
            self.match(SPLVParser.CurlyLeft)
            self.state = 235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.statementInFunction()
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234569728) != 0)):
                    break

            self.state = 239
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
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(SPLVParser.ReturnKeyword)
                self.state = 242
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(SPLVParser.FunctionKeyword)
                self.state = 247
                self.functionIdentifier()
                self.state = 248
                self.match(SPLVParser.ParenLeft)
                self.state = 249
                self.functionArgumentList()
                self.state = 250
                self.match(SPLVParser.ParenRight)
                self.state = 251
                self.functionBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(SPLVParser.FunctionKeyword)
                self.state = 254
                self.functionIdentifier()
                self.state = 255
                self.match(SPLVParser.ParenLeft)
                self.state = 256
                self.functionArgumentList()
                self.state = 257
                self.match(SPLVParser.ParenRight)
                self.state = 258
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
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0):
                self.state = 262
                self.functionArgument()
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 263
                        self.match(SPLVParser.Comma)
                        self.state = 264
                        self.functionArgument() 
                    self.state = 269
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 270
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
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.type_()
                self.state = 276
                self.match(SPLVParser.Colon)
                self.state = 277
                self.match(SPLVParser.Identifier)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(SPLVParser.VoidType)
                self.state = 280
                self.match(SPLVParser.Colon)
                self.state = 281
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
            self.state = 284
            self.type_()
            self.state = 285
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
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
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
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.ifStatementInsideFunction()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.whileStatementInsideFunction()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
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
            self.state = 297
            self.match(SPLVParser.IfKeyword)
            self.state = 298
            self.match(SPLVParser.ParenLeft)
            self.state = 299
            self.expression(0)
            self.state = 300
            self.match(SPLVParser.ParenRight)
            self.state = 301
            self.controlBlock()
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 302
                self.match(SPLVParser.ElseKeyword)
                self.state = 303
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
            self.state = 306
            self.match(SPLVParser.WhileKeyword)
            self.state = 307
            self.match(SPLVParser.ParenLeft)
            self.state = 308
            self.expression(0)
            self.state = 309
            self.match(SPLVParser.ParenRight)
            self.state = 310
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

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


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
        self.enterRule(localctx, 44, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(SPLVParser.LoopKeyword)
            self.state = 313
            self.match(SPLVParser.ParenLeft)
            self.state = 314
            self.type_()
            self.state = 315
            self.match(SPLVParser.Identifier)
            self.state = 316
            self.match(SPLVParser.InOperator)
            self.state = 317
            self.expression(0)
            self.state = 318
            self.match(SPLVParser.ParenRight)
            self.state = 319
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
            self.state = 321
            self.match(SPLVParser.IfKeyword)
            self.state = 322
            self.match(SPLVParser.ParenLeft)
            self.state = 323
            self.expression(0)
            self.state = 324
            self.match(SPLVParser.ParenRight)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 325
                self.match(SPLVParser.ElseKeyword)
                self.state = 326
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
            self.state = 329
            self.match(SPLVParser.WhileKeyword)
            self.state = 330
            self.match(SPLVParser.ParenLeft)
            self.state = 331
            self.expression(0)
            self.state = 332
            self.match(SPLVParser.ParenRight)
            self.state = 333
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

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


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
        self.enterRule(localctx, 50, self.RULE_loopStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(SPLVParser.LoopKeyword)
            self.state = 336
            self.match(SPLVParser.ParenLeft)
            self.state = 337
            self.type_()
            self.state = 338
            self.match(SPLVParser.Identifier)
            self.state = 339
            self.match(SPLVParser.InOperator)
            self.state = 340
            self.expression(0)
            self.state = 341
            self.match(SPLVParser.ParenRight)
            self.state = 342
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
        self._predicates[7] = self.expression_sempred
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
         




