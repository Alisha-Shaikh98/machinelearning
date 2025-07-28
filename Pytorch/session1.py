import torch as t

#Scalars, vector & matrices
a = t.tensor(2.0)
b = t.tensor([1.0, 2.0])
c = t.tensor ([[1,2], [3, 4]])

#Random values and zeros
rand = t.rand(3, 3)
zeros = t.zeros(2, 3)
ones = t.ones(3, 1)

print (f'''
A : {a}
B : {b}
C : {c}

Random Matrix: 
        {rand}

Zero Matrix: 
        {zeros}

One Matrix:
        {ones}
''')

#GPU Support test of pytorch
print(t.cuda.is_available())
print(t.backends.mps.is_available())
print(t.device('cpu'))