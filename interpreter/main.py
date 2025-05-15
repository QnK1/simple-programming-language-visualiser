from antlr4 import *
from .base.SPLVLexer import SPLVLexer
from .base.SPLVParser import SPLVParser
from .listener import Listener
from pathlib import Path

def run(source: str):
    lexer = SPLVLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = SPLVParser(stream)
    listener = Listener()
    
    parser.addParseListener(listener)

    tree = parser.program()

    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    with open(Path(__file__).resolve().parent / Path("test.txt"), "r") as f:
        input_text = f.read()

    output = run(input_text)