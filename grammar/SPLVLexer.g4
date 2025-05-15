lexer grammar SPLVLexer;

// whitespace
// WS: [ \t\r\n]+ -> skip;
WS : [ \t\r\n]+ -> channel(HIDDEN);

// comments
Comment: '//' ~[\r\n]* -> channel(HIDDEN);

// literals
IntLiteral: '-'? ([1-9][0-9]*) | '0';
FloatLiteral: IntLiteral '.' [0-9]+;
BoolLiteral: 'true' | 'false';
StringLiteral: '"' (ESC | SAFECODEPOINT)* '"'; //from JSON grammar
fragment ESC: '\\' (["\\/bfnrt]); //
fragment SAFECODEPOINT: ~ ["\\\u0000-\u001F]; //

// operators
AdditiveOperator: '+' | '-';
MultiplicativeOperator: '*' | '/' | '%';
ComparisonOperator: '>' | '>=' | '<' | '<=' | '==' | '!=';
BooleanOperator: 'and' | 'or' | 'xor';
NOTOperator: 'not';
AssignmentOperator: '=';
InOperator: 'in';

// keywords
IfKeyword: 'if';
ElseKeyword: 'els';
LoopKeyword: 'lop';
WhileKeyword: 'whl';
FunctionKeyword: 'fun';
ReturnKeyword: 'ret';

// type declarations
IntType: 'int';
FloatType: 'flo';
StringType: 'str';
BoolType: 'bol';
ListType: 'lst';
VoidType: 'nul';
GlobalTypeModifier: 'glo';

// identifiers
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

// special characters
Semicolon: ';';
Colon: ':';
Comma: ',';
DoubleDot: '..';
BracketLeft: '[';
BracketRight: ']';
CurlyLeft: '{';
CurlyRight: '}';
ParenLeft: '(';
ParenRight: ')';

// unmatched tokens
ERROR_CHAR: . ;