# swap your inputs

a = input("a: ")
b = input("b: ")

a,b = b,a

print("a: " + a)
print("b" + b)


# another method

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)


