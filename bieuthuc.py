# Function to solve each test case
def solve_expression(expression):
    stack = []
    result = [0] * len(expression)
    counter = 1

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                open_index = stack.pop()
                result[open_index] = counter
                result[i] = counter
                counter += 1

    # Print the result, filtering out non-parenthesis characters
    print(' '.join(str(result[i]) for i in range(len(expression)) if expression[i] in '()'))

# Main function to handle input and output
def main():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        expression = input().strip()  # Read the expression
        solve_expression(expression)

if __name__ == "__main__":
    main()
