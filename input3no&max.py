a = int(input("Enter number A: "))
b= int(input("Enter number B: "))
c = int(input("Enter number C: "))
if a <= b and a <= c:
    print("Minimum is:", a)
elif b <= a and b <= c:
    print("Minimum is:", b)
else:
    print("Minimum is:", c)

