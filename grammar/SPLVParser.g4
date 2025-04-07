parser grammar SPLVParser;

options {
    tokenVocab = SPLVLexer;
}

// starting symbol
program: statement* EOF;

// statements
statement
    : variableDefinition
    | variableAssignment
    | functionDefinition
    | functionCall
    | controlStatement
    ;

// statements inside loop/if blocks
innerStatement
    : variableAssignment
    | functionCall
    | controlStatement
    ;