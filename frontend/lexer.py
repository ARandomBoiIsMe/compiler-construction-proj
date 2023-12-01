from enum import Enum
import keyword
from dataclasses import dataclass

class TokenType(Enum):
    KEYWORD = 1
    IDENTIFIER = 2
    INTEGER_LITERAL = 3
    STRING_LITERAL = 4
    DOUBLE_STAR = 5
    PLUS = 6
    STAR = 7
    MINUS = 8
    SLASH = 9
    DOUBLE_SLASH = 10
    PERCENT = 11
    PLUS_EQUAL = 12
    MINUS_EQUAL = 13
    SLASH_EQUAL = 14
    DOUBLE_SLASH_EQUAL = 15
    PERCENT_EQUAL = 16
    STAR_EQUAL = 17
    EXCLAMATION = 18
    LESS_THAN = 19
    GREATER_THAN = 20
    LESS_EQUAL = 21
    GREATER_EQUAL = 22
    NOT_EQUAL = 23
    EQUAL_EQUAL = 24
    EQUAL = 25
    LEFT_PAREN = 26
    RIGHT_PAREN = 27
    LEFT_SQUARE_BRACE = 28
    RIGHT_SQUARE_BRACE = 29
    COLON = 30
    COMMA = 32
    INVALID = 33
    DOUBLE_STAR_EQUAL = 34
    LEFT_CURLY_BRACE = 35
    RIGHT_CURLY_BRACE = 36
    PERIOD = 37
    FLOAT = 38

@dataclass
class Token:
    value: str
    type: TokenType

class Lexer:
    def __init__(self, source_code: str):
        self.source_code = source_code.strip()
        self.index = 0
        self.current_lexeme = ""
        self.tokens = []
        
    def get_tokens(self):
        while self.index < len(self.source_code):
            # Skips whitespace
            if self.source_code[self.index].isspace():
                self.index += 1
                continue

            # Skips comments
            if self.source_code[self.index] == "#":
                while self.index < len(self.source_code) and self.source_code[self.index] != "\n":
                    self.index += 1

                continue

            # Handles keywords and identifiers
            if self.source_code[self.index] == "_" or self.source_code[self.index].isalpha():
                while self.index < len(self.source_code) and (
                    self.source_code[self.index].isalnum() or self.source_code[self.index] == "_"
                ):
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                # If the token is not a keyword, then it's an identifier
                if self.current_lexeme in keyword.kwlist:
                    self.tokens.append(Token(self.current_lexeme, TokenType.KEYWORD))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.IDENTIFIER))

                self.current_lexeme = ""
                continue

            # Handles string literals
            if self.source_code[self.index] == "'" or self.source_code[self.index] == '"':
                quote_type = self.source_code[self.index]
                self.current_lexeme += self.consume_characters() # Moves to first character in string

                while self.index < len(self.source_code) and self.source_code[self.index] != quote_type:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                self.index += 1 # Moves over closing quotation

                self.tokens.append(Token(self.current_lexeme, TokenType.STRING_LITERAL))
                self.current_lexeme = ""
                continue

            # Handles integer literals
            if self.source_code[self.index].isdigit():
                while self.index < len(self.source_code) and self.source_code[self.index].isdigit():
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                self.tokens.append(Token(self.current_lexeme, TokenType.INTEGER_LITERAL))
                self.current_lexeme = ""
                continue
            
            # Handles arithmetic operators
            # ----------------------------
            if self.source_code[self.index] == "+":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "+=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.PLUS_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.PLUS))

                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == "%":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "%=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.PERCENT_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.PERCENT))

                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == "-":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "-=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.MINUS_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.MINUS))
                    
                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == "*":
                if self.look_ahead(2) == "*=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters(2)
                elif self.look_ahead() == "*":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                elif self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1
                    
                if self.current_lexeme == "**=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.DOUBLE_STAR_EQUAL))
                elif self.current_lexeme == "**":
                    self.tokens.append(Token(self.current_lexeme, TokenType.DOUBLE_STAR))
                elif self.current_lexeme == "*=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.STAR_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.STAR))
                    
                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == "/":
                if self.look_ahead(2) == "/=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters(2)
                elif self.look_ahead() == "/":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                elif self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "//=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.DOUBLE_SLASH_EQUAL))
                elif self.current_lexeme == "//":
                    self.tokens.append(Token(self.current_lexeme, TokenType.DOUBLE_SLASH))
                elif self.current_lexeme == "/=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.SLASH_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.SLASH))
                    
                self.current_lexeme = ""
                continue
            # ----------------------------

            # Handles logical operators
            # -------------------------
            if self.source_code[self.index] == "<":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "<=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.LESS_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.LESS_THAN))

                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == ">":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == ">=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.GREATER_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.GREATER_THAN))

                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == "!":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "!=":
                    self.tokens.append(Token(self.current_lexeme, TokenType.NOT_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.EXCLAMATION))

                self.current_lexeme = ""
                continue

            if self.source_code[self.index] == "=":
                if self.look_ahead() == "=":
                    self.current_lexeme += self.source_code[self.index]
                    self.current_lexeme += self.consume_characters()
                else:
                    self.current_lexeme += self.source_code[self.index]
                    self.index += 1

                if self.current_lexeme == "==":
                    self.tokens.append(Token(self.current_lexeme, TokenType.EQUAL_EQUAL))
                else:
                    self.tokens.append(Token(self.current_lexeme, TokenType.EQUAL))

                self.current_lexeme = ""
                continue
            # -------------------------

            # Handles other symbols
            # ---------------------
            if self.source_code[self.index] == "(":
                self.add_single_token(TokenType.LEFT_PAREN)
                continue

            if self.source_code[self.index] == ")":
                self.add_single_token(TokenType.RIGHT_PAREN)
                continue

            if self.source_code[self.index] == "[":
                self.add_single_token(TokenType.LEFT_SQUARE_BRACE)
                continue

            if self.source_code[self.index] == "]":
                self.add_single_token(TokenType.RIGHT_SQUARE_BRACE)
                continue

            if self.source_code[self.index] == "{":
                self.add_single_token(TokenType.LEFT_CURLY_BRACE)
                continue

            if self.source_code[self.index] == "}":
                self.add_single_token(TokenType.RIGHT_CURLY_BRACE)
                continue

            if self.source_code[self.index] == ":":
                self.add_single_token(TokenType.COLON)
                continue

            if self.source_code[self.index] == ",":
                self.add_single_token(TokenType.COMMA)
                continue

            if self.source_code[self.index] == ".":
                self.add_single_token(TokenType.PERIOD)
                continue
            # ---------------------

            # Handles invalid operators
            else:
                self.add_single_token(TokenType.INVALID)
                continue

        return self.tokens

    # Adds a single-character token to the token list
    def add_single_token(self, token_type: TokenType):
        self.current_lexeme += self.source_code[self.index]
        self.tokens.append(Token(self.current_lexeme, token_type))
        self.current_lexeme = ""
        self.index += 1

    # Looks {distance} characters into the string
    def look_ahead(self, distance: int = 1):
        next_char_index = self.index + 1

        return self.source_code[next_char_index:next_char_index + distance]
    
    # Looks {distance} characters into the string and sets cursor to the start of the next token
    def consume_characters(self, distance: int = 1):
        next_char_index = self.index + 1
        self.index = next_char_index + distance # Moves cursor to start of next token

        return self.source_code[next_char_index:next_char_index + distance]