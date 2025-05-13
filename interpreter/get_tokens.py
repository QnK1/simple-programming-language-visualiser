from antlr4 import *
from .base.SPLVLexer import SPLVLexer
from dataclasses import dataclass

# a dataclass representing a token used for syntax highlighting
@dataclass
class SyntaxToken:
    line: int
    column: int
    text: str
    type: str
    

# returns all info about tokens needed for syntax highlighting
def get_tokens(code: str) -> list[SyntaxToken]:
    lexer = SPLVLexer(InputStream(code))
    stream = CommonTokenStream(lexer)

    stream.fill()
    
    return [SyntaxToken(t.line, t.column, t.text, SPLVLexer.symbolicNames[t.type]) for t in stream.tokens]


if __name__ == "__main__":
    with open("./test.txt", "r") as f:
        input_text = f.read()
    
    tokens = get_tokens(input_text)

    for token in tokens:
        print(token)
