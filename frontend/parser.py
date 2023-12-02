from frontend.lexer import Token, TokenType
from typing import List

class Identifier:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Identifier(name={self.name})'

class IntegerLiteral:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'IntegerLiteral(value={self.value})'

class BinaryExpr:
    def __init__(self, left_operand, operator, right_operand):
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand
    
    def __repr__(self):
        return f'BinaryExpr(left_operand={self.left_operand}, operator={self.operator}, right_operand={self.right_operand})'

class UnaryExpr:
    def __init__(self, unary_operand, operator):
        self.unary_operand = unary_operand
        self.operator = operator
    
    def __repr__(self):
        return f'UnaryExpr(unary_operand={self.unary_operand}, operator={self.operator})'

class AssignmentStmt:
    def __init__(self, identifier, expr):
        self.identifier = identifier
        self.expr = expr
    
    def __repr__(self):
        return f'AssignmentStmt(identifier={self.identifier}, expr={self.expr})'

class ReturnStmt:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'ReturnStmt(value={self.value})'

class Program:
    def __init__(self, body):
        self.body = body
    
    def __repr__(self):
        return f'Program(body={self.body})'

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.index = 0
        self.program_body = []
        self.current_token = None

    def parse(self):
        while self.tokens[self.index].type != TokenType.EOF:
            self.current_token = self.tokens[self.index]

            if self.current_token.type == TokenType.IDENTIFIER:
                expression = self.parse_assignment()
                self.program_body.append(expression)

            elif (
                self.current_token.type == TokenType.IDENTIFIER and
                self.current_token.value == 'print'
            ):
                pass

        return Program(self.program_body)

    def parse_assignment(self):
        identifier = self.parse_non_terminal_expression()

        if self.current_token.type != TokenType.EQUAL:
            return None
        
        self.move_forward()
        expression = self.parse_additive_expression()

        return AssignmentStmt(identifier, expression)

    # Handles addition and subtraction expressions
    # 10 - 7
    def parse_additive_expression(self):
        left = self.parse_non_terminal_expression()

        if not left:
            return None
        
        expr = left
        while (self.current_token.type == TokenType.PLUS or 
               self.current_token.type == TokenType.MINUS
               ):
            operator = self.current_token
            self.move_forward()
            right = self.parse_non_terminal_expression()

            expr = BinaryExpr(expr, operator, right)

        return expr

    # Handles divison and multiplication expressions
    def parse_multiplicative_expression(self):
        left = self.parse_non_terminal_expression()

        if not left:
            return None
        
        while (self.current_token.type == TokenType.SLASH or 
               self.current_token.type == TokenType.STAR
               ):
            pass

    def parse_non_terminal_expression(self):
        match (self.current_token.type):
            case TokenType.IDENTIFIER:
                identifier = Identifier(self.current_token.value)
                self.move_forward()
                return identifier
            case TokenType.INTEGER_LITERAL:
                number = IntegerLiteral(self.current_token.value)
                self.move_forward()
                return number
            case _:
                return None
    
    def look_ahead(self, distance: int = 1):
        next_token_index = self.index + 1

        return self.tokens[next_token_index:next_token_index + distance]
    
    def move_forward(self):
        self.index += 1
        self.current_token = self.tokens[self.index]