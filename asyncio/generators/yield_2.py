from itertools import cycle

def endless():
    # yield marks a breakpoint in the generator
    # control ceded but subroutine is not closed and state remains
    yield from cycle((9,8,7,6))

def main():
    e=endless()
    total =0
    for i in e:
        if total<30:
            print(i,end='')
            total+=1
        else:
            print()
            break
    
    #look at next iteration:
    # next(genrator) steps to next iteration
    print(next(e),' ',next(e),' ',next(e))

if __name__=="__main__":
    main()