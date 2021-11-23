from PIL import Image 
import numpy as np
import random  
import os

from numpy.lib.function_base import select

class initial:
    def __init__(self,imgURL) :
        self.img = Image.open(imgURL)
        #self.parameter = parameter
    def crateArray(self):
        imgArray = np.array(self.img)
        
        return imgArray

"""
    A.寫一個副程式 把其他4個SHARE(random share) 做計算 產出第五個SHARE 
    B.寫一個程式 做一個BIT
      做8次 產生一個灰階pixel
      再做五次 產生5個pixel
      再做XOR去做合成 
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
        self.beta = beta
        self.Secret = Secret
        self.covers = Covers 
        self.nOfCovers = nOfCovers
        
    def algo2(self,sPixel,nOfCovers):
        output = []

        if sPixel == 0:
            r = random.randrange(0,127) * 2
            
            for cover in range( len (nOfCovers) - 1 ):
                nOfCovers[cover] = nOfCovers[cover] ^ r 
                output.append(nOfCovers)

        else:
            r = random.randrange(1,255,2) 
            
            for cover in range( len(nOfCovers) - 1 ):
                nOfCovers[cover] = nOfCovers[cover] ^ r 
                output.append(nOfCovers)

        theLastCover = output[-1]

        for cover in range( len(output) ): 
            theLastCover = theLastCover ^ output[cover]
        
        output.append(theLastCover)

        return output


    def algo3(self,algo2Output):
        
        for row in range( 512 ):
            
            for column in range(512): 
                
                if random.random < self.beta:
                    
                    for number in range ( len(self.covers) ):
                        
                        self.Cover[number][row][column] = algo2Output[number]
                else:
                    tmp =  self.covers[0][row][column]
                    
                    for cover in range(1, len(self.covers) ):
                        tmp = tmp ^ self.covers[cover][row][column]
                    
                    if tmp % 2 == 0:
                        pass
                    else:  
                        r = random.randint( len( self.covers ) )
                        self.Cover[r][row][column] =  self.Cover[r][row][column] ^ 255

if __name__ == "__main__":

    coverImgs = []

    cover1 = initial("E:\\Visual Cryptograpyh\\input_image\\baboon.bmp")
    cover2 = initial("E:\\Visual Cryptograpyh\\input_image\\barbara.bmp")
    cover3 = initial("E:\\Visual Cryptograpyh\\input_image\\boat.bmp")
    cover4 = initial("E:\\Visual Cryptograpyh\\input_image\\bike2.bmp")
    cover5 = initial("E:\\Visual Cryptograpyh\\input_image\\pepper.bmp")

    coverImgs.append(cover1.crateArray())
    coverImgs.append(cover2.crateArray())
    coverImgs.append(cover3.crateArray())
    coverImgs.append(cover4.crateArray())
    coverImgs.append(cover5.crateArray())


    



    