import numpy as np
import math
data = np.array([6,7,8,9,10,11,12])
mean = np.mean(data)
print("mean is : ", mean)

numeratorSum = 0
for i in range(len(data)):
    print(data[i])
    numeratorSum = numeratorSum + (data[i]-mean)**2

print(numeratorSum)
variance = numeratorSum/len(data)
print("Variance is : ", variance)
SD = math.sqrt(variance)
print("Standard Deviation:", SD)
    