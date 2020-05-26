def generatorA1():
    # generator returns i first: 0 < x < 9
    for i in range(10):
        yield i

def generatorA2():
    # then generator returns j: 15 < x < 19
    for j in range(15,20):
        yield j

def generatorA():
    # step through generator A1 first
    for x in generatorA1():
        yield x 
    # once exhausted, step through generator A2
    for y in generatorA2():
        yield y


def main():
    for x in generatorA():
        print(x)

if __name__=="__main__":
    main()