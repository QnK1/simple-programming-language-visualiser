lexer grammar SPLVLexer;

// whitespace
WS: [ \t\r\n]+ -> skip;

// comments
Comment: '//' ~[\r\n]* -> channel(HIDDEN);

// identifiers
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

// literals
IntLiteral: '-'? ([1-9][0-9]*) | '0';
FloatLiteral: IntLiteral '.' [0-9]*;
BoolLiteral: 'true' | 'false';
StringLiteral: '"' (ESC | SAFECODEPOINT)* '"'; //from JSON grammar
fragment ESC: '\\' (["\\/bfnrt]); //
fragment SAFECODEPOINT: ~ ["\\\u0000-\u001F]; //

// operators
AdditiveOperator: '+' | '-';
MultiplicativeOperator: '*' | '/' | '%';
ComparisonOperator: '>' | '>=' | '<' | '<=' | '==' | '!=';
BooleanOperator: 'and' | 'or' | 'xor';
NOTOperator: '!';
AssignmentOperator: '=';
InOperator: 'in';

// keywords
IfKeyword: 'if';
LoopKeyword: 'lop';
WhileKeyword: 'while';
FunctionKeyword: 'fun';
ReturnKeyword: 'ret';

// type declarations
Type: 'int' | 'flo' | 'str' | 'bol' | 'lst';
GlobalTypeModifier: 'glob';

// special characters
Semicolon: ';';
Colon: ':';
Comma: ',';
BracketLeft: '[';
BracketRight: ']';
CurlyLeft: '{';
CurlRight: '}';
ParenLeft: '(';
ParenRight: ')';

