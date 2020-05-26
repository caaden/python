#%% define decorator
# i am passing the function i wish to decorate
def my_decorator(func):
    # returns a function that prints the name of the function passed into my decorator
    # argument func is in scope
    def function_wrapper(x):
        # x is the new argument to function wrapper
        # recall, func() is in scope
        print('Before calling ' + func.__name__)
        func(x)
        print('After calling '+ func.__name__)
    # return the function wrapper which implicitly requires that x be passed into the decorator
    return function_wrapper

#%% define base function, foo
def foo(x):
    print('Hi, foo has been called with: ' + str(x))

#%% call foo
print('We call foo before decoration:')
foo('Hi')

#%% decorate foo, and replace
print('Now, we decorate foo with f:')
foo=my_decorator(foo)

#%% call decorated foo
print('Now, we call foo after decoration:')
foo(90)

#%%
