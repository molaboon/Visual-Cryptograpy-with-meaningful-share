from PIL import Image 
import numpy as np
import random  
import os

from numpy.lib.function_base import select

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
        array2D = [ [0 for _ in range(8)] for _ in range(len(Covers)) ]

        ri = random.randint(0, len(Covers)-1 )
        secret = list( format(sPixel,"b") ) 

        while len(secret) < 8:
            secret.insert(0,"0")

        #share[ri][row][column] = tmpXOR 
        
        countBits = 0
        countCovers = ri

        while countBits < 8:
            array2D[countCovers][countBits] = secret[countBits]
            countBits += 1
            if countCovers ==  4 :
                countCovers = 0
            else:
                countCovers += 1


        for i in range( len(array2D) ):
            output.append( int( "".join(map(str, array2D[i]) ) , 2 ) )

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
    def method2(self):
        
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
    
    def method3(self):
        for row in range(512):
            for column in range(512):
                a =random.random()

                if  a <  beta  :
                    tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        
                        shareImgs[number][row][column] = tmp [number]

                else:
                    tmpXOR = 0
                    for cover in range( len(coverImgs) ):
                        tmpXOR = tmpXOR ^  coverImgs[cover][row][column]
                    
                    if tmpXOR == secret[row][column]:
                        pass
                    
                    else:
                        randcover = random.randint( 0 , len(coverImgs)-1 )
                        
                        tmpXOR = tmpXOR ^ coverImgs[randcover][row][column] ^ secret[row][column]

                        shareImgs[randcover][row][column] = tmpXOR


if __name__ == "__main__":

    coverImgs = []
    shareImgs = []

    s = initial("E:\\Visual Cryptograpyh\\input_image\\gray_lenna.png")

    secret = s.crateArray()

    cover5 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_baboon.png")
    cover1 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_barbara.png")
    cover2 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_boat.png")
    cover4 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_butterfly.png")
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

    beta = 0.8

    # 0.3 0.7 0.25 0.75

    for row in range(512):
            for column in range(512):
                a =random.random()

                if  a <  beta  :
                    tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                    for number in range ( len( coverImgs ) ):
                        
                        shareImgs[number][row][column] = tmp [number]

                else:
                    tmpXOR = 0
                    for cover in range( len(coverImgs) ):
                        tmpXOR = tmpXOR ^  coverImgs[cover][row][column]
                    
                    if tmpXOR == secret[row][column]:
                        pass
                    
                    else:
                        randcover = random.randint( 0 , len(coverImgs)-1 )
                        
                        tmpXOR = tmpXOR ^ coverImgs[randcover][row][column] ^ secret[row][column]

                        shareImgs[randcover][row][column] = tmpXOR
                        
    
    outi = 0
    for i in range( len(shareImgs) ):
        aa = Image.fromarray( shareImgs[i] )
        #aa.save(str( i ) + ".png" ) 
        aa.show()

    for i in range ( len(shareImgs) ) :
        outi = outi ^ shareImgs[i]


    o = Image.fromarray(outi)
    #o.save("output.png") 
    o.show()
    



    