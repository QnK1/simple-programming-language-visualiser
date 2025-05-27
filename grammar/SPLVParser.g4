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
    : BracketLeft expression DoubleDot expression BracketRight #listFromRangeLiteral
    | BracketLeft expression (Comma expression)* Comma? BracketRight #listFromElementsLiteral
    | BracketLeft BracketRight #emptyListLiteral
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
    | expression BracketLeft left_exp=expression? Colon right_exp=expression? BracketRight #listSlicingExpression
    | expression BracketLeft expression BracketRight #listIndexingExpression
    | literal #literalExpression
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
functionCall: Identifier ParenLeft passedParametersList ParenRight;
passedParametersList: (expression (Comma expression)* Comma?)?;
////

// variable definition and assignment
variableDefinition: GlobalTypeModifier? type Identifier AssignmentOperator expression;
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
functionIdentifier: functionReturnType Colon Identifier;
functionReturnType
    : type
    | VoidType
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

