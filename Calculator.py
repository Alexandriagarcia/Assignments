#Basic Calculator of Ma. Alexandria P. Garcia

ban = True
while ban:
    try:
        first = float(input("Fisrt no.:"))
    except ValueError:
            print("Not a number...")
    else:
            ban = False
print ("Valid")

ban = True
while ban:
    try:
        second = float(input("Second no.:"))
    except ValueError:
            print("Not a number...")
    else:
            ban = False
print ("Valid")

ban = True

while ban:
    op = input ("Operation you want to use? +, -, *, /:")
    if op == "+":
        ban = False
        sum = float(first) + float(second)
    elif op == "-":
        ban = False
        sum = float(first) - float(second)
    elif op == "*":
        ban = False
        sum = float(first) * float(second)
    elif op == "/":
        ban = False
        sum = float(first) / float(second)
    else:
        print("Invalid Operation")

print("The Answer is:", sum)


