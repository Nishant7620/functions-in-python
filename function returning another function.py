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
