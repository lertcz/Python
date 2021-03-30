from Matrix import Matrix

test = [[4, 3], [-2, 1]]

mat = Matrix(2, 2)

print("setting values...\n")
mat.setItem(0, 0, 1)
mat.setItem(0, 1, 2)
mat.setItem(1, 0, 3)
mat.setItem(1, 1, 4)

print("matrix:")
mat.printMatix()

print("get item on [1,1]:")
print(mat.getItem(1,1))

print("\nadd:")
mat.printMatix()
print("+")
for element in test:
    print(element)
print("=")
mat.add(test)
mat.printMatix()

print("\nsub:")
mat.printMatix()
print("+")
for element in test:
    print(element)
print("=")
mat.sub(test)
mat.printMatix()

print("\nmultiply by constant:")
mat.printMatix()
print("*\n5\n=")
mat.multiply(5)
mat.printMatix()

print("\nmultiply 2 matrices:")
mat.printMatix()
print("*")
for element in test:
    print(element)
print("=")
mat.multiply(test)
mat.printMatix()

print("\ntranspose:")
mat.transpose()
mat.printMatix()