import numpy as np

# a = np.array([1,2,3,4.0+0j, "True" , {1,2,3}])

# print(a.dtype)

# int - float - complex - str - object
l1 = [1,2,3,4]
l2 = [1,2,3,4]
print(l1+l2)
print(l1*3)


a = np.array([[1,2,3],[1,2,3],[1,2,3]])
b = np.array([[2,3,4],[4,5,6],[6,7,8.0]])

print(a)
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(b.dtype)