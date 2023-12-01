from frontend import lexer, parser

def main():
    with open('source_code.py', 'r') as file:
        source_code = file.read()

    _lexer = lexer.Lexer(source_code)
    tokens = _lexer.get_tokens()

    print(tokens)

    _parser = parser.Parser(tokens)

if __name__ == '__main__':
    main()