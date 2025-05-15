from interpreter.get_tokens import get_tokens
from interpreter.base.SPLVLexer import SPLVLexer
from pygments.token import Token
from pathlib import Path
import pygame
from pygame_texteditor import TextEditor

class SyntaxHighlighter:
    
    def __init__(self):
        lexer = SPLVLexer()
        
        self.antlr_to_pygments =  {
            lexer.WS : Token.Whitespace,
            lexer.Comment : Token.Comment,
            lexer.IntLiteral : Token.Name.Function,
            lexer.FloatLiteral : Token.Name.Function,
            lexer.BoolLiteral : Token.Name.Function,
            lexer.StringLiteral : Token.Literal.String,
            lexer.AdditiveOperator : Token.Operator,
            lexer.MultiplicativeOperator : Token.Operator,
            lexer.ComparisonOperator : Token.Operator,
            lexer.BooleanOperator : Token.Operator,
            lexer.NOTOperator : Token.Operator,
            lexer.AssignmentOperator : Token.Operator,
            lexer.InOperator : Token.Operator,
            lexer.IfKeyword : Token.Keyword,
            lexer.ElseKeyword : Token.Keyword,
            lexer.LoopKeyword : Token.Keyword,
            lexer.WhileKeyword : Token.Keyword,
            lexer.FunctionKeyword : Token.Keyword,
            lexer.ReturnKeyword : Token.Keyword,
            lexer.GlobalTypeModifier : Token.Keyword,
            lexer.IntType : Token.Name.Builtin,
            lexer.FloatType : Token.Name.Builtin,
            lexer.StringType : Token.Name.Builtin,
            lexer.BoolType : Token.Name.Builtin,
            lexer.ListType : Token.Name.Builtin,
            lexer.VoidType : Token.Name.Builtin,
            lexer.Identifier : Token.Name,
            lexer.Semicolon : Token.Punctuation,
            lexer.Colon : Token.Punctuation,
            lexer.Comma : Token.Punctuation,
            lexer.DoubleDot : Token.Punctuation,
            lexer.BracketLeft : Token.Punctuation,
            lexer.BracketRight : Token.Punctuation,
            lexer.CurlyLeft : Token.Punctuation,
            lexer.CurlyRight : Token.Punctuation,
            lexer.ParenLeft : Token.Punctuation,
            lexer.ParenRight : Token.Punctuation,
        }
    

    def get_tokens(self, code: str):
        tokens = get_tokens(code)

        for token in tokens:
            if token.type != -1:
                pygments_token_type = self.antlr_to_pygments.get(token.type, Token.Text)
                # yield token.start, pygments_token_type, token.text
                yield pygments_token_type, token.text

