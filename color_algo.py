from PIL import Image 
import numpy as np
import random  
import math
from algo_2 import algo2
import cv2
from countMSE import countmse


def crateArray(url):
    img = Image.open(url)
    imgArray = np.array(img)
    
    return imgArray

if __name__ == "__main__":
    coverImgs = []
    shareImgs = []
    
    s = "E:\\Visual Cryptograpyh\\input_image\\color_Lenna.png"
    
    cover1 = "E:\\Visual Cryptograpyh\\input_image\\sakura.png"
    cover2 = "E:\\Visual Cryptograpyh\\input_image\\color_mountain.png"
    cover3 = "E:\\Visual Cryptograpyh\\input_image\\color_tower.png"
    cover4 = "E:\\Visual Cryptograpyh\\input_image\\color_boat.png"
    cover5 = "E:\\Visual Cryptograpyh\\input_image\\color_dog.png"
    
    secret = crateArray(s)
    
    coverImgs.append( crateArray(cover1) )
    coverImgs.append( crateArray(cover2) )
    coverImgs.append( crateArray(cover3) )
    coverImgs.append( crateArray(cover4) )
    coverImgs.append( crateArray(cover5) )
    
    shareImgs.append( crateArray(cover1) ) 
    shareImgs.append( crateArray(cover2) ) 
    shareImgs.append( crateArray(cover3) ) 
    shareImgs.append( crateArray(cover4) ) 
    shareImgs.append( crateArray(cover5) ) 

    beta = 0
    count = [0,0,0,0,0,0]                
                              
    # 0.3 0.7 0.25 0.75
    for row in range(512):
        for column in range(512):
            for rgb in range(3):
                #a=random.random()
                """
                if  a <  beta  :
                    tmp = algo2( secret[row][column][rgb] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        shareImgs[number][row][column][rgb] = tmp [number]
                else:
                """ 
                
                allImgsXOR = secret[row][column][rgb]
                
                for cover in range( len(coverImgs) ):
                    #print(cover , coverImgs[cover][row][column])
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
                    count[5]+=1
                    randcover = random.choice(minCovers)
                elif len(minCovers) == 1:
                    randcover = minCovers[0]
                
                #count[randcover]+=1

                shareImgs[randcover][row][column][rgb] = allImgsXOR ^ coverImgs[randcover][row][column][rgb]

    
    psnr = []
    for cover in range(5):
        mse = 0
        for rgb in range(3):
            mse += countmse( coverImgs[cover],shareImgs[cover],512,512,rgb)

        mse = mse //3 
        ps = 10 * math.log( ( (255**2 ) /mse ),10 ) 
        psnr.append(ps)

    print(psnr)
    
    for i in range( len(shareImgs) ):
        aa = Image.fromarray( shareImgs[i] )
        aa.save(str( i ) +" algo2_0.75" +".png" ) 
        aa.show()
    
    outi = shareImgs[0]
    for row in range(512):
        for column in range(512):
            for rgb in range(3):
                for i in range (1, len(shareImgs) ) :
                    outi[row][column][rgb] = outi[row][column][rgb] ^ shareImgs[i][row][column][rgb]

    
    o = Image.fromarray(outi)
    o.save("output_algo2_0.75.png") 
    o.show()
    



    