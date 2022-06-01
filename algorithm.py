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
"""
    對五張圖片的每個bit 去做演算法2:
    "0" "1" "0" "1" "0" "1" "0" "1" "0"

    如何選圖片?
    若如果要翻最左邊的數值(1)
    則去尋找最接近128的圖片去做翻轉

    如果要翻左邊數過來第二個數字,
    則去選擇最接近64 or 128+64的圖片去做翻轉

    如果這些演算法不適用,那就在去找。
"""

if __name__ == "__main__":
    coverImgs = []
    shareImgs = []
    
    s = "E:\\Visual Cryptograpyh\\input_image\\gray_lenna.png"
    
    cover3 = "E:\\Visual Cryptograpyh\\input_image\\gray_barbara.png"
    cover2 = "E:\\Visual Cryptograpyh\\input_image\\gray_owl.png"
    cover1 = "E:\\Visual Cryptograpyh\\input_image\\gray_baboon.png"
    cover4 = "E:\\Visual Cryptograpyh\\input_image\\gray_bird.png"
    cover5 = "E:\\Visual Cryptograpyh\\input_image\\gray_butterfly.png"
    
    secret = crateArray(s)
    
    col = 512

    OriArray1 = np.zeros((col, col),int)
    OriArray2 = np.zeros((col, col),int)
    OriArray3 = np.zeros((col, col),int)
    OriArray4 = np.zeros((col, col),int)
    OriArray5 = np.zeros((col, col),int)

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

    beta = 0.5
    count = [0,0,0,0,0,0]                
                
    # 0.3 0.7 0.25 0.75
    for row in range(512):
        for column in range(512):
            a=random.random()
            if  a <  beta  :
                tmp = algo2( secret[row][column] , coverImgs , row, column)
                for number in range ( len( coverImgs ) ):
                    shareImgs[number][row][column] = tmp [number]
            else:
                allImgsXOR = secret[row][column]

                for cover in range( len(coverImgs) ):
                    try :
                        allImgsXOR = allImgsXOR ^ coverImgs[cover][row][column][0]
                    except :   
                        allImgsXOR = allImgsXOR ^ coverImgs[cover][row][column]

                randcover = random.randint(0,4)
                min = 999
                minCovers = []
                for cover in range( len(coverImgs) ):
                    try:
                        tmpMin = abs( ( int( coverImgs[cover][row][column][0] ) - int( allImgsXOR ^ coverImgs[cover][row][column][0] )))
                    except: 
                        tmpMin = abs( ( int( coverImgs[cover][row][column] ) - int( allImgsXOR ^ coverImgs[cover][row][column] )))
                        
                    if tmpMin < min:
                        minCovers.clear()
                        min = tmpMin 
                        minCovers.append(cover)
                    elif tmpMin == min: 
                        minCovers.append(cover)

                if len(minCovers) > 1 :
                    #count[5]+=1
                    randcover = random.choice(minCovers)
                elif len(minCovers) == 1:
                    randcover = minCovers[0]
                
                # count[randcover]+=1
                
                #allImgsXOR = secret[row][column] ^ allImgsXOR
               
                for cover in range(len(coverImgs)):
                    if cover != randcover:
                        try :
                            shareImgs[cover][row][column] = coverImgs[cover][row][column][0]
                        except:
                            shareImgs[cover][row][column] = coverImgs[cover][row][column]
                    else:
                        try :
                            shareImgs[randcover][row][column] = allImgsXOR ^ coverImgs[randcover][row][column][0]
                        except:
                            shareImgs[randcover][row][column] = allImgsXOR ^ coverImgs[randcover][row][column]
                    
    psnr = []
    for cover in range(5):
        mse = countmse( coverImgs[cover],shareImgs[cover],512,512)
        
        ps = 10 * math.log( ( (255**2 ) /mse ),10 ) 
        psnr.append(ps)

    print(psnr)
  
    outi = 0
    for i in range( len(shareImgs) ):
        aa = Image.fromarray( shareImgs[i].astype(np.uint8) )
        aa.save(str( i ) +" algo2" +".png" ) 
        aa.show()

    for i in range ( len(shareImgs) ) :
        outi = outi ^ shareImgs[i]

    
    o = Image.fromarray(outi.astype(np.uint8))
    o.save("output_algo2_0.75.png") 
    o.show()
    




    