# --- FIBONACCI EXERCISE
n1 = 0
n2 = 1
print("0 1", end=' ')

for i in range(2, 11):
    term_n = n1 + n2
    print(term_n, end=' ')

    n1 = n2
    n2 = term_n
