def generatorA():
    # generator returns i first: 0 < x < 9
    for i in range(10):
        yield i
    # then generator returns j: 15 < x < 19
    for j in range(15,20):
        yield j

def main():
    for x in generatorA():
        print(x)

if __name__=="__main__":
    main()