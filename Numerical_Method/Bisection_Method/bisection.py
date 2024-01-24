def solve_f(f:list,x:int):
    value=0
    for i in range(0,len(f),2):
        value+= f[i]*(x**f[i+1])
    return (value)

def bisection(f:list,a:int,b:int,ephsilon:int):
    while(True):
        c=(a+b)/2
        if b-c < ephsilon:
            return c
            break
        
        elif solve_f(f,c) <= 0 :
            a=c
        else:
            b=c

def find_limit(f:list):
    if solve_f(f,0) < 0: 
        for i in range(100):
            if solve_f(f,i) < 0 and solve_f(f,i+1)>=0 :
                return i,i+1
            
    else:
        for i in range(0,-100,1):
            if solve_f(f,i) >= 0 and solve_f(f,i-1) < 0 :
                return i+1,i


def main():
    f = []
    n = int(input("Enter how many variables in the function: "))

    for i in range(0, n*2, 2):
        power = int(input("Enter the power of x: "))
        constant = int(input(f"Enter the constant of power {power}: "))
        f.append(constant)
        f.append(power)

    a,b=find_limit(f)
    root=bisection(f,a,b,ephsilon=0.00005)
    print(f"root of the given equation is : {root}")

if __name__== "__main__":
    main()
