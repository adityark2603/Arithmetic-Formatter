def arithmetic_arranger(problems, show_answers=False):
    # Check for the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top = []
    bottom = []
    dashes = []
    results = []
    
    for problem in problems:
        # Split the problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check if operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if numbers contain only digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check if numbers are within 4 digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the result if needed
        if operator == '+':
            result = str(int(num1) + int(num2))
        elif operator == '-':
            result = str(int(num1) - int(num2))
        
        # Calculate the length of the longest number
        width = max(len(num1), len(num2)) + 2  # +2 for the operator and space
        
        # Add the components to the respective lists
        top.append(num1.rjust(width))
        bottom.append(f"{operator} {num2.rjust(width - 2)}")  # Align operator with right padding
        dashes.append('-' * width)
        if show_answers:
            results.append(result.rjust(width))
    
    # Format the output lines
    arranged_problems = '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems
