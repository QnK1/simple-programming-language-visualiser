from antlr4 import *
from pathlib import Path

from .base.SPLVLexer import SPLVLexer
from .base.SPLVParser import SPLVParser
from .declaration_checker import DeclarationChecker
from .type_checker import TypeChecker
from .return_checker import ReturnChecker
from .ParsingErrorListener import ParsingErrorListener
from .errors import DeclarationException, CompilationError, ReturnException, TypeException
from .runner import Runner


def run(source: str) -> tuple[list[CompilationError], list]:
    lexer = SPLVLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = SPLVParser(stream)
    declaration_checker = DeclarationChecker()
    return_checker = ReturnChecker()
    type_checker = TypeChecker()
    runner = Runner()

    parser.addParseListener(declaration_checker)

    compile_time_errors = []

    error_listener = ParsingErrorListener()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    declaration_errors = []
    tree = None
    try:
        tree = parser.program()
    except DeclarationException as e:
        declaration_errors.append(CompilationError(e.line, e.column, e.msg))

    compile_time_errors.extend(error_listener.errors)
    compile_time_errors.extend(declaration_errors)

    program = None
    if tree is not None and len(compile_time_errors) == 0:
        try:
            return_checker.visit(tree)
            type_checker.visit(tree)

            program = runner.visit(tree)
        except (ReturnException, TypeException) as e:
            compile_time_errors.append(CompilationError(e.line, e.column, e.msg))


    return compile_time_errors, program


if __name__ == "__main__":
    with open(Path(__file__).resolve().parent / Path("test3.txt"), "r") as f:
        input_text = f.read()

    compilation_errors, program = run(input_text)

    if program is not None:
        for s in program:
            print(f"\n{s}")
            for key, val in s.__dict__.items():
                print(key, val)
    else:
        print(compilation_errors)