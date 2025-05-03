from antlr4 import *
from parser.SPLVLexer import SPLVLexer
from parser.SPLVParser import SPLVParser

with open("test.jp2gmd", "r") as f:
    input_text = f.read()

# input_text = input("")
lexer = SPLVLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = SPLVParser(stream)

tree = parser.program()

print(tree.toStringTree(recog=parser))