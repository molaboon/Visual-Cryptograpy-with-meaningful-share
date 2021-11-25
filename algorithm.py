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
    algo_2
    1.𝑀𝑛 ->𝑀𝑛 𝑜𝑑𝑑 & 𝑀𝑛 𝑒𝑣𝑒𝑛 
    2.ℎ𝑤(𝑀𝑛 (𝑖, 1: 𝑛)) = odd ,𝑀𝑛 (𝑖, 1: 𝑛) into the matrix 𝑀𝑛 𝑜𝑑𝑑 
    3. If 𝑆(𝑖,𝑗) = 0
    Randomly choose a row vector =  r 
    𝑅1 (𝑖,𝑗) = 𝑀𝑛 𝑒𝑣𝑒𝑛(𝑟, 1), … 𝑅𝑛 (𝑖,𝑗) = 𝑀𝑛 𝑒𝑣𝑒𝑛(𝑟, 𝑛) 

    If 𝑆(𝑖,𝑗) = 1
    Randomly choose a row vector =  r 
    𝑅1 (𝑖,𝑗) = 𝑀𝑛 odd(𝑟, 1), … 𝑅𝑛 (𝑖,𝑗) = 𝑀𝑛 odd(𝑟, 𝑛) 
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


class algo:
    def __init__(self, beta , Secret , Covers , nOfCovers ):
        self.beta = float ( beta )
        self.Secret = Secret
        self.covers = Covers 
        self.nOfCovers = nOfCovers
        self.even = [170,]
        
    def algo2(self,sPixel,nOfCovers,row,column):
        output = []

        r = random.randint( 0,255 ) 
        
        for cover in range( len (nOfCovers)-1 ):
            nOfCovers[cover][row][column] = nOfCovers[cover][row][column] ^ r
            output.append(nOfCovers[cover][row][column])

        
        theLastCover = sPixel 

        for cover in range( len(output) ): 
            theLastCover = theLastCover ^ output[cover]
        
        output.append(theLastCover)
        
        return output


if __name__ == "__main__":

    coverImgs = []
    shareImgs = []

    s = initial("E:\\Visual Cryptograpyh\\input_image\\gray_lenna.png")

    secret = s.crateArray()

    cover1 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_baboon.png")
    cover2 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_barbara.png")
    cover3 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_boat.png")
    cover4 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_butterfly.png")
    cover5 = initial("E:\\Visual Cryptograpyh\\input_image\\gray_tower.png")



    coverImgs.append(cover1.crateArray())
    coverImgs.append(cover2.crateArray())
    coverImgs.append(cover3.crateArray())
    coverImgs.append(cover4.crateArray())
    coverImgs.append(cover5.crateArray())

   


    result1 = algo(0.7,secret,coverImgs,5)

    for row in range(512):
        for column in range(512):
            a =random.random()

            if  a <  0.5  :
                tmp = result1.algo2( secret[row][column] , coverImgs , row, column)
                for number in range ( len( coverImgs ) ):
                    
                    coverImgs[number][row][column] = tmp [number]

            else:
                tmp = 0
                
                for cover in range( len( coverImgs ) ):
                    tmp = tmp ^ coverImgs[cover][row][column]
                
                if tmp % 2 == 0:
                    pass
                else:  
                    r = random.randint(  0 ,len( coverImgs )-1 )
                    coverImgs[r][row][column] =  coverImgs[r][row][column] ^ 255


    
    outi = coverImgs[0]
    for i in coverImgs:
        aa = Image.fromarray(i)
        aa.show() 


    for i in range (1 , 5) :
        outi = outi ^ coverImgs[i]


    o = Image.fromarray(outi)
    o.show() 

    



    