from frontend.lexer import Token, TokenType
from typing import List

class SyntaxAnalyzer:
    def _init_(self, tokens: List[Token]):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        self.program()

    def match(self, expected_type):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == expected_type:
            self.current_token_index += 1
        else:
            raise SyntaxError(f"Expected {expected_type}, found {self.tokens[self.current_token_index].type}")

    def program(self):
        while self.current_token_index < len(self.tokens):
            self.statement()

    def statement(self):
        if self.tokens[self.current_token_index].type == TokenType.KEYWORD:
            self.keyword_statement()
        elif self.tokens[self.current_token_index].type == TokenType.IDENTIFIER:
            self.assignment_statement()
        else:
            raise SyntaxError("Invalid statement")

    def keyword_statement(self):
        # Handle different keyword statements
        pass

    def assignment_statement(self):
        self.match(TokenType.IDENTIFIER)
        self.match(TokenType.EQUAL)
        self.expression()

    def expression(self):
        self.term()
        while (
            self.tokens[self.current_token_index].type in [TokenType.PLUS, TokenType.MINUS]
        ):
            operator = self.tokens[self.current_token_index].type
            self.match(operator)
            self.term()

    def term(self):
        self.factor()
        while (
            self.tokens[self.current_token_index].type in [TokenType.STAR, TokenType.SLASH]
        ):
            operator = self.tokens[self.current_token_index].type
            self.match(operator)
            self.factor()

    def factor(self):
        if self.tokens[self.current_token_index].type == TokenType.INTEGER_LITERAL:
            self.match(TokenType.INTEGER_LITERAL)
        elif self.tokens[self.current_token_index].type == TokenType.IDENTIFIER:
            self.match(TokenType.IDENTIFIER)
        elif self.tokens[self.current_token_index].type == TokenType.LEFT_PAREN:
            self.match(TokenType.LEFT_PAREN)
            self.expression()
            self.match(TokenType.RIGHT_PAREN)
        else:
            raise SyntaxError("Invalid factor")