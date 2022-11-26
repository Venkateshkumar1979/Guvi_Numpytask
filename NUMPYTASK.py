import numpy as np
"""Tasks:
1.  The most basic kind of broadcast is with a scalar, in which you can perform a binary
    operation (e.g., add, multiply, ...) on an array and a scalar, the effect is to perform that
    operation with the scalar for every element of the array. To try this out, create a vector
    1, 2, . . . , 10 by adding 1 to the result of the arange function.

2.  Now, create a 10 × 10 matrix A in which A[i][j] = i + j. """
a=np.zeros((10,10))
for i in range(10):
    for j in range(10):
        a[i][j]=a[i][j]+i+j
print("\n---------10 × 10 matrix A in which A[i][j] = i + j---------\n")
print(a+2)
import numpy.random as npr
data = np.exp(npr.randn(50, 5))
print("\n---------50 x 5 Random Numbers---------\n")
print(data)

print("\n---------Mean - Column wise---------\n")
mean=np.mean(data,axis=0)
std=np.std(data,axis=0)
print (mean)
print("\n---------Standard Deviation - Column wise---------\n")
print (std)
mean_sub=data-mean
print("\n---------Matrix After Subtracting Mean Off of Each Coulmn---------\n")
print(mean_sub)
normalized=mean_sub / std
print("\n---------Matrix After Dividing STD Off of Each Coulmn---------\n")
print(normalized)
normalized_mean=np.mean(normalized,axis=0)
normalized_std=np.std(normalized,axis=0)
print("\n---------Mean After Normalization---------\n")

print(normalized_mean)
print("\n---------STD After Normalization---------\n")
print(normalized_std)