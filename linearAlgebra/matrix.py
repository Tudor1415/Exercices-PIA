import numpy as np

class Matrix:
    def __init__(self, *elements, shape=(1,1)):
        self.shape = shape
        self.elements = self.get_elements(elements)
 
    def get_elements(self, elements):
        return [[ elements[j+i] for j in range(self.shape[0])] for i in range(self.shape[1])]

    def __str__(self):
        str = ""
        for i in self.elements:
            str += f"{i} \n"
        return str
        
    def dot(self, M2):
        if M1.shape[1] == M2.shape[0]:
            return [[sum(a*b for a,b in zip(M1_row,M2_col)) for M2_col in zip(*M2.elements)] for M1_row in self.elements]
        else:
            return "Error shapes don't match!"
    
    def print(self, content):
        for i in content:
            print(i)

M1 = Matrix(1,2,3,4, shape=(1,4))
M2 = Matrix(*list(range(16)), shape=(4,4))
print(M2)
print(M1)

print(M1.print(M1.dot(M2)))