# LEGB
# local, enclosing, global, built-in

# enclosing
# def outer():
#     x = "outter x"
#     def inner():
#         y = "inner x"
#         print(y)
#     inner()
#     print(x)

# outer()

x = "global x"
def outer():
    x = "outer x"     # enclosing scope/ enclosing variable for inner x()
    def inner():
        nonlocal x      # nonlocal x → refers to the nearest enclosing scope variable, which is outer’s x.
        x = "inner x"   # local scope/ # modifies outer's x
        print(x)        # inner x
    inner()
    print(x)    # inner x

outer()

x = "global x"       # global scope

def outer():
    x = "outer x"    # enclosing (outer) scope for inner()
    
    def inner():
        nonlocal x
        x = "inner x"   # changes outer's x
        print(x)        # prints "inner x"
    
    inner()
    print(x)            # prints outer's x (which was changed by inner())
    
outer()
