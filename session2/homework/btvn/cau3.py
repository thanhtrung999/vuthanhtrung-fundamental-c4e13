#What is nested conditionals?
#The outer conditional contains two branches. The second branch (the else from the outer) contains another if statement, which has two branches of its own. Those two branches could contain conditional statements as well.


# Write a piece of code that uses nested conditionals

x = 10
y = 10

if x < y:
    print('x nhỏ hơn ỹ')
else:
    if x > y:
        print('x lớn hơn y')
    else:
        print('cả hai bằng nhau')