def star(func):
    def inner(*args,**kwargs):
        print('*'*30)
        func(*args,**kwargs)
        print('*'*30)
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print('%'*30)
        func(*args,**kwargs)
        print('%'*30)
    return inner

#decorator function passes a function to be decorated
def smart_divide(func):
    #inner has same vars as ftbd
    def inner(a,b):
        print('I am going to divide ',a,' and ',b)
        if b==0:
            print("Can't divide by zero.")
            return
        return func(a,b)
    return inner

@star
@percent
@smart_divide
def divide(a,b):
    div=a/b
    print('a/b=',div)
    return div

def main():
    divide(2,5)
    divide(2,0)
    # will throw an error, too many input vars
    # divide(2,5,4)

if __name__ == "__main__":
    main()