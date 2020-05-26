def adder(**kwargs):
    args=kwargs["ints"]
    sum=0
    for n in args:
        sum=sum+n
    print('sum=',sum)


def main():
    adder(ints=[1,2,3])
    adder(ints=[1,2,3,4,5])


if __name__ == "__main__":
    main()