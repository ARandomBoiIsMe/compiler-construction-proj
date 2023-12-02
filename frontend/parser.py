from frontend.lexer import Token, TokenType
from typing import List

class Identifier:
    def __init__(self, name):
        self.name = name

class IntegerLiteral:
    def __init__(self, value):
        self.value = value

class BinaryExpr:
    def __init__(self, left_operand, operator, right_operand):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

class UnaryExpr:
    def __init__(self, unary_operand, operator):
        self.unary_operand = unary_operand
        self.operator = operator

class AssignmentStmt:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class ReturnStmt:
    def __init__(self, value):
        self.value = value

class Function:
    def __init__(self, function_name, statement):
        self.function_name = function_name
        self.statement = statement

class Program:
    def __init__(self, body):
        self.body = body

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.index = 0
        self.program_body = []
        self.current_token = None

    def parse(self):
        while self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]

            if self.current_token.type == TokenType.IDENTIFIER:
                parse_expression()

    def parse_expression(self):
        # Handle assignments
        if self.look_ahead()[0].type == TokenType.EQUAL:
            pass

    def consume(expected_type):
        pass
    
    def look_ahead(self, distance: int = 1):
        next_token_index = self.index + 1

        return self.tokens[next_token_index:next_token_index + distance]
"""
    def parse_statement(self):
        self.parse_expression()

    def parse_expression(self):
        if self.tokens[self.index].type == TokenType.IDENTIFIER:
            return

    def parse_assignment_statement(self):
        identifier = self.parse_identifier()
        self.consume_token(TokenType.EQUAL) # Skips equal to sign
        value = self.parse_integer()

        return AssignmentStmt(identifier=identifier, value=value)
    
    def parse_simple_return_function(self):
        if self.consume_token(TokenType.KEYWORD).value != "def":
            raise SyntaxError(f"Expected function start.")
        
        function_name = self.parse_identifier()

        self.consume_token(TokenType.LEFT_PAREN)
        self.consume_token(TokenType.RIGHT_PAREN)
        self.consume_token(TokenType.COLON)

        if self.consume_token(TokenType.KEYWORD).value != "return":
            raise SyntaxError(f"Expected return start.")
        
        return_value = self.consume_token(TokenType.INTEGER_LITERAL)
        return_stmt = ReturnStmt(return_value)

        return Function(function_name, return_stmt)

    def parse_identifier(self):
        token = self.consume_token(TokenType.IDENTIFIER)
        return Identifier(token.value)
    
    def parse_integer(self):
        token = self.consume_token(TokenType.INTEGER_LITERAL)
        return IntegerLiteral(int(token.value))
    
"""        