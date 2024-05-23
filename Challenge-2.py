
import re

def add_implicit_multiplication(expression):
    # Insert explicit multiplication where there's implicit multiplication
    expression = re.sub(r'(?<=\d)(?=\()', '*', expression)  # Between number and opening parenthesis
    expression = re.sub(r'(?<=\))(?=\d)', '*', expression)  # Between closing parenthesis and number
    expression = re.sub(r'(?<=\))(?=\()', '*', expression)  # Between closing and opening parenthesis
    return expression

def balance_parentheses(expression):
    # Count opening and closing parentheses
    open_parentheses = expression.count('(')
    close_parentheses = expression.count(')')
    # Add missing closing parentheses
    if open_parentheses > close_parentheses:
        expression += ')' * (open_parentheses - close_parentheses)
    return expression

def evaluate_expression(expression):
    try:
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')
        # Add implicit multiplication
        expression = add_implicit_multiplication(expression)
        # Balance parentheses
        expression = balance_parentheses(expression)
        # Debug: print the expression to be evaluated
        print(f"Evaluating: {expression}")
        # Evaluate the expression
        result = eval(expression)
        return result
    except Exception as e:
        # If there's an error in evaluation, return the error message
        return str(e)

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if '=' in line:
                expr = line.split('=')[0].strip()
                result = evaluate_expression(expr)
                outfile.write(f"{line} {result}\n")

# Specify the input and output file paths
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# Process the file
process_file(input_file_path, output_file_path)