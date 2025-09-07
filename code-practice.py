# to find the factorial of any number 

n= int(input("Enter a number : "))

product=1
for i in range (1,n+1):
    product=product*i 
    i=i+1

print(f"The factorial of {n} is {product}")

# code to print the table of n number in reversed order 

n=int(input("Enter a number :" ))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
 
#factorial of any number by method of recursion 

def factorial(n):
    if (n==1 or n==0):
        return 1
    return(n * factorial(n-1))

n=int(input("Enter a number :"))
print(f"The factorial of {n} is : {factorial(n)}")




