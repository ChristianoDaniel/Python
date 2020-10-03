import re

print("Our magical calculator")
print("Type 'quit' to exit\n")
# create a variable called previuos which will hold the result of the previous result
previous = 0
# create a variable called run for the loop
run = True

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        run = False
        print("Goodbye, my friend!")
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()