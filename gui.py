# Exercise!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = "*"
empty = " "
for row in picture:
    for col in row:
        if col:
            print(fill, end="")
        else:
            print(empty, end="")
    print() # print a new line after every row is printed


# Good Coding Practices:
# clean
# readable
# predictable
# DRY - donot repeat yourself - make functions to run the same code multiple times - reuseable code
