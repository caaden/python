#%% Basic Class
class MyClass:
    pass
#%% Create new object of MyClass
c=MyClass()
# %% Print all inherited methods and attributes
print(dir(c))
# %% Create new object class
# Note, all python classes implicitly derive from the object
o=object()
dir(o)
# %% Exceptions are unique and must derive from BaseException 
class MyError(Exception):
    pass
raise MyError()
# %%
