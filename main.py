from frontend import lexer, parser

def main():
    with open('source_code.py', 'r') as file:
        source_code = file.read()

    _lexer = lexer.Lexer(source_code)
    tokens = _lexer.get_tokens()

    _parser = parser.Parser(tokens)
    print(_parser.parse().body)

if __name__ == '__main__':
    main()