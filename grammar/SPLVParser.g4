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

// types
type
    : IntType
    | FloatType
    | StringType
    | BoolType
    | ListType BracketLeft type BracketRight
    ;
////

// expressions
expression
    : literal #literalExpression
    | functionCall #functionCallExpression
    | Identifier #identifierExpression
    | expression MultiplicativeOperator expression #multiplicativeOperatorExpression
    | expression AdditiveOperator expression #additiveOperatorExpression
    | expression InOperator expression #inOperatorExpression
    | NOTOperator expression #notOperatorExpression
    | expression ComparisonOperator expression #comparisonOperatorExpression
    | expression BooleanOperator expression #booleanOperatorExpression
    | ParenLeft expression ParenRight #parenthesesExpression
    | expression BracketLeft expression BracketRight #listIndexingExpression
    | expression BracketLeft expression? Colon expression? BracketRight #listSlicingExpression
    ;
////`

// function calls
functionCall: Identifier ParenLeft (expression (Comma expression)* Comma?)? ParenRight; 
////

// variable definition and assignment
variableDefinition
    : GlobalTypeModifier? type Identifier AssignmentOperator expression
    | GlobalTypeModifier? type Identifier
    ;
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
    : FunctionKeyword functionIdentifier ParenLeft functionArgumentList ParenRight functionBlock
    | FunctionKeyword functionIdentifier ParenLeft functionArgumentList ParenRight functionBlock
    ;

functionArgumentList: (functionArgument (Comma functionArgument)* Comma?)?;
functionIdentifier
    : type Colon Identifier
    | VoidType Colon Identifier
    ;
functionArgument: type Identifier;
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
loopStatement: LoopKeyword ParenLeft loopStatementIterator ParenRight controlBlock;

ifStatementInsideFunction: IfKeyword ParenLeft expression ParenRight (ElseKeyword functionBlock)?;
whileStatementInsideFunction: WhileKeyword ParenLeft expression ParenRight functionBlock;
loopStatementInsideFunction: LoopKeyword ParenLeft loopStatementIterator ParenRight functionBlock;

loopStatementIterator: type Identifier InOperator expression;
////

