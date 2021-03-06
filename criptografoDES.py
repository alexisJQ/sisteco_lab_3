import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from time import time
from random import randint

# initial permutation Table for DES
initialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]

# inverse initial permutation Table for DES
inverseInitial = [ 40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25 ]

# Permutatin function for DES
permutationFunction = [ 16, 7, 20, 21,
                        29, 12, 28, 17,
                        1, 15, 23, 26,
                        5, 18, 31, 10,
                        2, 8, 24, 14,
                        32, 27, 3, 9,
                        19, 13, 30, 6,
                        22, 11,  4, 25 ]

#Expansion permutation for DES
expansionPermutation = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]

# definition of DES s-boxes
sBox =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
            
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
   
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
       
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
        
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
       
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
         
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
        
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

# Permutation choice one
permutationChoice1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4 ]

# Permutation choice 2
permutationChoice2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32 ]

# Number of bit shifts
shift = [1, 1, 2, 2,
        2, 2, 2, 2,
        1, 2, 2, 2,
        2, 2, 2, 1 ]

def str2bit(text):
    bits = ""
    for i in text:
        bits += '{0:08b}'.format(ord(i))
    return bits

def bit2str(bits):
    text = ""
    for i in range(int(len(bits) / 8)):
        text += chr(int(bits[i*8 : (i+1)*8], 2))
    return text

def shiftLeft(bits, n):
    shifted = ""
    for i in range(n):
        for j in range(1,len(bits)):
            shifted += bits[j]
        shifted += bits[0]
        bits = shifted
        shifted = ""
    return bits 

def permute(bits, table, nBits):
    permutation = ""
    for i in range(0, nBits):
        permutation += bits[table[i] - 1]
    return permutation

def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

def getKeys(key):
    roundKeys = []

    key = str2bit(key)
    key = permute(key, permutationChoice1, 56)
    
    leftKey = key[0:28]
    rightKey = key[28:56]

    for i in range(0, 8):
        
        leftKey = shiftLeft(leftKey, shift[i])
        rightKey = shiftLeft(rightKey, shift[i])

        combineKey = leftKey + rightKey

        roundKey = permute(combineKey, permutationChoice2, 48)
        roundKeys.append(roundKey)

    return roundKeys

def encrypt(block, roundKeys):

    bitBlock = str2bit(block)

    bitBlock = permute(bitBlock, initialPermutation, 64)

    leftBlock = bitBlock[0:32]
    rightBlock = bitBlock[32:64]

    for i in range(0, 8):

        rightExpanded = permute(rightBlock, expansionPermutation, 48)

        rightXOR = xor(rightExpanded, roundKeys[i])

        sBoxStr = ""
        for j in range(0, 8):
            row = int(rightXOR[j*6]+ rightXOR[j*6 + 5], 2)
            col = int(rightXOR[j*6 + 1] + rightXOR[j*6 + 2] + rightXOR[j*6 + 3] + rightXOR[j*6 + 4], 2)
            val = sBox[j][row][col]
            sBoxStr += '{0:08b}'.format(val)
        
        sBoxStr = permute(sBoxStr, permutationFunction, 32)

        result = xor(leftBlock, sBoxStr)
        leftBlock = result

        if (i != 7):
            leftBlock, rightBlock = rightBlock, leftBlock
    
    combine = leftBlock + rightBlock

    cipherText = permute(combine, inverseInitial, 64)
    cipherText = bit2str(cipherText)

    return cipherText
    
def testOfDES():
    key = "asdjgdjagd"
    encryptTime = []
    decryptTime = []
    sizePlainText = []
    sizeCipherText = []
    text = ""
    for i in range(10):

        cipherText = ""
        plainText = ""
        text += chr(randint(0, 255))

        sizePlainText.append(len(text))

        start = time()
        while len(text) % 8 != 0:
            text += ' '
        roundKeys = getKeys(key)

        for j in range(int(len(text)/8)):
            block = text[j*8:(j+1)*8]
            cipherText += encrypt(block, roundKeys)

        encryptTime.append(time()-start)
        sizeCipherText.append(len(cipherText))

        start = time()
        roundKeys = getKeys(key)
        roundKeysRev = roundKeys[::-1]
        for j in range(int(len(text)/8)):
            block = cipherText[j*8:(j+1)*8]
            plainText += encrypt(block, roundKeysRev)
        plainText = plainText.rstrip(" ")
        decryptTime.append(time()-start)

    return encryptTime, decryptTime, sizePlainText, sizeCipherText

def main():

    encryptTime, decryptTime, sizePlainText, sizeCipherText = testOfDES()
    plt.figure()
    plt.plot(np.array(sizePlainText), np.array(encryptTime))
    plt.xlabel('tama??o de la palabra')
    plt.ylabel('tiempo (s)')
    plt.title("tiempo de encriptaci??n")

    plt.figure()
    plt.plot(np.array(sizeCipherText), np.array(decryptTime))
    plt.xlabel('tama??o de la palabra')
    plt.ylabel('tiempo (s)')
    plt.title("tiempo de desincriptaci??n")
    plt.show()
    return

if __name__ == "__main__":
    main()
