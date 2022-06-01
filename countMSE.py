import math

def countmse(img,originalImg,row,column):
    mse = 0
    for r in range(row):
        for c in range(column):
            #print(img[row][column])
            try:
                mse += ( (int( originalImg[r][c] ) - int( img[r][c]))**2 )
            except TypeError:
                mse += ( (int( originalImg[r][c] ) - int( img[r][c][0]))**2 )
                
    mse = mse //( row*column )
    if mse == 0:
        mse+=1
    
    return mse