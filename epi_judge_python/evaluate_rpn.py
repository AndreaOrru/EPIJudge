from test_framework import generic_test


def evaluate(expression: str) -> int:
    intermediate_results = []
    operations = {
        '+': lambda x, y: x  + y,
        '-': lambda x, y: x  - y,
        '*': lambda x, y: x  * y,
        '/': lambda x, y: x // y,
    }

    i = start = 0
    while i < len(expression):
        while i < len(expression) and expression[i] != ',':
            i += 1
        
        op = expression[start: i]
        if op in operations:
            y = intermediate_results.pop()
            x = intermediate_results.pop()
            intermediate_results.append(operations[op](x, y))
        else:
            intermediate_results.append(int(op))

        i += 1
        start = i

    return intermediate_results[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
