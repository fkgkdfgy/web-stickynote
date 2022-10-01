
name_dict={}
def add_into_dict(f):
    def inner(x,y):
        return f(5+x,5+y)
    name_dict[f.__name__] = f
    return inner

@add_into_dict
def calculate(x,y):
    return x+y

print(name_dict)
print(calculate(10,10))
