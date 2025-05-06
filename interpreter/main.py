from antlr4 import *
from base.SPLVLexer import SPLVLexer
from base.SPLVParser import SPLVParser
from listener import Listener

def run(source: str):
    lexer = SPLVLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = SPLVParser(stream)
    listener = Listener()
    
    parser.addParseListener(listener)

    tree = parser.program()

    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        input_text = f.read()

    output = run(input_text)