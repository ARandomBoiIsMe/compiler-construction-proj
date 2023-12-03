from frontend import lexer, parser
import interpreter

def main():
    with open('source_code.py', 'r') as file:
        source_code = file.read()

    _lexer = lexer.Lexer(source_code)
    tokens = _lexer.get_tokens()

    _parser = parser.Parser(tokens)
    program = _parser.parse()

    _intepreter = interpreter.Interpreter(program.body)
    _intepreter.interprete_ast()

if __name__ == '__main__':
    main()