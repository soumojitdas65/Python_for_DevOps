n = int(input())

if n%2 != 0:
    print("Weird- Odd")
else:
    if   n>=2 and n<=5:  
        print("Not Weird -Even")
    elif n>=6 and n<=20:
        print("Weird -Even")
    elif n>20:
        print("Not Weird -Even (>20)")
