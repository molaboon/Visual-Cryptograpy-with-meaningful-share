from PIL import Image 
import numpy as np
import random  
import os

class initial:
    def __init__(self,imgURL) :
        self.img = imgURL
        #self.parameter = parameter
    def crateArray(self):
        img = Image.open(self.img)
        imgArray = np.array(img)
        
        return imgArray

class algo:
    def __init__(self,  Secret , Covers ):
        self.Secret = Secret
        self.covers = Covers 

        
    def algo2(self,sPixel,Covers,row,column):
        output = []
        output = []

        r = random.randint( 0,255 ) 
        """
        for cover in range( len (Covers) ):
            share[cover][row][column] = Covers[cover][row][column] ^ r
            output.append(share[cover][row][column])
            
        
        """

        ri = random.randint(0, len(Covers)-1 )
        tmpXOR = sPixel

        for cover in range( len(Covers) ):
            if cover == ri:
                pass
            else:
                tmpXOR = tmpXOR ^  Covers[cover][row][column]

        #share[ri][row][column] = tmpXOR 

        for cover in range( len (Covers) ):
            if cover == ri:
                output.append(tmpXOR)
            else:
                cXORrandint = Covers[cover][row][column] ^ r
                output.append(cXORrandint)


        return output

class algo3:
    def __init__(self,coverImgs):
        self.coverIms = coverImgs 
    

    # 全不動 
    def method1(self):

        for row in range(512):
            for column in range(512):
                a =random.random()

                if  a <  beta  :
                    tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        
                        shareImgs[number][row][column] = tmp [number]

                
    #轉黑
    def method3(self):
        
        for row in range(512):
            for column in range(512):
                a =random.random()

                if  a <=  beta  :
                    tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        
                        shareImgs[number][row][column] = tmp [number]

                else: 
                    randcover = random.randint(0,4)
                    tmpXOR = 0
                    for cover in range( len(coverImgs) ):
                        if cover == randcover:
                            pass
                        else:
                            tmpXOR = tmpXOR ^  coverImgs[cover][row][column]
                            
                    shareImgs[randcover][row][column] = tmpXOR
    
    def method2(self):
        for row in range(512):
            for column in range(512):
                a =random.random()

                if  a <  beta  :
                    tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        
                        shareImgs[number][row][column] = tmp [number]

                else:
                    tmpXOR = 0
                    similarCover = 0
                    min = 999
                    def hammingDistance(x, y):
                        a=x^y
                        num = 0
                        while a != 0:
                            num += a & 1
                            a >>= 1
                        return num

                    for cover in range( len(coverImgs) ):
                        tmpXOR = tmpXOR ^  coverImgs[cover][row][column]
            
                    for cover in range( len(coverImgs) ):
                        hd = hammingDistance( secret[row][column],coverImgs[cover][row][column] )
                        if  hd == min : 
                            preDis = abs( int( secret[row][column] ) - int( coverImgs[similarCover][row][column] )  )
                            nowDis = abs( int( secret[row][column] ) - int( coverImgs[cover][row][column] )  )
                            if preDis > nowDis:
                                similarCover = cover
                            else:
                                continue
                        elif  hd < min : 
                            min = hd
                            similarCover = cover
                
                    similarPixel = secret[row][column] ^ coverImgs[similarCover][row][column]
                    
                    tmpXOR = tmpXOR ^ similarPixel ^ coverImgs[similarCover][row][column]
                    """    

                    for cover in range( len(coverImgs) ):
                            if abs( int( secret[row][column] ) - int( coverImgs[cover][row][column] )  ) < min:
                                min = abs( int( coverImgs[cover][row][column] ) - int( tmpXOR ^  coverImgs[cover][row][column] )  )
                                similarCover = cover
                    tmpXOR = tmpXOR ^ coverImgs[similarCover][row][column]
                    shareImgs[similarCover][row][column] = secret[row][column]
                    """
                    min = 999
                    for cover in range( len(coverImgs) ):
                        if cover != similarCover:
                            if abs( int( coverImgs[cover][row][column] ) - int( tmpXOR ^  coverImgs[cover][row][column] )  ) < min:
                                min = abs( int( coverImgs[cover][row][column] )  - int( tmpXOR ^  coverImgs[cover][row][column] )  )
                                lastCover = cover
                        
                    #avrpixel = 0 
                    """
                    if row > 0 and row < 510 and column > 0 and column < 510:
                        avrpixel = avrpixel +coverImgs[randcover][row-1][column-1] + coverImgs[randcover][row-1][column] + coverImgs[randcover][row-1][column+1]
                        avrpixel = avrpixel +coverImgs[randcover][row+1][column-1] + coverImgs[randcover][row+1][column] + coverImgs[randcover][row+1][column+1]
                        avrpixel = avrpixel +coverImgs[randcover][row][column-1] + secret[row][column] + coverImgs[randcover][row][column+1]
                        avrpixel = avrpixel // 9
                    """
                    
                    #tmpXOR = ( tmpXOR  ^ coverImgs[similarCover][row][column] ^ coverImgs[randcover][row][column]  ) 
                    # tmpXOR  = tmpXOR ^ secret[row][column]
                    #^ coverImgs[similarCover][row][column]
                    #shareImgs[randcover][row][column] = tmpXOR ^ secret[row][column]
                    shareImgs[lastCover][row][column] = tmpXOR ^  coverImgs[lastCover][row][column]
            
    

if __name__ == "__main__":

    coverImgs = []
    shareImgs = []
    
    cover4= initial("E:\\Visual Cryptograpyh\\input_image\\gray_baboon.png")
    
    s = initial("E:\\Visual Cryptograpyh\\input_image\\gray_lenna.png")

    secret = s.crateArray()
    outi = secret

    cover1 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_barbara.png")
    cover2 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_boat.png")
    cover5 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_butterfly.png")
    cover3 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_jet.png")

    coverImgs.append(cover1.crateArray())
    coverImgs.append(cover2.crateArray())
    coverImgs.append(cover3.crateArray())
    coverImgs.append(cover4.crateArray())
    coverImgs.append(cover5.crateArray())
    
    shareImgs.append(cover1.crateArray()) 
    shareImgs.append(cover2.crateArray()) 
    shareImgs.append(cover3.crateArray()) 
    shareImgs.append(cover4.crateArray()) 
    shareImgs.append(cover5.crateArray()) 


    result1 = algo(secret,coverImgs)

    beta = 1

    # 0.3 0.7 0.25 0.75
    for row in range(512):
            for column in range(512):
                a =random.random()

                if  a <=  beta  :
                    tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        
                        shareImgs[number][row][column] = tmp [number]

                else: 
                    randcover = random.randint(0,4)
                    tmpXOR = 0
                    for cover in range( len(coverImgs) ):
                        if cover == randcover:
                            pass
                        else:
                            tmpXOR = tmpXOR ^  coverImgs[cover][row][column]
                            
                    shareImgs[randcover][row][column] = tmpXOR
    
    outi = 0
    for i in range( len(shareImgs) ):
        aa = Image.fromarray( shareImgs[i] )
        aa.save(str( i ) +" algo2_0.75" +".png" ) 
        aa.show()

    for i in range ( len(shareImgs) ) :
        outi = outi ^ shareImgs[i]

    
    o = Image.fromarray(outi)
    o.save("output_algo2_0.75.png") 
    o.show()
    



    