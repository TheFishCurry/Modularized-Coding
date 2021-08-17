print("\n")
print("Hello, this is a simple python calculator.")
print("\n")

print("Given two parameters, it can calculate following: ","\n"
" 1. Sum -> Use sum(a,b)", 
"\n","2. Product -> Use product(a,b)", 
"\n","3. Difference -> Use different(a,b)", 
"\n","4. Ratio -> Use ratio(a,b)" )
print("\n")
print("Given one argument, it can do following: ","\n",
"1. Tell if number is even or odd","\n",
"2. Tell if number is prime or not", "\n",
"3. Square -> Use square(a)", "\n",
"4. Square Root -> Use square_root(a)", "\n",
"5. Cube")

def sum(a, b):
    return (a+b)


def product(a, b):
    return (a*b)


def difference(a, b):
    return a-b


def ratio(a, b):
    return a/b



# FOR ONE ARGUMENT ______________________________________________________


def is_prime(a):
    if a<1:
        return "Invalid input"
    if a==1:
        return "Not Prime"
    count = 0
    for i in range(2,a):
        if a%i == 0:
            count+=1
    if count>0:
        return ("Not Prime")
    else:
        return ("Prime")
def odd_even(a):
    if a<1:
        return "Invalid input"
    if a%2==0:
        return("Even")
    else:
        return "Odd"
def square(a):
    return a*a

def square_root(a):
    return a**(0.5)

def cube(a):
    return a*a*a

# print(sum(int(input()), int(input())))
