# --- SESSION 2; 2 EXERCISE
def fibonacci(n):
    if n in [0, 1]:
        return n

    n1 = 0
    n2 = 1

    term_n = 0

    for i in range(2, n+1):
        term_n = n1 + n2

        n1 = n2
        n2 = term_n

    return term_n


print("5th Fibonacci term: ", fibonacci(5))
print("10th Fibonacci term:", fibonacci(10))
print("15th Fibonacci term:", fibonacci(15))
