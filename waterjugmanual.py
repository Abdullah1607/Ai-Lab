import math

#Input capacities and initial/final states for jugs
a = int(input("Enter Jug A capacity: "))
b = int(input("Enter Jug B capacity: "))
ai = int(input("initially Water in Jug A: "))
bi = int(input("initially Water in Jug B: "))
af = int(input("Final State of jug A: "))
bf = int(input("Final State of jug B: "))

if a <= 0 or b <= 0:
    print("jug capacities must be positive.")
    exit(1)
if ai < 0 or bi < 0 or af < 0 or bf < 0:
    print("Negative values are not allowed.")
    exit(1)

def wjug(a, b, ai, bi, af, bf):
    print("list of operations you can do:\n")
    print("1. Fill Jug A completely")
    print("2. Fill Jug B completely")
    print("3. Empty Jug A completely")
    print("4. Empty Jug B completely")
    print("5. Pour from jug A till jug B is Full or A becomes empty")
    print("6. Pour from jug B till Jug A is Full or B becomes empty")
    print("7. Pour all from jug B to Jug A")
    print("8. Pour all from jub A to jug B")

    while ai != af or bi != bf:
        op = int(input("Enter the operation (1-8): "))

        if op == 1:
            ai = a
        elif op == 2:
            bi = b
        elif op == 3:
            ai = 0
        elif op == 4:
            bi = 0
        elif op == 5:
            pour_amount = min(ai,b-bi)
            ai -= pour_amount
            bi += pour_amount
        elif op == 6:
            pour_amount = min(bi, a-ai)
            bi -= pour_amount
            ai += pour_amount
        elif op == 7:
            pour_amount = min(bi, a-ai)
            ai += pour_amount
            bi -= pour_amount
        elif op == 8:
            pour_amount = min(ai, b-bi)
            bi += pour_amount
            ai -= pour_amount
        else:
            print("Invalid Operation please shoose a number between 1 and 8")
            continue
        print(f"Jug A:{ai}, Jug B{bi}")
        
        if ai==af and bi==bf:
            print("final state Reached: Jug A =", ai, ", Jug B =", bi)
            return
        print("final state Reached: Jug A =", ai, ", Jug B =", bi)

gcd = math.gcd(a, b)

if (af <= a and bf <= b) and (af % gcd == bf % gcd == 0):
    wjug(a, b, ai, bi, af, bf)
else:
    print("the final state is not achievable with the given capacities,")
    exit(1)
