# The special syntax *args in function definitions in python is used to pass a variable number 
# of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 
# The syntax is to use the symbol * to take in a variable number of arguments; by convention, 
# it is often used with the word args.

def adder(*args):
    sum=0
    for n in args:
        sum=sum+n
    print('sum=',sum)


def main():
    adder(1,2,3)
    adder(1,2,3,4,5)


if __name__ == "__main__":
    main()