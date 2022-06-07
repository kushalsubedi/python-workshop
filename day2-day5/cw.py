# create function to accept number from user 
        # -> return teh number
# create another function to check wether the number from user is odd or even 
       # -> return True if even return False if odd

def ask_num():
    num = int(input("Enter any number :"))
    return num

def check(n):
    if n%2==0:
        return True
    else :
        return False
  
x=ask_num()
y=check(x)
print(y)