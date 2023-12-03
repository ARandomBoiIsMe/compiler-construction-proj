from frontend import lexer, parser
from backend import interpreter
import sys

def main():
    source_code = sys.argv[1]

    _lexer = lexer.Lexer(source_code)
    tokens = _lexer.get_tokens()

    _parser = parser.Parser(tokens)
    program = _parser.parse()

    _intepreter = interpreter.Interpreter(program.body)
    _intepreter.interprete_ast()

if __name__ == '__main__':
    main()