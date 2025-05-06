from antlr4 import *
from base.SPLVParser import SPLVParser
from base.SPLVParserListener import SPLVParserListener

class Listener(SPLVParserListener):
    def __init__(self):
        self.def_scopes: dict[str, dict[str, str]] = {
            "glo" : {},
        }
        
        self.current_scope = "glo"