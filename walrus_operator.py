# The walrus operator ':=' assigns values to varialbles as part of a large expression
a = 'heloooooooo'
if ((n := len(a)) > 10): # wrap the walrus operator assignment in parantheses to evaluate it first 
    # (store 'n' first) and then evaluate condition
    print(f"too long {n} elements")

print()
print()

while ((k := len(a)) > 1):
    print("length of a: ", k)
    a = a[:-1]