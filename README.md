# Simple programming language visualiser
**for Compilers and Theory of Compilation course**

## Introduction

### Authors
 - Kacper Dłubała - kacperd@student.agh.edu.pl
 - Andre Baron - andrebaron@student.agh.edu.pl
 
### Goal
The goal is to create an interpreter for a custom programming language, transpiled not to another language, but to a sequence of simple 2D animations meant to help beginner programmers visualise the inner workings of loops, functions, conditional statements, data structures and more.

### Tech stack
- Python 3
- ANTLR4 - used as a parser generator
- PyGame - graphics engine, used for displaying code animations

### How to run
1. Install Python 3.13.3
2. Install the required packages: ```pip install -r requirements.txt```
3. Run: ```python -m program.run_simulation```

### Code example - Quicksort implemented in the language
```
lst[int] tab = [6, 5, 4, 3, 2, 1];

fun int:partition(int p, int r){
    int x = tab[r];
    int i = p - 1;
    int temp = 0;

    lop(int j in [p..r]){
        if(tab[j] <= x){
            i = i + 1;
            temp = tab[i];
            tab[i] = tab[j];
            tab[j] = temp;
        }
    }

    temp = tab[i + 1];
    tab[i + 1] = tab[r];
    tab[r] = temp;

    ret i + 1;
}

fun nul:quicksort(int p, int r){
    int q = 0;
    if(p < r){
        q = partition(p, r);
        quicksort(p, q - 1);
        quicksort(q + 1, r);
    }
}

quicksort(0, 5);

lst[int] res = tab;
```

## The language
### Key features
- Static typing
   - *int* - integer type
   - *flo* - floating-point numbers
   - *bol* - boolean values
   - *str* - string type
   - *lst* - list type
   - *nul* - void function type
- Supports functions and recursion, but not nested function definitions
- Includes conditional statements, while and for-style loops
- Supports global and local variable declarations
- All variables must be initialized at the time of declaring them
- Variables cannot be declared inside conditional statements

### Tokens
| Name | Definition | Description |
|---|---|---|
| WS | `[ \t\r\n]+` | Whitespace, skipped by the parser |
| Comment | `'//' ~[\r\n]*` | Single-line comment, skipped by the parser |
| IntLiteral | `'-'? ([1-9][0-9]*) \| '0'` | Integer literal (e.g., `123`, `-45`, `0`) |
| FloatLiteral | `IntLiteral '.' [0-9]+` | Floating-point literal (e.g., `3.14`, `-2.5`) |
| BoolLiteral | `'true' \| 'false'` | Boolean literal (either `true` or `false`) |
| StringLiteral | `'"' (ESC \| SAFECODEPOINT)* '"'` | String literal enclosed in double quotes, supporting escape sequences |
| AdditiveOperator | `'+' \| '-'` | Addition and subtraction operators |
| MultiplicativeOperator | `'*' \| '/' \| '%'` | Multiplication, division, and modulo operators |
| ComparisonOperator | `'>' \| '>=' \| '<' \| '<=' \| '==' \| '!='` | Comparison operators (greater than, less than, equals, etc.) |
| BooleanOperator | `'and' \| 'or' \| 'xor'` | Logical boolean operators |
| NOTOperator | `'not'` | Logical NOT operator |
| AssignmentOperator | `'='` | Assignment operator |
| InOperator | `'in'` | Membership testing operator |
| IfKeyword | `'if'` | Keyword for conditional statements |
| ElseKeyword | `'els'` | Keyword for the "else" part of conditional statements |
| LoopKeyword | `'lop'` | Keyword for loop (for-loop-style) constructs |
| WhileKeyword | `'whl'` | Keyword for while loops |
| FunctionKeyword | `'fun'` | Keyword for function declarations |
| ReturnKeyword | `'ret'` | Keyword for returning from a function |
| IntType | `'int'` | Type declaration for integers |
| FloatType | `'flo'` | Type declaration for floating-point numbers |
| StringType | `'str'` | Type declaration for strings |
| BoolType | `'bol'` | Type declaration for booleans |
| ListType | `'lst'` | Type declaration for lists |
| VoidType | `'nul'` | Type declaration for a void type |
| GlobalTypeModifier | `'glo'` | Modifier for global type declarations |
| Identifier | `[a-zA-Z_][a-zA-Z0-9_]*` | User-defined identifiers (variables, function names, etc.) |
| Semicolon | `';'` | Statement terminator |
| Colon | `':'` | Used in function declarations and list slicing |
| Comma | `','` | Separator in lists, arguments, etc. |
| DoubleDot | `'..'` | Range operator |
| BracketLeft | `'['` | Left square bracket, used for list literals or indexing |
| BracketRight | `']'` | Right square bracket |
| CurlyLeft | `'{'` | Left curly brace, used for code blocks |
| CurlyRight | `'}'` | Right curly brace |
| ParenLeft | `'('` | Left parenthesis, used for grouping or function calls |
| ParenRight | `')'` | Right parenthesis |
| ERROR_CHAR | `.` | Catches any unmatched characters as an error, necessary for syntax highlighting |

### Grammar

```antlr
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
    : expression BracketLeft left_exp=expression? Colon right_exp=expression? BracketRight #listSlicingExpression
    | expression BracketLeft expression BracketRight #listIndexingExpression
    | Identifier #identifierExpression
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
    | lValue BracketLeft expression BracketRight
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

```

### Error handling

Apart from the parsing functionality present in ANTLR4, our language provides custom compile-time error handling, which includes:
- checking if identifiers have been defined, as well as checking if they haven't been defined multiple times
- checking if functions return values in all control paths
- robust static type checking

The interpreter also includes runtime error handling, for example for out-of-bounds list indices or arithmetic errors.


## GUI
The GUI is an integral part of the project. It lets users inspect variable values in real time, track expression calculations and see which lines of code are currently being executed, with the integrated text editor providing custom syntax highlighting. Using the interface, code execution can be paused at any time and its speed can be controlled.

### GUI elements
![image1](/images/1.png)

### Error example
![image2](/images/2.png)
