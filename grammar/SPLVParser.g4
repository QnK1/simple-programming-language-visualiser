parser grammar SPLVParser;

options {
    tokenVocab = SPLVLexer;
}

// starting symbol
program: statement+ EOF;
////

// statements
statement
    : variableDefinition Semicolon
    | variableAssignment Semicolon
    | functionDefinition
    | functionCall Semicolon
    | controlStatement
    ;
////

// statements inside loop/if blocks
statementInControlBlock
    : variableAssignment Semicolon
    | variableDefinition Semicolon
    | functionCall Semicolon
    | controlStatement
    ;
////

// statements inside functions
statementInFunction
    : variableAssignment Semicolon
    | functionCall Semicolon
    | variableDefinition Semicolon
    | controlStatement
    | returnStatement Semicolon
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
    | functionCall
    | Identifier
    | expression BracketLeft expression BracketRight // list indexing
    | expression BracketLeft expression? Colon expression? BracketRight // list slicing
    | ParenLeft expression ParenRight
    | NOTOperator expression 
    | expression ComparisonOperator expression
    | expression BooleanOperator expression
    | expression MultiplicativeOperator expression
    | expression AdditiveOperator expression
    | expression InOperator expression
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
controlBlock: CurlyLeft statementInControlBlock+ CurlyRight;
functionBlock: CurlyLeft statementInFunction+ CurlyRight;
returnStatement
    : ReturnKeyword expression
    | ReturnKeyword
    ;
////

// function definitions
functionDefinition
    : FunctionKeyword Type Colon Identifier ParenLeft (Type Identifier (Comma Type Identifier)* Comma?)? ParenRight functionBlock #returningFunction
    | FunctionKeyword VoidType Colon Identifier ParenLeft (Type Identifier (Comma Type Identifier)* Comma?)? ParenRight functionBlock #voidFunction
    ;
////

// control statements
controlStatement
    : ifStatement
    | whileStatement
    | loopStatement
    ;

controlStatementInsideFunction
    : ifStatementInsideFunction
    | whileStatementInsideFunction
    | loopStatementInsideFunction
    ;

ifStatement: IfKeyword ParenLeft expression ParenRight controlBlock (ElseKeyword controlBlock)?;
whileStatement: WhileKeyword ParenLeft expression ParenRight controlBlock;
loopStatement: LoopKeyword ParenLeft Type Identifier InOperator expression ParenRight controlBlock;

ifStatementInsideFunction: IfKeyword ParenLeft expression ParenRight (ElseKeyword functionBlock)?;
whileStatementInsideFunction: WhileKeyword ParenLeft expression ParenRight functionBlock;
loopStatementInsideFunction: LoopKeyword ParenLeft Type Identifier InOperator expression ParenRight functionBlock;
////

