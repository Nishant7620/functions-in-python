def diplay(sh):
    def info():
        print("this is information")
    print("this is display function")
    return info()    
        

def show():
    print("this is show function")

diplay(show())    

