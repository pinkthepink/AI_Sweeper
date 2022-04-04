import random as rd
import numpy as np

nMinas = 10
 
mineField = np.zeros((9,9))

print(mineField)
i=0
while i < nMinas :
    x = int(rd.random()*9)
    y = int(rd.random()*9)
    if(mineField[x][y] == 0):
        mineField[x][y] = -1
        i+=1

print(mineField)



for i in range(8):
    for j in range(8):
        if mineField[i][j] == -1:
            if mineField[i-1][j-1] != -1:
                mineField[i-1][j-1] +=1
            if mineField[i][j-1] != -1:
                mineField[i][j-1] +=1
            if mineField[i+1][j-1] != -1:
                mineField[i+1][j-1] +=1
            if mineField[i-1][j] != -1:
                mineField[i-1][j] +=1
            if mineField[i+1][j] != -1:
                mineField[i+1][j] +=1
            if mineField[i-1][j+1] != -1:
                mineField[i-1][j+1] +=1
            if mineField[i][j+1] != -1:
                mineField[i][j+1] +=1
            if mineField[i+1][j+1] != -1:
                mineField[i+1][j+1] +=1

print(mineField)

np.savetxt("field.csv",mineField,delimiter=",")