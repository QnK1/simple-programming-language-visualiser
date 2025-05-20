from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import RecognitionException
from antlr4.atn.ATNConfigSet import ATNConfigSet
from .errors import CompilationError

class ParsingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, charPositionInLine, msg, e: RecognitionException):
        self.errors.append(CompilationError(line, charPositionInLine, msg))
