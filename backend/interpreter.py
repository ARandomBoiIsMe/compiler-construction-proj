class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def interprete_ast(self):
        for statement in self.ast:
            if statement.type == 'AssignmentStmt':
                variable_name = statement.identifier.name
                expression = statement.expr
                value = self.evaluate_expression(expression)
                self.symbol_table[variable_name] = value

            elif statement.type == 'PrintStmt':
                expression = statement.expr
                value = self.evaluate_expression(expression)
                print(value)

    def evaluate_expression(self, statement):
        if statement.type == 'IntegerLiteral':
            return int(statement.value)
        
        elif statement.type == 'Identifier':
            if statement.name not in self.symbol_table:
                raise ValueError(f"Variable '{statement.name}' not found")
            return self.symbol_table[statement.name]
        
        elif statement.type == 'BinaryExpr':
            left = self.evaluate_expression(statement.left)
            right = self.evaluate_expression(statement.right)

            if statement.operator == '+':
                return left + right
            elif statement.operator == '-':
                return left - right
            elif statement.operator == '*':
                return left * right
            elif statement.operator == '/':
                return left // right
            elif statement.operator == '%':
                return left % right
            elif statement.operator == '**':
                return left ^ right