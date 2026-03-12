import numpy as np
from sklearn.preprocessing import StandardScaler
from math import sqrt

data = np.array([
    [25,20000],
    [30,40000],
    [35,80000]
])

# Points
A = data[0]
B = data[1]

print("A is ", A)
# -------- BEFORE SCALING --------
dist_before = sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

print("Distance before scaling:", dist_before)


# -------- SCALING --------
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

A_scaled = scaled_data[0]
B_scaled = scaled_data[1]

# -------- AFTER SCALING --------
dist_after = sqrt((A_scaled[0]-B_scaled[0])**2 + (A_scaled[1]-B_scaled[1])**2)

print("Distance after scaling:", dist_after)