class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name
    def __str__(self):
        return (self.Name)
    def work(self):
        raise(Exception("I’m just an intern, I can’t do that..."))
    def make_coffee(self):
        return(self.Coffee())
    class Coffee:
        def __str__(self):
            return("This is the worst coffee you ever tasted.")

        
        

def main():
    try:
        Mark = Intern("Mark")
        Nobody = Intern()
        print(Mark)
        print(Nobody)
        print(Mark.make_coffee())
        Nobody.work()
    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()