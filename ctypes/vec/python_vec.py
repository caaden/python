from ctypes import *

class Vector(object):
    lib = cdll.LoadLibrary('./vector_python.so')
    
    lib.new_vector.restype = c_void_p
    lib.new_vector.argtypes = []
    
    lib.delete_vector.restype = None
    lib.delete_vector.argtypes = [c_void_p]
    
    lib.vector_size.restype = c_int
    lib.vector_size.argtypes = [c_void_p]
    
    lib.vector_get.restype = c_int
    lib.vector_get.argtypes = [c_void_p, c_int]
    
    lib.vector_pushback.restype = None
    lib.vector_pushback.argtypes = [c_void_p, c_int]
    

    def __init__(self):
        self.obj = Vector.lib.new_vector()  # pointer to new vector

    def __del__(self):  # when reference count hits 0 in Python,
        Vector.lib.delete_vector(self.obj)  # call C++ vector destructor

    def __len__(self):
        return Vector.lib.vector_size(self.obj)

    def __getitem__(self, i):  # access elements in vector at index
        if 0 <= i < len(self):
            return Vector.lib.vector_get(self.obj, c_int(i))
        raise IndexError('Vector index out of range')

    def __repr__(self):
        return '[{}]'.format(', '.join(str(self[i]) for i in range(len(self))))

    def push(self, i):  # push calls vector's push_back
        Vector.lib.vector_pushback(self.obj, c_int(i))

    def foo(self, filename):  # foo in Python calls foo in C++
        Vector.lib.foo(self.obj, c_char_p(filename))

if __name__ == "__main__":
    a=Vector()
    a.push(22)
    a.push(28)
    a.push(16)
    print(a)
    print('length a:',a.__len__())
    print('a[0]=',a.__getitem__(0))
    del a

