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
        4,1,38,367,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,4,0,60,8,0,11,0,12,0,61,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,89,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,4,1,4,1,4,1,4,1,4,3,4,111,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,123,8,5,10,5,12,5,126,
        9,5,1,5,3,5,129,8,5,1,5,1,5,1,5,1,5,3,5,135,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,146,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,158,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,183,8,7,1,7,
        1,7,3,7,187,8,7,1,7,5,7,190,8,7,10,7,12,7,193,9,7,1,8,1,8,1,8,1,
        8,1,8,5,8,200,8,8,10,8,12,8,203,9,8,1,8,3,8,206,8,8,3,8,208,8,8,
        1,8,1,8,1,9,3,9,213,8,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,221,8,9,1,9,
        1,9,1,9,3,9,226,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,238,8,11,1,12,1,12,4,12,242,8,12,11,12,12,12,243,1,12,
        1,12,1,13,1,13,4,13,250,8,13,11,13,12,13,251,1,13,1,13,1,14,1,14,
        4,14,258,8,14,11,14,12,14,259,1,14,1,14,1,15,1,15,1,15,3,15,267,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,283,8,16,1,17,1,17,1,17,5,17,288,8,17,10,17,12,17,
        291,9,17,1,17,3,17,294,8,17,3,17,296,8,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,305,8,18,1,19,1,19,1,19,1,20,1,20,1,20,3,20,313,
        8,20,1,21,1,21,1,21,3,21,318,8,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,3,22,327,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,348,8,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,0,1,14,29,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,0,396,0,59,
        1,0,0,0,2,76,1,0,0,0,4,88,1,0,0,0,6,103,1,0,0,0,8,110,1,0,0,0,10,
        134,1,0,0,0,12,145,1,0,0,0,14,157,1,0,0,0,16,194,1,0,0,0,18,225,
        1,0,0,0,20,227,1,0,0,0,22,237,1,0,0,0,24,239,1,0,0,0,26,247,1,0,
        0,0,28,255,1,0,0,0,30,266,1,0,0,0,32,282,1,0,0,0,34,295,1,0,0,0,
        36,304,1,0,0,0,38,306,1,0,0,0,40,312,1,0,0,0,42,317,1,0,0,0,44,319,
        1,0,0,0,46,328,1,0,0,0,48,334,1,0,0,0,50,340,1,0,0,0,52,349,1,0,
        0,0,54,355,1,0,0,0,56,361,1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,
        61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,0,0,
        1,64,1,1,0,0,0,65,66,3,18,9,0,66,67,5,28,0,0,67,77,1,0,0,0,68,69,
        3,20,10,0,69,70,5,28,0,0,70,77,1,0,0,0,71,77,3,32,16,0,72,73,3,16,
        8,0,73,74,5,28,0,0,74,77,1,0,0,0,75,77,3,40,20,0,76,65,1,0,0,0,76,
        68,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,
        0,78,79,3,20,10,0,79,80,5,28,0,0,80,89,1,0,0,0,81,82,3,18,9,0,82,
        83,5,28,0,0,83,89,1,0,0,0,84,85,3,16,8,0,85,86,5,28,0,0,86,89,1,
        0,0,0,87,89,3,40,20,0,88,78,1,0,0,0,88,81,1,0,0,0,88,84,1,0,0,0,
        88,87,1,0,0,0,89,5,1,0,0,0,90,91,3,20,10,0,91,92,5,28,0,0,92,104,
        1,0,0,0,93,94,3,16,8,0,94,95,5,28,0,0,95,104,1,0,0,0,96,97,3,18,
        9,0,97,98,5,28,0,0,98,104,1,0,0,0,99,104,3,42,21,0,100,101,3,30,
        15,0,101,102,5,28,0,0,102,104,1,0,0,0,103,90,1,0,0,0,103,93,1,0,
        0,0,103,96,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,104,7,1,0,0,0,
        105,111,5,3,0,0,106,111,5,4,0,0,107,111,5,6,0,0,108,111,5,5,0,0,
        109,111,3,10,5,0,110,105,1,0,0,0,110,106,1,0,0,0,110,107,1,0,0,0,
        110,108,1,0,0,0,110,109,1,0,0,0,111,9,1,0,0,0,112,113,5,32,0,0,113,
        114,3,14,7,0,114,115,5,31,0,0,115,116,3,14,7,0,116,117,5,33,0,0,
        117,135,1,0,0,0,118,119,5,32,0,0,119,124,3,14,7,0,120,121,5,30,0,
        0,121,123,3,14,7,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,
        0,124,125,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,127,129,5,30,0,
        0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,5,33,0,
        0,131,135,1,0,0,0,132,133,5,32,0,0,133,135,5,33,0,0,134,112,1,0,
        0,0,134,118,1,0,0,0,134,132,1,0,0,0,135,11,1,0,0,0,136,146,5,20,
        0,0,137,146,5,21,0,0,138,146,5,22,0,0,139,146,5,23,0,0,140,141,5,
        24,0,0,141,142,5,32,0,0,142,143,3,12,6,0,143,144,5,33,0,0,144,146,
        1,0,0,0,145,136,1,0,0,0,145,137,1,0,0,0,145,138,1,0,0,0,145,139,
        1,0,0,0,145,140,1,0,0,0,146,13,1,0,0,0,147,148,6,7,-1,0,148,158,
        5,27,0,0,149,158,3,8,4,0,150,158,3,16,8,0,151,152,5,11,0,0,152,158,
        3,14,7,4,153,154,5,36,0,0,154,155,3,14,7,0,155,156,5,37,0,0,156,
        158,1,0,0,0,157,147,1,0,0,0,157,149,1,0,0,0,157,150,1,0,0,0,157,
        151,1,0,0,0,157,153,1,0,0,0,158,191,1,0,0,0,159,160,10,7,0,0,160,
        161,5,8,0,0,161,190,3,14,7,8,162,163,10,6,0,0,163,164,5,7,0,0,164,
        190,3,14,7,7,165,166,10,5,0,0,166,167,5,13,0,0,167,190,3,14,7,6,
        168,169,10,3,0,0,169,170,5,9,0,0,170,190,3,14,7,4,171,172,10,2,0,
        0,172,173,5,10,0,0,173,190,3,14,7,3,174,175,10,10,0,0,175,176,5,
        32,0,0,176,177,3,14,7,0,177,178,5,33,0,0,178,190,1,0,0,0,179,180,
        10,9,0,0,180,182,5,32,0,0,181,183,3,14,7,0,182,181,1,0,0,0,182,183,
        1,0,0,0,183,184,1,0,0,0,184,186,5,29,0,0,185,187,3,14,7,0,186,185,
        1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,190,5,33,0,0,189,159,
        1,0,0,0,189,162,1,0,0,0,189,165,1,0,0,0,189,168,1,0,0,0,189,171,
        1,0,0,0,189,174,1,0,0,0,189,179,1,0,0,0,190,193,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,15,1,0,0,0,193,191,1,0,0,0,194,195,5,
        27,0,0,195,207,5,36,0,0,196,201,3,14,7,0,197,198,5,30,0,0,198,200,
        3,14,7,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,204,206,5,30,0,0,205,204,
        1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,196,1,0,0,0,207,208,
        1,0,0,0,208,209,1,0,0,0,209,210,5,37,0,0,210,17,1,0,0,0,211,213,
        5,26,0,0,212,211,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,215,
        3,12,6,0,215,216,5,27,0,0,216,217,5,12,0,0,217,218,3,14,7,0,218,
        226,1,0,0,0,219,221,5,26,0,0,220,219,1,0,0,0,220,221,1,0,0,0,221,
        222,1,0,0,0,222,223,3,12,6,0,223,224,5,27,0,0,224,226,1,0,0,0,225,
        212,1,0,0,0,225,220,1,0,0,0,226,19,1,0,0,0,227,228,3,22,11,0,228,
        229,5,12,0,0,229,230,3,14,7,0,230,21,1,0,0,0,231,238,5,27,0,0,232,
        233,5,27,0,0,233,234,5,32,0,0,234,235,3,14,7,0,235,236,5,33,0,0,
        236,238,1,0,0,0,237,231,1,0,0,0,237,232,1,0,0,0,238,23,1,0,0,0,239,
        241,5,34,0,0,240,242,3,4,2,0,241,240,1,0,0,0,242,243,1,0,0,0,243,
        241,1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,246,5,35,0,0,246,
        25,1,0,0,0,247,249,5,34,0,0,248,250,3,6,3,0,249,248,1,0,0,0,250,
        251,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,
        254,5,35,0,0,254,27,1,0,0,0,255,257,5,34,0,0,256,258,3,6,3,0,257,
        256,1,0,0,0,258,259,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,
        261,1,0,0,0,261,262,5,35,0,0,262,29,1,0,0,0,263,264,5,19,0,0,264,
        267,3,14,7,0,265,267,5,19,0,0,266,263,1,0,0,0,266,265,1,0,0,0,267,
        31,1,0,0,0,268,269,5,18,0,0,269,270,3,36,18,0,270,271,5,36,0,0,271,
        272,3,34,17,0,272,273,5,37,0,0,273,274,3,26,13,0,274,283,1,0,0,0,
        275,276,5,18,0,0,276,277,3,36,18,0,277,278,5,36,0,0,278,279,3,34,
        17,0,279,280,5,37,0,0,280,281,3,26,13,0,281,283,1,0,0,0,282,268,
        1,0,0,0,282,275,1,0,0,0,283,33,1,0,0,0,284,289,3,38,19,0,285,286,
        5,30,0,0,286,288,3,38,19,0,287,285,1,0,0,0,288,291,1,0,0,0,289,287,
        1,0,0,0,289,290,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,292,294,
        5,30,0,0,293,292,1,0,0,0,293,294,1,0,0,0,294,296,1,0,0,0,295,284,
        1,0,0,0,295,296,1,0,0,0,296,35,1,0,0,0,297,298,3,12,6,0,298,299,
        5,29,0,0,299,300,5,27,0,0,300,305,1,0,0,0,301,302,5,25,0,0,302,303,
        5,29,0,0,303,305,5,27,0,0,304,297,1,0,0,0,304,301,1,0,0,0,305,37,
        1,0,0,0,306,307,3,12,6,0,307,308,5,27,0,0,308,39,1,0,0,0,309,313,
        3,44,22,0,310,313,3,46,23,0,311,313,3,48,24,0,312,309,1,0,0,0,312,
        310,1,0,0,0,312,311,1,0,0,0,313,41,1,0,0,0,314,318,3,50,25,0,315,
        318,3,52,26,0,316,318,3,54,27,0,317,314,1,0,0,0,317,315,1,0,0,0,
        317,316,1,0,0,0,318,43,1,0,0,0,319,320,5,14,0,0,320,321,5,36,0,0,
        321,322,3,14,7,0,322,323,5,37,0,0,323,326,3,24,12,0,324,325,5,15,
        0,0,325,327,3,24,12,0,326,324,1,0,0,0,326,327,1,0,0,0,327,45,1,0,
        0,0,328,329,5,17,0,0,329,330,5,36,0,0,330,331,3,14,7,0,331,332,5,
        37,0,0,332,333,3,24,12,0,333,47,1,0,0,0,334,335,5,16,0,0,335,336,
        5,36,0,0,336,337,3,56,28,0,337,338,5,37,0,0,338,339,3,24,12,0,339,
        49,1,0,0,0,340,341,5,14,0,0,341,342,5,36,0,0,342,343,3,14,7,0,343,
        344,5,37,0,0,344,347,3,28,14,0,345,346,5,15,0,0,346,348,3,28,14,
        0,347,345,1,0,0,0,347,348,1,0,0,0,348,51,1,0,0,0,349,350,5,17,0,
        0,350,351,5,36,0,0,351,352,3,14,7,0,352,353,5,37,0,0,353,354,3,28,
        14,0,354,53,1,0,0,0,355,356,5,16,0,0,356,357,5,36,0,0,357,358,3,
        56,28,0,358,359,5,37,0,0,359,360,3,28,14,0,360,55,1,0,0,0,361,362,
        3,12,6,0,362,363,5,27,0,0,363,364,5,13,0,0,364,365,3,14,7,0,365,
        57,1,0,0,0,34,61,76,88,103,110,124,128,134,145,157,182,186,189,191,
        201,205,207,212,220,225,237,243,251,259,266,282,289,293,295,304,
        312,317,326,347
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
    RULE_variableDefinition = 9
    RULE_variableAssignment = 10
    RULE_lValue = 11
    RULE_controlBlock = 12
    RULE_functionBlock = 13
    RULE_functionControlBlock = 14
    RULE_returnStatement = 15
    RULE_functionDefinition = 16
    RULE_functionArgumentList = 17
    RULE_functionIdentifier = 18
    RULE_functionArgument = 19
    RULE_controlStatement = 20
    RULE_controlStatementInsideFunction = 21
    RULE_ifStatement = 22
    RULE_whileStatement = 23
    RULE_loopStatement = 24
    RULE_ifStatementInsideFunction = 25
    RULE_whileStatementInsideFunction = 26
    RULE_loopStatementInsideFunction = 27
    RULE_loopStatementIterator = 28

    ruleNames =  [ "program", "statement", "statementInControlBlock", "statementInFunction", 
                   "literal", "listLiteral", "type", "expression", "functionCall", 
                   "variableDefinition", "variableAssignment", "lValue", 
                   "controlBlock", "functionBlock", "functionControlBlock", 
                   "returnStatement", "functionDefinition", "functionArgumentList", 
                   "functionIdentifier", "functionArgument", "controlStatement", 
                   "controlStatementInsideFunction", "ifStatement", "whileStatement", 
                   "loopStatement", "ifStatementInsideFunction", "whileStatementInsideFunction", 
                   "loopStatementInsideFunction", "loopStatementIterator" ]

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
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.statement()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234307584) != 0)):
                    break

            self.state = 63
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
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.variableDefinition()
                self.state = 66
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.variableAssignment()
                self.state = 69
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.functionCall()
                self.state = 73
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.variableAssignment()
                self.state = 79
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.variableDefinition()
                self.state = 82
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.functionCall()
                self.state = 85
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.variableAssignment()
                self.state = 91
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.functionCall()
                self.state = 94
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.variableDefinition()
                self.state = 97
                self.match(SPLVParser.Semicolon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.controlStatementInsideFunction()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.returnStatement()
                self.state = 101
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
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(SPLVParser.IntLiteral)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(SPLVParser.FloatLiteral)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(SPLVParser.StringLiteral)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.match(SPLVParser.BoolLiteral)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(SPLVParser.BracketLeft)
                self.state = 113
                self.expression(0)
                self.state = 114
                self.match(SPLVParser.DoubleDot)
                self.state = 115
                self.expression(0)
                self.state = 116
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(SPLVParser.BracketLeft)
                self.state = 119
                self.expression(0)
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 120
                        self.match(SPLVParser.Comma)
                        self.state = 121
                        self.expression(0) 
                    self.state = 126
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 127
                    self.match(SPLVParser.Comma)


                self.state = 130
                self.match(SPLVParser.BracketRight)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(SPLVParser.BracketLeft)
                self.state = 133
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(SPLVParser.IntType)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(SPLVParser.FloatType)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.match(SPLVParser.StringType)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.match(SPLVParser.BoolType)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.match(SPLVParser.ListType)
                self.state = 141
                self.match(SPLVParser.BracketLeft)
                self.state = 142
                self.type_()
                self.state = 143
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = SPLVParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 148
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 2:
                localctx = SPLVParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.literal()
                pass

            elif la_ == 3:
                localctx = SPLVParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = SPLVParser.NotOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(SPLVParser.NOTOperator)
                self.state = 152
                self.expression(4)
                pass

            elif la_ == 5:
                localctx = SPLVParser.ParenthesesExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(SPLVParser.ParenLeft)
                self.state = 154
                self.expression(0)
                self.state = 155
                self.match(SPLVParser.ParenRight)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 189
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = SPLVParser.MultiplicativeOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 159
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 160
                        self.match(SPLVParser.MultiplicativeOperator)
                        self.state = 161
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SPLVParser.AdditiveOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 163
                        self.match(SPLVParser.AdditiveOperator)
                        self.state = 164
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = SPLVParser.InOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 166
                        self.match(SPLVParser.InOperator)
                        self.state = 167
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = SPLVParser.ComparisonOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 169
                        self.match(SPLVParser.ComparisonOperator)
                        self.state = 170
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = SPLVParser.BooleanOperatorExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 172
                        self.match(SPLVParser.BooleanOperator)
                        self.state = 173
                        self.expression(3)
                        pass

                    elif la_ == 6:
                        localctx = SPLVParser.ListIndexingExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 175
                        self.match(SPLVParser.BracketLeft)
                        self.state = 176
                        self.expression(0)
                        self.state = 177
                        self.match(SPLVParser.BracketRight)
                        pass

                    elif la_ == 7:
                        localctx = SPLVParser.ListSlicingExpressionContext(self, SPLVParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 180
                        self.match(SPLVParser.BracketLeft)
                        self.state = 182
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 181
                            self.expression(0)


                        self.state = 184
                        self.match(SPLVParser.Colon)
                        self.state = 186
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                            self.state = 185
                            self.expression(0)


                        self.state = 188
                        self.match(SPLVParser.BracketRight)
                        pass

             
                self.state = 193
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
            self.state = 194
            self.match(SPLVParser.Identifier)
            self.state = 195
            self.match(SPLVParser.ParenLeft)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 73148663928) != 0):
                self.state = 196
                self.expression(0)
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 197
                        self.match(SPLVParser.Comma)
                        self.state = 198
                        self.expression(0) 
                    self.state = 203
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 204
                    self.match(SPLVParser.Comma)




            self.state = 209
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
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 211
                    self.match(SPLVParser.GlobalTypeModifier)


                self.state = 214
                self.type_()
                self.state = 215
                self.match(SPLVParser.Identifier)
                self.state = 216
                self.match(SPLVParser.AssignmentOperator)
                self.state = 217
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 219
                    self.match(SPLVParser.GlobalTypeModifier)


                self.state = 222
                self.type_()
                self.state = 223
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
        self.enterRule(localctx, 20, self.RULE_variableAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.lValue()
            self.state = 228
            self.match(SPLVParser.AssignmentOperator)
            self.state = 229
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




    def lValue(self):

        localctx = SPLVParser.LValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lValue)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(SPLVParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(SPLVParser.Identifier)
                self.state = 233
                self.match(SPLVParser.BracketLeft)
                self.state = 234
                self.expression(0)
                self.state = 235
                self.match(SPLVParser.BracketRight)
                pass


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
        self.enterRule(localctx, 24, self.RULE_controlBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(SPLVParser.CurlyLeft)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240
                self.statementInControlBlock()
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234045440) != 0)):
                    break

            self.state = 245
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
        self.enterRule(localctx, 26, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(SPLVParser.CurlyLeft)
            self.state = 249 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 248
                self.statementInFunction()
                self.state = 251 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234569728) != 0)):
                    break

            self.state = 253
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
        self.enterRule(localctx, 28, self.RULE_functionControlBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(SPLVParser.CurlyLeft)
            self.state = 257 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 256
                self.statementInFunction()
                self.state = 259 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 234569728) != 0)):
                    break

            self.state = 261
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
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(SPLVParser.ReturnKeyword)
                self.state = 264
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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
        self.enterRule(localctx, 32, self.RULE_functionDefinition)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(SPLVParser.FunctionKeyword)
                self.state = 269
                self.functionIdentifier()
                self.state = 270
                self.match(SPLVParser.ParenLeft)
                self.state = 271
                self.functionArgumentList()
                self.state = 272
                self.match(SPLVParser.ParenRight)
                self.state = 273
                self.functionBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(SPLVParser.FunctionKeyword)
                self.state = 276
                self.functionIdentifier()
                self.state = 277
                self.match(SPLVParser.ParenLeft)
                self.state = 278
                self.functionArgumentList()
                self.state = 279
                self.match(SPLVParser.ParenRight)
                self.state = 280
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
        self.enterRule(localctx, 34, self.RULE_functionArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0):
                self.state = 284
                self.functionArgument()
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 285
                        self.match(SPLVParser.Comma)
                        self.state = 286
                        self.functionArgument() 
                    self.state = 291
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 292
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
        self.enterRule(localctx, 36, self.RULE_functionIdentifier)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.type_()
                self.state = 298
                self.match(SPLVParser.Colon)
                self.state = 299
                self.match(SPLVParser.Identifier)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(SPLVParser.VoidType)
                self.state = 302
                self.match(SPLVParser.Colon)
                self.state = 303
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
        self.enterRule(localctx, 38, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.type_()
            self.state = 307
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
        self.enterRule(localctx, 40, self.RULE_controlStatement)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.ifStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.whileStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
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
        self.enterRule(localctx, 42, self.RULE_controlStatementInsideFunction)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.ifStatementInsideFunction()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.whileStatementInsideFunction()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
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
        self.enterRule(localctx, 44, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(SPLVParser.IfKeyword)
            self.state = 320
            self.match(SPLVParser.ParenLeft)
            self.state = 321
            self.expression(0)
            self.state = 322
            self.match(SPLVParser.ParenRight)
            self.state = 323
            self.controlBlock()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 324
                self.match(SPLVParser.ElseKeyword)
                self.state = 325
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
        self.enterRule(localctx, 46, self.RULE_whileStatement)
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
        self.enterRule(localctx, 48, self.RULE_loopStatement)
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
        self.enterRule(localctx, 50, self.RULE_ifStatementInsideFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(SPLVParser.IfKeyword)
            self.state = 341
            self.match(SPLVParser.ParenLeft)
            self.state = 342
            self.expression(0)
            self.state = 343
            self.match(SPLVParser.ParenRight)
            self.state = 344
            self.functionControlBlock()
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 345
                self.match(SPLVParser.ElseKeyword)
                self.state = 346
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
        self.enterRule(localctx, 52, self.RULE_whileStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(SPLVParser.WhileKeyword)
            self.state = 350
            self.match(SPLVParser.ParenLeft)
            self.state = 351
            self.expression(0)
            self.state = 352
            self.match(SPLVParser.ParenRight)
            self.state = 353
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
        self.enterRule(localctx, 54, self.RULE_loopStatementInsideFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(SPLVParser.LoopKeyword)
            self.state = 356
            self.match(SPLVParser.ParenLeft)
            self.state = 357
            self.loopStatementIterator()
            self.state = 358
            self.match(SPLVParser.ParenRight)
            self.state = 359
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
        self.enterRule(localctx, 56, self.RULE_loopStatementIterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.type_()
            self.state = 362
            self.match(SPLVParser.Identifier)
            self.state = 363
            self.match(SPLVParser.InOperator)
            self.state = 364
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
         




