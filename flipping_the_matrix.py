def flippingMatrix(matrix):
    # Write your code here
    nmayor = 0
    nmenor = list()
    for i in range(len(matrix)):
        nmayor += max(matrix[i])
        nmenor.append(min(matrix[i]))
    res = nmayor - max(nmenor) + min(nmenor) + int(len(nmenor)/2)
    print(res)

mat = [[107, 54, 128, 15],[12, 75, 110, 138],[100, 96, 34, 85],[75, 15, 28, 112]]
flippingMatrix(mat)