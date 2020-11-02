# 0 1 1 2 3 5 8 13 ...

A = 0
B = 1
C = 0
counter = 5

for x in range(counter):
    print(A)
    A = A + B
    B = C
    C = A
    
