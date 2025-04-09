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
innerStatement
    : variableAssignment
    | functionCall
    | controlStatement
    ;
////

// literals
literal
    : IntLiteral
    | FloatLiteral
    | StringLiteral
    | BooleanOperator
    | listLiteral
    ;

listLiteral
    : BracketLeft expression Colon expression BracketRight
    | BracketLeft expression (Comma expression)* Comma? BracketRight
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
    ;
////

// function calls
functionCall: Identifier ParenLeft (expression (Comma expression)* Comma?)? ParenRight; 
////

// variable definition and assignment
variableDefinition: GlobalTypeModifier? Type Identifier AssignmentOperator expression;
variableAssignment: Identifier AssignmentOperator expression;
////

// block
block: CurlyLeft (innerStatement Semicolon)* CurlRight;
functionBlock: CurlyLeft (innerStatement Semicolon)* ReturnKeyword Semicolon CurlRight;
////

// function definitions
functionDefinition
    : FunctionKeyword Type Colon Identifier ParenLeft (Type Identifier (Comma Type Identifier)* Comma?)? ParenRight functionBlock;
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

