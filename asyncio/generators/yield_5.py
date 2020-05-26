def generatorA1():
    # generator returns i first: 0 < x < 9
    for i in range(10):
        yield i

def generatorA2():
    # then generator returns j: 15 < x < 19
    for j in range(15,20):
        yield j

def generatorA():
    # eliminates the intermediate iterator loop from yield_4 by 
    # communicating directly to the generators
    yield from generatorA1()
    yield from generatorA2()

def main():
    for x in generatorA():
        print(x)

if __name__=="__main__":
    main()