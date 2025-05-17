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
    | controlStatementInsideFunction
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
    : Identifier #identifierExpression
    | literal #literalExpression
    | expression BracketLeft expression BracketRight #listIndexingExpression
    | expression BracketLeft expression? Colon expression? BracketRight #listSlicingExpression
    | functionCall #functionCallExpression
    | expression MultiplicativeOperator expression #multiplicativeOperatorExpression
    | expression AdditiveOperator expression #additiveOperatorExpression
    | expression InOperator expression #inOperatorExpression
    | NOTOperator expression #notOperatorExpression
    | expression ComparisonOperator expression #comparisonOperatorExpression
    | expression BooleanOperator expression #booleanOperatorExpression
    | ParenLeft expression ParenRight #parenthesesExpression
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
variableAssignment: lValue AssignmentOperator expression;
lValue
    : Identifier
    | Identifier BracketLeft expression BracketRight
    ;
////

// block
controlBlock: CurlyLeft statementInControlBlock+ CurlyRight;
functionBlock: CurlyLeft statementInFunction+ CurlyRight;
functionControlBlock: CurlyLeft statementInFunction+ CurlyRight;
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

ifStatementInsideFunction: IfKeyword ParenLeft expression ParenRight functionControlBlock (ElseKeyword functionControlBlock)?;
whileStatementInsideFunction: WhileKeyword ParenLeft expression ParenRight functionControlBlock;
loopStatementInsideFunction: LoopKeyword ParenLeft loopStatementIterator ParenRight functionControlBlock;

loopStatementIterator: type Identifier InOperator expression;
////

