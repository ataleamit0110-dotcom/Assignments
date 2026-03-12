actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

TP = TN = FP = FN = 0

for a, p in zip(actual, predicted):
    if a == 1 and p == 1:
        TP += 1
    elif a == 0 and p == 0:
        TN += 1
    elif a == 0 and p == 1:
        FP += 1
    elif a == 1 and p == 0:
        FN += 1

print("TP:", TP)# 3
print("TN:", TN)# 3
print("FP:", FP)#1
print("FN:", FN)#1


# Other way
# cm = confusion_matrix(actual, predicted)
# TN, FP, FN, TP = cm.ravel()
