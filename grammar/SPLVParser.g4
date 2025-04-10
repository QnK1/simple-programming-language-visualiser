parser grammar SPLVParser;

options {
    tokenVocab = SPLVLexer;
}

// starting symbol
program: (statement Semicolon)* EOF;
////

// statements
statement
    : variableDefinition
    | variableAssignment
    | functionDefinition
    | functionCall
    | controlStatement
    ;
////

// statements inside loop/if blocks
statementInblock
    : variableAssignment
    | functionCall
    | controlStatement
    ;
////

// statements inside functions
statementInFunction
    : variableAssignment
    | functionCall
    | variableDefinition
    | controlStatement
    ;
////

// literals
literal
    : IntLiteral
    | FloatLiteral
    | StringLiteral
    | BoolLiteral
    | listLiteral
    ;

listLiteral
    : BracketLeft expression DoubleDot expression BracketRight // list from range
    | BracketLeft expression (Comma expression)* Comma? BracketRight // list with given elements
    | BracketLeft BracketRight
    ;
////

// expressions
expression
    : literal
    | Identifier
    | functionCall
    | ParenLeft expression ParenRight
    | expression AdditiveOperator expression
    | expression MultiplicativeOperator expression
    | expression BooleanOperator expression
    | expression ComparisonOperator expression
    | NOTOperator expression
    | expression InOperator expression
    | expression BracketLeft expression BracketRight // list indexing
    | expression BracketLeft expression? Colon expression? BracketRight // list slicing
    ;
////`

// function calls
functionCall: Identifier ParenLeft (expression (Comma expression)* Comma?)? ParenRight; 
////

// variable definition and assignment
variableDefinition: GlobalTypeModifier? Type Identifier AssignmentOperator expression;
variableAssignment: Identifier AssignmentOperator expression;
////

// block
block: CurlyLeft (statementInblock Semicolon)* CurlyRight;
functionBlock: CurlyLeft (statementInFunction Semicolon)* returnStatement Semicolon CurlyRight;
voidFunctionBlock: CurlyLeft (statementInFunction Semicolon)* voidReturnStatement Semicolon CurlyRight;
voidReturnStatement: ReturnKeyword;
returnStatement: ReturnKeyword expression;
////

// function definitions
functionDefinition
    : FunctionKeyword Type Colon Identifier ParenLeft (Type Identifier (Comma Type Identifier)* Comma?)? ParenRight functionBlock #returningFunction
    | FunctionKeyword VoidType Colon Identifier ParenLeft (Type Identifier (Comma Type Identifier)* Comma?)? ParenRight voidFunctionBlock #voidFunction
    ;
////

// control statements
controlStatement
    : ifStatement
    | whileStatement
    | loopStatement
    ;

ifStatement: IfKeyword ParenLeft expression ParenRight block;
whileStatement: WhileKeyword ParenLeft expression ParenRight block;
loopStatement: LoopKeyword ParenLeft Type Identifier InOperator expression ParenRight block;
////

