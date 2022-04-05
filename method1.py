import random

def method1(coverImgs, row, column,shareImgs):
    randcover = random.randint(0,4)
    outPixel = 0
    for cover in range( len(coverImgs) ):
        if cover == randcover:
            pass
        else:
            outPixel = outPixel ^  coverImgs[cover][row][column]
            
    shareImgs[randcover][row][column] = outPixel

