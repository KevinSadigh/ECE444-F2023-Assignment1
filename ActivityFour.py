#Creating class called utils which implements a function that reverses and integer 
#as well as a function that takes and int number and returns the number 
# in base two and octal format 

class utils:
    def reversed(self, num):
        #using string slicing reverse the number then convert it back to an int
        return int(str(num)[::-1])
    
    def formatter(self,num):
        #using built in functions to convert the number
        return bin(num), oct(num)
    


