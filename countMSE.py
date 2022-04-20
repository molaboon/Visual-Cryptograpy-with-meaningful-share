import math

def countmse(img,originalImg,row,column,rgb):
    mse = 0
    for row in range(column):
        for column in range(row):
            mse += ( (int( originalImg[row][column][rgb] ) - int( img[row][column][rgb]))**2 )

    mse = mse //( row*column )
    if mse == 0:
        mse+=1
    
    return mse