import numpy as np
# value for test
matrix1=np.array([[1]])
matrix2=np.array([[1,2],[3,4]])
matrix3=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix4=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
matrix5=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])

def matrix_subset(matrix,colomn):
    subs=[]
    for i in range(matrix.shape[0]):
        if i != colomn:
            subs.append(list(matrix[1:,i]))
    return np.array(subs).T

def sum_det(list):
    T=0;P=2
    for item in list:
        T=T+(item*(-1)**P)
        P+=1
    return T

def det(matrix):
    list_objects=[]
    if matrix.shape[0]>2:
        for i in range(matrix.shape[0]):
            matrix_sub=matrix_subset(matrix,i)
            matrix22=matrix_sub
            list_objects.append(matrix[0,i]*det(matrix22))
        return sum_det(list_objects)
    elif matrix.shape[0]==2:
        for i in range(matrix.shape[0]):
            matrix_sub=matrix_subset(matrix,i)
            list_objects.append(matrix[0,i]*matrix_sub)
        return sum_det(list_objects)[0,0]
    elif matrix.shape[0]==1:return matrix[0,0]

# determinan matrix 3*3
print(det(matrix3))