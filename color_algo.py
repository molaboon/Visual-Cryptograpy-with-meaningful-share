from PIL import Image 
import numpy as np
import random  
import math
from algo_2 import algo2
import cv2
from countColorMse import countmse


def crateArray(url):
    img = Image.open(url)
    imgArray = np.array(img)
    
    #imgArray = cv2.imread(url)
    return imgArray

if __name__ == "__main__":
    coverImgs = []
    shareImgs = []
    
    s = "E:\\Visual Cryptograpyh\\input_image\\color_Lenna.png"
    
    cover1 = "E:\\Visual Cryptograpyh\\input_image\\color_tiger.png"
    cover2 = "E:\\Visual Cryptograpyh\\input_image\\color_bird.png"
    cover3 = "E:\\Visual Cryptograpyh\\input_image\\color_owl.png"
    cover4 = "E:\\Visual Cryptograpyh\\input_image\\color_butterfly.png"
    cover5 = "E:\\Visual Cryptograpyh\\input_image\\color_fox.png"
    
    secret = crateArray(s)
    
    col = 512
    three= 3

    OriArray1 = np.zeros((col, col, three),np.int8)
    OriArray2 = np.zeros((col, col, three),np.int8)
    OriArray3 = np.zeros((col, col, three),np.int8)
    OriArray4 = np.zeros((col, col, three),np.int8)
    OriArray5 = np.zeros((col, col, three),np.int8)
    OriArray6 = np.zeros((col, col, three),np.int8)

    coverImgs.append( crateArray(cover1) )
    coverImgs.append( crateArray(cover2) )
    coverImgs.append( crateArray(cover3) )
    coverImgs.append( crateArray(cover4) )
    coverImgs.append( crateArray(cover5) )
    
    shareImgs.append( OriArray1 ) 
    shareImgs.append( OriArray2 ) 
    shareImgs.append( OriArray3 ) 
    shareImgs.append( OriArray4 ) 
    shareImgs.append( OriArray5 ) 

    print(len(shareImgs))
    
    # shareImgs.append( crateArray(cover1) ) 
    # shareImgs.append( crateArray(cover2) ) 
    # shareImgs.append( crateArray(cover3) ) 
    # shareImgs.append( crateArray(cover4) ) 
    # shareImgs.append( crateArray(cover5) )    
    
    beta = 0.25
    #count = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]                
                              
    # 0.3 0.7 0.25 0.75
    for row in range(512):
        for column in range(512):
            for rgb in range(3):
                a=random.random()
                if  a <  beta  :
                    tmp = algo2( secret[row][column][rgb] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        shareImgs[number][row][column][rgb] = tmp [number]
                else:
                    
                    allImgsXOR = secret[row][column][rgb]
                    
                    for cover in range( len(coverImgs) ):
                        allImgsXOR = allImgsXOR ^ int( coverImgs[cover][row][column][rgb] )    
                    
                    randcover = random.randint(0,len(coverImgs)-1)
                    min = 999
                    minCovers = []
                    for cover in range( len(coverImgs) ):
                        tmpMin = abs( ( int( coverImgs[cover][row][column][rgb] ) - int( allImgsXOR ^ coverImgs[cover][row][column][rgb] )))
                        if tmpMin < min:
                            minCovers.clear()
                            min = tmpMin 
                            minCovers.append(cover)
                        elif tmpMin == min: 
                            minCovers.append(cover)

                    if len(minCovers) > 1 :
                        randcover = random.choice(minCovers)
                    elif len(minCovers) == 1:
                        randcover = minCovers[0]
                    
                    for cover in range(len(coverImgs)):
                        if cover != randcover:
                            shareImgs[cover][row][column][rgb] = coverImgs[cover][row][column][rgb]
                        else:
                            shareImgs[randcover][row][column][rgb] = int(allImgsXOR) ^ int( coverImgs[randcover][row][column][rgb]) 
    psnr = []
    for cover in range(len(coverImgs)):
        mse = 0
        for rgb in range(3):
            mse += countmse( coverImgs[cover],shareImgs[cover],512,512,rgb)
        
        mse = mse //3 
        ps = 10 * math.log( ( (255**2 ) /mse ),10 ) 
        
        psnr.append(ps)

    print(psnr)
    
    for i in range( len(shareImgs) ):
        aa = Image.fromarray( shareImgs[i].astype(np.uint8))
        aa.save(str( i ) +" algo2_0.75" +".png" ) 
        aa.show()
    
    outi = OriArray6

    for row in range(512):
        for column in range(512):
            for rgb in range(3):
                for i in range (len(shareImgs)) :
                    outi[row][column][rgb] = outi[row][column][rgb] ^ shareImgs[i][row][column][rgb]

    
    o = Image.fromarray(outi.astype(np.uint8))
    o.save("output_algo2_0.75.png") 
    o.show()
    



    