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
        4,1,38,365,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,4,0,64,8,0,11,0,12,0,
        65,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,81,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,105,8,3,1,4,1,4,1,4,1,4,1,4,3,4,
        112,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,124,8,5,10,5,
        12,5,127,9,5,1,5,3,5,130,8,5,1,5,1,5,1,5,1,5,3,5,136,8,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,147,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,159,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,179,8,7,1,7,1,7,3,7,183,
        8,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,191,8,7,10,7,12,7,194,9,7,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,204,8,9,10,9,12,9,207,9,9,1,9,3,9,
        210,8,9,3,9,212,8,9,1,10,3,10,215,8,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,
        234,8,12,10,12,12,12,237,9,12,1,13,1,13,4,13,241,8,13,11,13,12,13,
        242,1,13,1,13,1,14,1,14,4,14,249,8,14,11,14,12,14,250,1,14,1,14,
        1,15,1,15,4,15,257,8,15,11,15,12,15,258,1,15,1,15,1,16,1,16,1,16,
        3,16,266,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,3,17,282,8,17,1,18,1,18,1,18,5,18,287,8,18,10,
        18,12,18,290,9,18,1,18,3,18,293,8,18,3,18,295,8,18,1,19,1,19,1,19,
        1,19,1,20,1,20,3,20,303,8,20,1,21,1,21,1,21,1,22,1,22,1,22,3,22,
        311,8,22,1,23,1,23,1,23,3,23,316,8,23,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,3,24,325,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,
        26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,346,8,
        27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,
        30,1,30,1,30,1,30,1,30,1,30,0,2,14,24,31,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,
        0,389,0,63,1,0,0,0,2,80,1,0,0,0,4,89,1,0,0,0,6,104,1,0,0,0,8,111,
        1,0,0,0,10,135,1,0,0,0,12,146,1,0,0,0,14,158,1,0,0,0,16,195,1,0,
        0,0,18,211,1,0,0,0,20,214,1,0,0,0,22,221,1,0,0,0,24,225,1,0,0,0,
        26,238,1,0,0,0,28,246,1,0,0,0,30,254,1,0,0,0,32,265,1,0,0,0,34,281,
        1,0,0,0,36,294,1,0,0,0,38,296,1,0,0,0,40,302,1,0,0,0,42,304,1,0,
        0,0,44,310,1,0,0,0,46,315,1,0,0,0,48,317,1,0,0,0,50,326,1,0,0,0,
        52,332,1,0,0,0,54,338,1,0,0,0,56,347,1,0,0,0,58,353,1,0,0,0,60,359,
        1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,0,0,1,68,1,1,0,0,0,69,70,3,20,
        10,0,70,71,5,28,0,0,71,81,1,0,0,0,72,73,3,22,11,0,73,74,5,28,0,0,
        74,81,1,0,0,0,75,81,3,34,17,0,76,77,3,16,8,0,77,78,5,28,0,0,78,81,
        1,0,0,0,79,81,3,44,22,0,80,69,1,0,0,0,80,72,1,0,0,0,80,75,1,0,0,
        0,80,76,1,0,0,0,80,79,1,0,0,0,81,3,1,0,0,0,82,83,3,22,11,0,83,84,
        5,28,0,0,84,90,1,0,0,0,85,86,3,16,8,0,86,87,5,28,0,0,87,90,1,0,0,
        0,88,90,3,44,22,0,89,82,1,0,0,0,89,85,1,0,0,0,89,88,1,0,0,0,90,5,
        1,0,0,0,91,92,3,22,11,0,92,93,5,28,0,0,93,105,1,0,0,0,94,95,3,16,
        8,0,95,96,5,28,0,0,96,105,1,0,0,0,97,98,3,20,10,0,98,99,5,28,0,0,
        99,105,1,0,0,0,100,105,3,46,23,0,101,102,3,32,16,0,102,103,5,28,
        0,0,103,105,1,0,0,0,104,91,1,0,0,0,104,94,1,0,0,0,104,97,1,0,0,0,
        104,100,1,0,0,0,104,101,1,0,0,0,105,7,1,0,0,0,106,112,5,3,0,0,107,
        112,5,4,0,0,108,112,5,6,0,0,109,112,5,5,0,0,110,112,3,10,5,0,111,
        106,1,0,0,0,111,107,1,0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,
        110,1,0,0,0,112,9,1,0,0,0,113,114,5,32,0,0,114,115,3,14,7,0,115,
        116,5,31,0,0,116,117,3,14,7,0,117,118,5,33,0,0,118,136,1,0,0,0,119,
        120,5,32,0,0,120,125,3,14,7,0,121,122,5,30,0,0,122,124,3,14,7,0,
        123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,
        126,129,1,0,0,0,127,125,1,0,0,0,128,130,5,30,0,0,129,128,1,0,0,0,
        129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,33,0,0,132,136,1,0,0,0,
        133,134,5,32,0,0,134,136,5,33,0,0,135,113,1,0,0,0,135,119,1,0,0,
        0,135,133,1,0,0,0,136,11,1,0,0,0,137,147,5,20,0,0,138,147,5,21,0,
        0,139,147,5,22,0,0,140,147,5,23,0,0,141,142,5,24,0,0,142,143,5,32,
        0,0,143,144,3,12,6,0,144,145,5,33,0,0,145,147,1,0,0,0,146,137,1,
        0,0,0,146,138,1,0,0,0,146,139,1,0,0,0,146,140,1,0,0,0,146,141,1,
        0,0,0,147,13,1,0,0,0,148,149,6,7,-1,0,149,159,5,27,0,0,150,159,3,
        8,4,0,151,159,3,16,8,0,152,153,5,11,0,0,153,159,3,14,7,4,154,155,
        5,36,0,0,155,156,3,14,7,0,156,157,5,37,0,0,157,159,1,0,0,0,158,148,
        1,0,0,0,158,150,1,0,0,0,158,151,1,0,0,0,158,152,1,0,0,0,158,154,
        1,0,0,0,159,192,1,0,0,0,160,161,10,7,0,0,161,162,5,8,0,0,162,191,
        3,14,7,8,163,164,10,6,0,0,164,165,5,7,0,0,165,191,3,14,7,7,166,167,
        10,5,0,0,167,168,5,13,0,0,168,191,3,14,7,6,169,170,10,3,0,0,170,
        171,5,9,0,0,171,191,3,14,7,4,172,173,10,2,0,0,173,174,5,10,0,0,174,
        191,3,14,7,3,175,176,10,12,0,0,176,178,5,32,0,0,177,179,3,14,7,0,
        178,177,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,182,5,29,0,0,
        181,183,3,14,7,0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,
        184,191,5,33,0,0,185,186,10,11,0,0,186,187,5,32,0,0,187,188,3,14,
        7,0,188,189,5,33,0,0,189,191,1,0,0,0,190,160,1,0,0,0,190,163,1,0,
        0,0,190,166,1,0,0,0,190,169,1,0,0,0,190,172,1,0,0,0,190,175,1,0,
        0,0,190,185,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,
        0,0,193,15,1,0,0,0,194,192,1,0,0,0,195,196,5,27,0,0,196,197,5,36,
        0,0,197,198,3,18,9,0,198,199,5,37,0,0,199,17,1,0,0,0,200,205,3,14,
        7,0,201,202,5,30,0,0,202,204,3,14,7,0,203,201,1,0,0,0,204,207,1,
        0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,205,1,
        0,0,0,208,210,5,30,0,0,209,208,1,0,0,0,209,210,1,0,0,0,210,212,1,
        0,0,0,211,200,1,0,0,0,211,212,1,0,0,0,212,19,1,0,0,0,213,215,5,26,
        0,0,214,213,1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,216,217,3,12,
        6,0,217,218,5,27,0,0,218,219,5,12,0,0,219,220,3,14,7,0,220,21,1,
        0,0,0,221,222,3,24,12,0,222,223,5,12,0,0,223,224,3,14,7,0,224,23,
        1,0,0,0,225,226,6,12,-1,0,226,227,5,27,0,0,227,235,1,0,0,0,228,229,
        10,1,0,0,229,230,5,32,0,0,230,231,3,14,7,0,231,232,5,33,0,0,232,
        234,1,0,0,0,233,228,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,
        236,1,0,0,0,236,25,1,0,0,0,237,235,1,0,0,0,238,240,5,34,0,0,239,
        241,3,4,2,0,240,239,1,0,0,0,241,242,1,0,0,0,242,240,1,0,0,0,242,
        243,1,0,0,0,243,244,1,0,0,0,244,245,5,35,0,0,245,27,1,0,0,0,246,
        248,5,34,0,0,247,249,3,6,3,0,248,247,1,0,0,0,249,250,1,0,0,0,250,
        248,1,0,0,0,250,251,1,0,0,0,251,252,1,0,0,0,252,253,5,35,0,0,253,
        29,1,0,0,0,254,256,5,34,0,0,255,257,3,6,3,0,256,255,1,0,0,0,257,
        258,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,
        261,5,35,0,0,261,31,1,0,0,0,262,263,5,19,0,0,263,266,3,14,7,0,264,
        266,5,19,0,0,265,262,1,0,0,0,265,264,1,0,0,0,266,33,1,0,0,0,267,
        268,5,18,0,0,268,269,3,38,19,0,269,270,5,36,0,0,270,271,3,36,18,
        0,271,272,5,37,0,0,272,273,3,28,14,0,273,282,1,0,0,0,274,275,5,18,
        0,0,275,276,3,38,19,0,276,277,5,36,0,0,277,278,3,36,18,0,278,279,
        5,37,0,0,279,280,3,28,14,0,280,282,1,0,0,0,281,267,1,0,0,0,281,274,
        1,0,0,0,282,35,1,0,0,0,283,288,3,42,21,0,284,285,5,30,0,0,285,287,
        3,42,21,0,286,284,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,
        1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,291,293,5,30,0,0,292,291,
        1,0,0,0,292,293,1,0,0,0,293,295,1,0,0,0,294,283,1,0,0,0,294,295,
        1,0,0,0,295,37,1,0,0,0,296,297,3,40,20,0,297,298,5,29,0,0,298,299,
        5,27,0,0,299,39,1,0,0,0,300,303,3,12,6,0,301,303,5,25,0,0,302,300,
        1,0,0,0,302,301,1,0,0,0,303,41,1,0,0,0,304,305,3,12,6,0,305,306,
        5,27,0,0,306,43,1,0,0,0,307,311,3,48,24,0,308,311,3,50,25,0,309,
        311,3,52,26,0,310,307,1,0,0,0,310,308,1,0,0,0,310,309,1,0,0,0,311,
        45,1,0,0,0,312,316,3,54,27,0,313,316,3,56,28,0,314,316,3,58,29,0,
        315,312,1,0,0,0,315,313,1,0,0,0,315,314,1,0,0,0,316,47,1,0,0,0,317,
        318,5,14,0,0,318,319,5,36,0,0,319,320,3,14,7,0,320,321,5,37,0,0,
        321,324,3,26,13,0,322,323,5,15,0,0,323,325,3,26,13,0,324,322,1,0,
        0,0,324,325,1,0,0,0,325,49,1,0,0,0,326,327,5,17,0,0,327,328,5,36,
        0,0,328,329,3,14,7,0,329,330,5,37,0,0,330,331,3,26,13,0,331,51,1,
        0,0,0,332,333,5,16,0,0,333,334,5,36,0,0,334,335,3,60,30,0,335,336,
        5,37,0,0,336,337,3,26,13,0,337,53,1,0,0,0,338,339,5,14,0,0,339,340,
        5,36,0,0,340,341,3,14,7,0,341,342,5,37,0,0,342,345,3,30,15,0,343,
        344,5,15,0,0,344,346,3,30,15,0,345,343,1,0,0,0,345,346,1,0,0,0,346,
        55,1,0,0,0,347,348,5,17,0,0,348,349,5,36,0,0,349,350,3,14,7,0,350,
        351,5,37,0,0,351,352,3,30,15,0,352,57,1,0,0,0,353,354,5,16,0,0,354,
        355,5,36,0,0,355,356,3,60,30,0,356,357,5,37,0,0,357,358,3,30,15,
        0,358,59,1,0,0,0,359,360,3,12,6,0,360,361,5,27,0,0,361,362,5,13,
        0,0,362,363,3,14,7,0,363,61,1,0,0,0,32,65,80,89,104,111,125,129,
        135,146,158,178,182,190,192,205,209,211,214,235,242,250,258,265,
        281,288,292,294,302,310,315,324,345
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
                      "CurlyLeft", "CurlyRight", "ParenLeft", "ParenRight", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementInControlBlock = 2
    RULE_statementInFunction = 3
    RULE_literal = 4
    RULE_listLiteral = 5
    RULE_type = 6
    RULE_expression = 7
    RULE_functionCall = 8
    RULE_passedParametersList = 9
    RULE_variableDefinition = 10
    RULE_variableAssignment = 11
    RULE_lValue = 12
    RULE_controlBlock = 13
    RULE_functionBlock = 14
    RULE_functionControlBlock = 15
    RULE_returnStatement = 16
    RULE_functionDefinition = 17
    RULE_functionArgumentList = 18
    RULE_functionIdentifier = 19
    RULE_functionReturnType = 20
    RULE_functionArgument = 21
    RULE_controlStatement = 22
    RULE_controlStatementInsideFunction = 23
    RULE_ifStatement = 24
    RULE_whileStatement = 25
    RULE_loopStatement = 26
    RULE_ifStatementInsideFunction = 27
    RULE_whileStatementInsideFunction = 28
    RULE_loopStatementInsideFunction = 29
    RULE_loopStatementIterator = 30

    ruleNames =  [ "program", "statement", "statementInControlBlock", "statementInFunction", 
                   "literal", "listLiteral", "type", "expression", "functionCall", 
                   "passedParametersList", "variableDefinition", "variableAssignment", 
                   "lValue", "controlBlock", "functionBlock", "functionControlBlock", 
                   "returnStatement", "functionDefinition", "functionArgumentList", 
                   "functionIdentifier", "functionReturnType", "functionArgument", 
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
    ERROR_CHAR=38

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
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.statement()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234307584) != 0)):
                    break

            self.state = 67
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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.variableDefinition()
                self.state = 70
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.variableAssignment()
                self.state = 73
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.functionCall()
                self.state = 77
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.variableAssignment()
                self.state = 83
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.functionCall()
                self.state = 86
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
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


        def controlStatementInsideFunction(self):
            return self.getTypedRuleContext(SPLVParser.ControlStatementInsideFunctionContext,0)


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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.variableAssignment()
                self.state = 92
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.functionCall()
                self.state = 95
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.variableDefinition()
                self.state = 98
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.controlStatementInsideFunction()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.returnStatement()
                self.state = 102
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
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(SPLVParser.BoolLiteral)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 110
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


        def getRuleIndex(self):
            return SPLVParser.RULE_listLiteral

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListFromRangeLiteralContext(ListLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ListLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListFromRangeLiteral" ):
                listener.enterListFromRangeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListFromRangeLiteral" ):
                listener.exitListFromRangeLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListFromRangeLiteral" ):
                return visitor.visitListFromRangeLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ListFromElementsLiteralContext(ListLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ListLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SPLVParser.ExpressionContext,i)

        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)
        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(SPLVParser.Comma)
            else:
                return self.getToken(SPLVParser.Comma, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListFromElementsLiteral" ):
                listener.enterListFromElementsLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListFromElementsLiteral" ):
                listener.exitListFromElementsLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListFromElementsLiteral" ):
                return visitor.visitListFromElementsLiteral(self)
            else:
                return visitor.visitChildren(self)


    class EmptyListLiteralContext(ListLiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SPLVParser.ListLiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)
        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyListLiteral" ):
                listener.enterEmptyListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyListLiteral" ):
                listener.exitEmptyListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyListLiteral" ):
                return visitor.visitEmptyListLiteral(self)
            else:
                return visitor.visitChildren(self)



    def listLiteral(self):

        localctx = SPLVParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = SPLVParser.ListFromRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(SPLVParser.BracketLeft)
                self.state = 114
                self.expression(0)
                self.state = 115
                self.match(SPLVParser.DoubleDot)
                self.state = 116
                self.expression(0)
                self.state = 117
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                localctx = SPLVParser.ListFromElementsLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(SPLVParser.BracketLeft)
                self.state = 120
                self.expression(0)
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 121
                        self.match(SPLVParser.Comma)
                        self.state = 122
                        self.expression(0) 
                    self.state = 127
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 128
                    self.match(SPLVParser.Comma)


                self.state = 131
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                localctx = SPLVParser.EmptyListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(SPLVParser.BracketLeft)
                self.state = 134
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
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(SPLVParser.IntType)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(SPLVParser.FloatType)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(SPLVParser.StringType)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(SPLVParser.BoolType)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.match(SPLVParser.ListType)
                self.state = 142
                self.match(SPLVParser.BracketLeft)
                self.state = 143
                self.type_()
                self.state = 144
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
            self.left_exp = None # ExpressionContext
            self.right_exp = None # ExpressionContext
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = SPLVParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 149
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 2:
                localctx = SPLVParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.literal()
                pass

            elif la_ == 3:
                localctx = SPLVParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = SPLVParser.NotOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(SPLVParser.NOTOperator)
                self.state = 153
                self.expression(4)
                pass

            elif la_ == 5:
                localctx = SPLVParser.ParenthesesExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(SPLVParser.ParenLeft)
                self.state = 155
                self.expression(0)
                self.state = 156
                self.match(SPLVParser.ParenRight)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 190
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.MultiplicativeOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 161
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 162
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.AdditiveOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 164
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 165
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.InOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 167
                        self.match(SPLVParser.InOperator)
                        self.state = 168
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ComparisonOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 170
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 171
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.BooleanOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 173
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 174
                        self.expression(3)
                        pass

                    elif la_ == 6:
                        localctx = SPLVParser.ListSlicingExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 176
                        self.match(SPLVParser.BracketLeft)
                        self.state = 178
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 177
                            localctx.left_exp = self.expression(0)


                        self.state = 180
                        self.match(SPLVParser.Colon)
                        self.state = 182
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 181
                            localctx.right_exp = self.expression(0)


                        self.state = 184
                        self.match(SPLVParser.BracketRight)
                        pass

                    elif la_ == 7:
                        localctx = SPLVParser.ListIndexingExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 186
                        self.match(SPLVParser.BracketLeft)
                        self.state = 187
                        self.expression(0)
                        self.state = 188
                        self.match(SPLVParser.BracketRight)
                        pass

             
                self.state = 194
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

        def passedParametersList(self):
            return self.getTypedRuleContext(SPLVParser.PassedParametersListContext,0)


        def ParenRight(self):
            return self.getToken(SPLVParser.ParenRight, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(SPLVParser.Identifier)
            self.state = 196
            self.match(SPLVParser.ParenLeft)
            self.state = 197
            self.passedParametersList()
            self.state = 198
            self.match(SPLVParser.ParenRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassedParametersListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return SPLVParser.RULE_passedParametersList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassedParametersList" ):
                listener.enterPassedParametersList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassedParametersList" ):
                listener.exitPassedParametersList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassedParametersList" ):
                return visitor.visitPassedParametersList(self)
            else:
                return visitor.visitChildren(self)




    def passedParametersList(self):

        localctx = SPLVParser.PassedParametersListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_passedParametersList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                self.state = 200
                self.expression(0)
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 201
                        self.match(SPLVParser.Comma)
                        self.state = 202
                        self.expression(0) 
                    self.state = 207
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 208
                    self.match(SPLVParser.Comma)




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
        self.enterRule(localctx, 20, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
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
            self.state = 218
            self.match(SPLVParser.AssignmentOperator)
            self.state = 219
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

        def lValue(self):
            return self.getTypedRuleContext(SPLVParser.LValueContext,0)


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
        self.enterRule(localctx, 22, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.lValue(0)
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


    class LValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

        def lValue(self):
            return self.getTypedRuleContext(SPLVParser.LValueContext,0)


        def BracketLeft(self):
            return self.getToken(SPLVParser.BracketLeft, 0)

        def expression(self):
            return self.getTypedRuleContext(SPLVParser.ExpressionContext,0)


        def BracketRight(self):
            return self.getToken(SPLVParser.BracketRight, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_lValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLValue" ):
                listener.enterLValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLValue" ):
                listener.exitLValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLValue" ):
                return visitor.visitLValue(self)
            else:
                return visitor.visitChildren(self)



    def lValue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SPLVParser.LValueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_lValue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(SPLVParser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SPLVParser.LValueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lValue)
                    self.state = 228
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 229
                    self.match(SPLVParser.BracketLeft)
                    self.state = 230
                    self.expression(0)
                    self.state = 231
                    self.match(SPLVParser.BracketRight) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 26, self.RULE_controlBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(SPLVParser.CurlyLeft)
            self.state = 240 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 239
                self.statementInControlBlock()
                self.state = 242 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 134430720) != 0)):
                    break

            self.state = 244
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
        self.enterRule(localctx, 28, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(SPLVParser.CurlyLeft)
            self.state = 248 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 247
                self.statementInFunction()
                self.state = 250 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234569728) != 0)):
                    break

            self.state = 252
            self.match(SPLVParser.CurlyRight)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionControlBlockContext(ParserRuleContext):
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
            return SPLVParser.RULE_functionControlBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionControlBlock" ):
                listener.enterFunctionControlBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionControlBlock" ):
                listener.exitFunctionControlBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionControlBlock" ):
                return visitor.visitFunctionControlBlock(self)
            else:
                return visitor.visitChildren(self)




    def functionControlBlock(self):

        localctx = SPLVParser.FunctionControlBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionControlBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(SPLVParser.CurlyLeft)
            self.state = 256 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 255
                self.statementInFunction()
                self.state = 258 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234569728) != 0)):
                    break

            self.state = 260
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
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(SPLVParser.ReturnKeyword)
                self.state = 263
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 34, self.RULE_functionDefinition)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(SPLVParser.FunctionKeyword)
                self.state = 268
                self.functionIdentifier()
                self.state = 269
                self.match(SPLVParser.ParenLeft)
                self.state = 270
                self.functionArgumentList()
                self.state = 271
                self.match(SPLVParser.ParenRight)
                self.state = 272
                self.functionBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.match(SPLVParser.FunctionKeyword)
                self.state = 275
                self.functionIdentifier()
                self.state = 276
                self.match(SPLVParser.ParenLeft)
                self.state = 277
                self.functionArgumentList()
                self.state = 278
                self.match(SPLVParser.ParenRight)
                self.state = 279
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
        self.enterRule(localctx, 36, self.RULE_functionArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0):
                self.state = 283
                self.functionArgument()
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 284
                        self.match(SPLVParser.Comma)
                        self.state = 285
                        self.functionArgument() 
                    self.state = 290
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 291
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

        def functionReturnType(self):
            return self.getTypedRuleContext(SPLVParser.FunctionReturnTypeContext,0)


        def Colon(self):
            return self.getToken(SPLVParser.Colon, 0)

        def Identifier(self):
            return self.getToken(SPLVParser.Identifier, 0)

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
        self.enterRule(localctx, 38, self.RULE_functionIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.functionReturnType()
            self.state = 297
            self.match(SPLVParser.Colon)
            self.state = 298
            self.match(SPLVParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SPLVParser.TypeContext,0)


        def VoidType(self):
            return self.getToken(SPLVParser.VoidType, 0)

        def getRuleIndex(self):
            return SPLVParser.RULE_functionReturnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionReturnType" ):
                listener.enterFunctionReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionReturnType" ):
                listener.exitFunctionReturnType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionReturnType" ):
                return visitor.visitFunctionReturnType(self)
            else:
                return visitor.visitChildren(self)




    def functionReturnType(self):

        localctx = SPLVParser.FunctionReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functionReturnType)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.type_()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(SPLVParser.VoidType)
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
        self.enterRule(localctx, 42, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.type_()
            self.state = 305
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
        self.enterRule(localctx, 44, self.RULE_controlStatement)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
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
        self.enterRule(localctx, 46, self.RULE_controlStatementInsideFunction)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.ifStatementInsideFunction()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.whileStatementInsideFunction()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
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
        self.enterRule(localctx, 48, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(SPLVParser.IfKeyword)
            self.state = 318
            self.match(SPLVParser.ParenLeft)
            self.state = 319
            self.expression(0)
            self.state = 320
            self.match(SPLVParser.ParenRight)
            self.state = 321
            self.controlBlock()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 322
                self.match(SPLVParser.ElseKeyword)
                self.state = 323
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
        self.enterRule(localctx, 50, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(SPLVParser.WhileKeyword)
            self.state = 327
            self.match(SPLVParser.ParenLeft)
            self.state = 328
            self.expression(0)
            self.state = 329
            self.match(SPLVParser.ParenRight)
            self.state = 330
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
        self.enterRule(localctx, 52, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(SPLVParser.LoopKeyword)
            self.state = 333
            self.match(SPLVParser.ParenLeft)
            self.state = 334
            self.loopStatementIterator()
            self.state = 335
            self.match(SPLVParser.ParenRight)
            self.state = 336
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

        def functionControlBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SPLVParser.FunctionControlBlockContext)
            else:
                return self.getTypedRuleContext(SPLVParser.FunctionControlBlockContext,i)


        def ElseKeyword(self):
            return self.getToken(SPLVParser.ElseKeyword, 0)

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
        self.enterRule(localctx, 54, self.RULE_ifStatementInsideFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(SPLVParser.IfKeyword)
            self.state = 339
            self.match(SPLVParser.ParenLeft)
            self.state = 340
            self.expression(0)
            self.state = 341
            self.match(SPLVParser.ParenRight)
            self.state = 342
            self.functionControlBlock()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 343
                self.match(SPLVParser.ElseKeyword)
                self.state = 344
                self.functionControlBlock()


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

        def functionControlBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionControlBlockContext,0)


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
        self.enterRule(localctx, 56, self.RULE_whileStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(SPLVParser.WhileKeyword)
            self.state = 348
            self.match(SPLVParser.ParenLeft)
            self.state = 349
            self.expression(0)
            self.state = 350
            self.match(SPLVParser.ParenRight)
            self.state = 351
            self.functionControlBlock()
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

        def functionControlBlock(self):
            return self.getTypedRuleContext(SPLVParser.FunctionControlBlockContext,0)


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
        self.enterRule(localctx, 58, self.RULE_loopStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(SPLVParser.LoopKeyword)
            self.state = 354
            self.match(SPLVParser.ParenLeft)
            self.state = 355
            self.loopStatementIterator()
            self.state = 356
            self.match(SPLVParser.ParenRight)
            self.state = 357
            self.functionControlBlock()
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
        self.enterRule(localctx, 60, self.RULE_loopStatementIterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.type_()
            self.state = 360
            self.match(SPLVParser.Identifier)
            self.state = 361
            self.match(SPLVParser.InOperator)
            self.state = 362
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
        self._predicates[12] = self.lValue_sempred
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
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         

    def lValue_sempred(self, localctx:LValueContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




