matrixA=[]
matrixB=[]
matrixC=[]
rowA=int(input("How many rows does matrix A have: "))
columnA=int(input("How many columns does matrix A have: "))
rowB=int(input("How many rows does matrix B  have: "))
columnB=int(input("How many columns does matrix B have: "))
# Check if the dimensions are compatible for matrix multiplication
if columnA == rowB:
    for num_of_rows in range(rowA):
        matrixA.append([])
        matrixC.append([])
    for num_of_rows in range(rowB):
        matrixB.append([])
    print("\nEnter the elements of the first matrix")
    for i in range(rowA):
        for j in range(columnA):
            elements=int(input(f"Enter element ({i+1},{j+1}) matrixA: "))
            matrixA[i].append(elements)
    print("\nEnter the elements of the second matrix")
    for i in range(rowB):
        for j in range(columnB):
            elements=int(input(f"Enter element ({i+1},{j+1}) matrixB: "))
            matrixB[i].append(elements)
    for i in range(rowA):
            for j in range(columnB):
                element = 0
                for k in range(rowB):
                    element += matrixA[i][k] * matrixB[k][j]
                matrixC[i].append(element)
    print("The matrix product is given by: ")
    for i in range(len(matrixC)):
        for x in matrixC:
            print(x[i], end =' ')
        print()
    
else:
    print("Error: The dimensions of the matrices are not compatible for matrix multiplication.")