#Conditional Statements
x = int(input("Enter no 1 :"))
y = int(input("Enter no 2 :"))
z = int(input("Enter no 3 :"))

#find the largest amongst 3 nos
if x>y and x>z:
    print(f"{x} is largest")
elif y>z:
    print(f"{y} is largest")
else:
    print(f"{z} is largest")
        
