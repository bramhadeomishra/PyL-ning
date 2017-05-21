class Greetings:              
    def Greet(self,lang):                
        if lang=="english":
            print "Hello Bramha!"
        elif lang=="hindi":
            print "Namaskar Bramha!"
        elif lang=="marathi":
            print "Helo Bramha!"
        elif lang=="bengoli":
            print "Nomoskar Bramha!"
        elif lang=="marwari":
            print "Khamma Ghani Bramha!"
        else:
            print "I don't understand your language!"            
                      
def main():
    g=Greetings()
    g.Greet("aa")   
main()    
#if __name__ == "__main__":
#    main()