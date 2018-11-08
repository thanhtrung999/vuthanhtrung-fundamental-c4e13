content = '''
noi dung
'''

with open("content.txt", "r") as f:
   c = f.read()
   print(c)
#1: open file
# f = open("content.txt", "w") #write

# #2: Write file
# f.write(content)

# #3: Close file
# f.close()