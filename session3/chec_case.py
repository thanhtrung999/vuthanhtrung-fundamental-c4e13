s = input('enter text:')
if (not s.islower()) and (not s.isupper()):
    print("Contain both lowercase and uppercase")
else:
    print('not ok')