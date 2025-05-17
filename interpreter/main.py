from antlr4 import *
from pathlib import Path

from .base.SPLVLexer import SPLVLexer
from .base.SPLVParser import SPLVParser
from .declaration_checker import DeclarationChecker
from .type_checker import TypeChecker
from .return_checker import ReturnChecker


def run(source: str):
    lexer = SPLVLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = SPLVParser(stream)
    declaration_checker = DeclarationChecker()
    return_checker = ReturnChecker()
    type_checker = TypeChecker()
    
    parser.addParseListener(declaration_checker)

    tree = parser.program()
    
    return_checker.visit(tree)
    type_checker.visit(tree)
    

    # print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    with open(Path(__file__).resolve().parent / Path("test.txt"), "r") as f:
        input_text = f.read()

    output = run(input_text)