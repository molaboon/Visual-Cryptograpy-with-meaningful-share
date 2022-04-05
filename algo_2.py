import random

def algo2(sPixel,Covers,row,column):
    output = []
    randPixel = random.randint( 0,255 ) 
    randCover = random.randint(0, len(Covers)-1 )
    outPixel = sPixel
    for cover in range( len(Covers) ):
        if cover == randCover:
            pass
        else:
            outPixel = outPixel ^ Covers[cover][row][column]
    
    for cover in range( len (Covers) ):
        if cover == randCover:
            output.append(outPixel)
        else:
            cXORrandint = Covers[cover][row][column] ^ randPixel
            output.append(cXORrandint)
    
    return output
