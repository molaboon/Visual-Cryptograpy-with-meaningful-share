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

"""
    A.寫一個副程式 把其他4個SHARE(random share) 做計算 產出第五個SHARE 
    B.寫一個程式 做一個BIT
      做8次 產生一個灰階pixel
      再做五次 產生5個pixel
      再做XOR去做合成 jjjjjkkk
"""
"""
    Input: S & C(cover image), both with 𝐻 × 𝑊 pixels & a parameter β.

    d -> which is 1 with probability β and 0 with probability 1 −𝛽.
    If 𝑑 = 1, 𝑅1 (𝑖,𝑗), … , 𝑅𝑛 (𝑖,𝑗) = 𝐴𝑙𝑔_2((𝑛, 𝑛), 𝑆(𝑖,𝑗), 𝑀𝑛),
    If d = 0 , let 𝑡 = 𝑛 XOR C(𝑖,𝑗)
    If t = even , 𝑅1 (𝑖,𝑗) = 𝐶1 (𝑖,𝑗), … , 𝑅𝑛 (𝑖,𝑗) = 𝐶𝑛 (𝑖,𝑗); 
    If t = odd , randomly choose a number f form {1,…,n}
        𝑅1 (𝑖,𝑗) = 𝐶(𝑖,𝑗), … , 𝑅𝑓 (𝑖,𝑗) = 1− 𝐶f(𝑖,𝑗), … , 𝑅𝑛 (𝑖,𝑗) = 𝐶(𝑖,𝑗).

    Output: n meaningful shares 𝑅1,…, 𝑅𝑛, each of which is 𝐻 × 𝑊 in size
"""

"""
    三大方向:
    1. share 全不動
    2. 隨機挑一個cover跟 黑色做 XOR (做黑色)
    3. 隨機選擇 n-1 張 做XOR 在 ^S or black(去做計算，最後XOR出來變成黑色)
    4. 每一張都是share ,加密歸加密 (亂數*4 + 算第五張) 
"""

class algo:
    def __init__(self,  Secret , Covers ):
        self.Secret = Secret
        self.covers = Covers 

        
    def algo2(self,sPixel,Covers,row,column):
        output = []
        """
        randomX = random.randint( 0,255 ) 
        randomY = random.randint( 0,255 )
        """
        array2D = [ [0 for _ in range(8)] for _ in range(len(Covers)) ]

        """
        for cover in range( len (Covers) ):
            share[cover][row][column] = Covers[cover][row][column] ^ r
            output.append(share[cover][row][column])

        """

        ri = random.randint(0, len(Covers)-1 )
        secret = list( format(sPixel,"b") ) 

        while len(secret) < 8:
            secret.insert(0,"0")

        #share[ri][row][column] = tmpXOR 
        """
        for cover in range( len (Covers) ):
            if cover == ri:
                pass
            
            else:
                cXORrandint = Covers[cover][row][column] ^ Covers[cover][randomX][randomY]
                output.append(cXORrandint)
        
        for cover in range( 4 ):
            tmpXOR = tmpXOR ^  output[cover]
    
        output.insert(ri,tmpXOR)
        
        """
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
            
                    for cover in range( len(coverImgs) ):
                        if cover == randcover:
                            pass
                        else:
                            tmpXOR = tmpXOR ^  coverImgs[cover][row][column]
                            
                    shareImgs[randcover][row][column] = tmpXOR


if __name__ == "__main__":

    coverImgs = []
    shareImgs = []

    s = initial("E:\\Visual Cryptograpyh\\input_image\\gray_lenna.png")

    secret = s.crateArray()

    cover1 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_baboon.png")
    cover2 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_barbara.png")
    cover3 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_boat.png")
    cover4 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_butterfly.png")
    cover5 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_jet.png")

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

                
    """
        coverXOR = 0
                for cover in range(5):
                    coverXOR = coverXOR ^ coverImgs[cover][row][column]
        

        if coverXOR < 127 : 
                    
                    shareImgs[randcover][row][column] =  tmpXOR  
                
                else:
                    
                    shareImgs[randcover][row][column] = tmpXOR ^ 255

    """

    
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
    



    