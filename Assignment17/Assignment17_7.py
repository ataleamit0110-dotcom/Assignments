
#3 . display pattern
# 12345
# 12345
# 12345
# 12345
# 12345
def displayPatter(rows):
    for i in range(rows):
       for j in range(1, rows + 1):
           print(j, end="")
       print()

displayPatter(5) 