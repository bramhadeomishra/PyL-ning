class Fibonacci:
    def rangeFibo(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return (Fibonacci.rangeFibo(self,n-1)+Fibonacci.rangeFibo(self,n-2))



class Prime:
    def isPrime(self,n): # Checks if number is prime
        number=n        
        flag=0
        #code to exclude 1 nd 2 from check
        if number==1:
            return False
        elif number==2:
            return True
            
        for i in range(2,(number/2)+1):
            if (number)%i==0:
                flag=1
                break
            else:
                flag-0
                continue 
                                               
        if flag==0:
            return True
        elif flag==1:
            return False
                    
    def rangePrime(self,n): # List prime number between 1 to number
        number=n 
        l=[]       
        for i in range(2,number):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                l.append(i)
        return l
    
    def factors(self,n): # Lists all factors of number
        l =[]
        for i in range(1,n):
            if n%i==0:
                l.append(i)
        return l
    
    def largestPrime(self,n): # largest prime
        f=Prime.factors(self,n)
        for i in reversed(f):
            if Prime.isPrime(self,i):
                return i
            else:
                continue              

    def primeFactors(self,n): # list all the prime factor of a number
        f=Prime.factors(self, n)
        for i in f:
            if Prime.isPrime(self, i):
                continue
            else:
                f.remove(i)
                                
        return f

def main(): # driver function to call functions from class Prime
    p=Prime()    
    n=input('Please enter a number :')
    print n,'is a Prime Number: ' , p.isPrime(n)
    print 'Prime numbers between 1 and ',n,':',p.rangePrime(n)
    print 'Factors of',n,'are :', p.factors(n)
    print 'List of prime factors: ', p.primeFactors(n)
    print 'Largest prime factor: ',p.largestPrime(n)

#main()