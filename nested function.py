def outer():
    def inner():
        print("outer function")
    print("inner function")
    inner()
outer()            