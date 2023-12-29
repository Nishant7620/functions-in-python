def diplay(sh):
    def info():
        print("this is information")
    print("this is display function")
    return info()    
        

def show():
    print("this is show function")

diplay(show()) 

#---------------------------------------------------------------------------------

def create_machine(mach):
    def machine():
        print("this is machine")
    print("machine is created")    
    return machine()

def manufacture():
    print("machine manufacture")
x = create_machine(manufacture())

#--------------------------------------------------------------------------------------

def create_machine(mach):
    print("This is create machine function")
    return mach

def machine():
    print("this is machine function")

design = create_machine(machine)

#--------------------------------------------------------------------------------------------

def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

y = create_multiplier(2)(5)
print(y)

