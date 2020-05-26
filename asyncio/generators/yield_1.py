def nextSquare(num_squares):
    # next Square maintains state with each call 
    # but only works in a loop
    for s in range(num_squares):
        yield s*s

def nextOne(num):
    # next Square maintains state with each call 
    # but only works in a loop
    for i in range(num):
        yield i

for sq in nextSquare(10):
    print(sq)

no=print(list(nextOne(10)))