
#3 . display pattern
# 1
# 12
# 123
# 1234
# 1234
def displayPattern(rows):
    for i in range(1, rows + 1):
       for j in range(1, i + 1):
           print(j, end="")
       print()

displayPattern(5)