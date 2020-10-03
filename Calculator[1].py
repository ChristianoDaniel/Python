def add(x,y):
    return x + y
def multiply(x,y):
    return x*y

print("This is our calculator")
print("1.add")
print("2.multiply")

choose = input("select from options (1 / 2): ")

num1 = float(input("first input"))
num2 = float(input("second input"))

if choose == '1':
    print(num1, "+", num2, "=", add(num1,num2))
elif choose == '2':
    print(num1, "*", num2, "=", multiply(num1,num2))
else:
    print("invalid input")