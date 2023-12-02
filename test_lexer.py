from frontend import lexer
from frontend.lexer import Token, TokenType

def test_assignment():
    _lexer = lexer.Lexer("x = 1")
    assert _lexer.get_tokens() == [
        Token(value='x', type=TokenType.IDENTIFIER),
        Token(value='=', type=TokenType.EQUAL),
        Token(value='1', type=TokenType.INTEGER_LITERAL),
        Token(value='', type=TokenType.EOF)
    ], "Token list does not match"

    _lexer = lexer.Lexer("x = 1 + 2 * 3")
    assert _lexer.get_tokens() == [
        Token(value='x', type=TokenType.IDENTIFIER),
        Token(value='=', type=TokenType.EQUAL),
        Token(value='1', type=TokenType.INTEGER_LITERAL),
        Token(value='+', type=TokenType.PLUS),
        Token(value='2', type=TokenType.INTEGER_LITERAL),
        Token(value='*', type=TokenType.STAR),
        Token(value='3', type=TokenType.INTEGER_LITERAL),
        Token(value='', type=TokenType.EOF)
    ], "Token list does not match"

    _lexer = lexer.Lexer("steps = 12\nanswer = steps * 2")
    assert _lexer.get_tokens() == [
    Token(value='steps', type=TokenType.IDENTIFIER),
    Token(value='=', type=TokenType.EQUAL),
    Token(value='12', type=TokenType.INTEGER_LITERAL),
    Token(value='answer', type=TokenType.IDENTIFIER),
    Token(value='=', type=TokenType.EQUAL),
    Token(value='steps', type=TokenType.IDENTIFIER),
    Token(value='*', type=TokenType.STAR),
    Token(value='2', type=TokenType.INTEGER_LITERAL),
    Token(value='', type=TokenType.EOF)
    ], "Token list does not match"
    
if __name__ == '__main__':
    test_assignment()