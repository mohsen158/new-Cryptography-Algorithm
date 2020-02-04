import os
from utils.permList import permList


def intListToHexString(intList):
    hexString = ''
    for i in intList:
        hexString = hexString+hex(i).split('x')[-1].zfill(2)
    return hexString


def split(block):
    assert len(block) % 3 == 0
    return block[0:8], block[8:16], block[16:24]
    # return inp[:int(len(inp)/2)], inp[int(len(inp)/2):]


def xor(word1, word2):
    """
    hex input
    hex output
    this xor is in hex mode
    """
    res = [None] * len(word1)
    for i in range(len(word1)):
        res[i] = hex(int(word1[i], 16) ^ int(word2[i], 16)).split('x')[-1]
    return res


def xorBinery(word1, word2):
    """
    bin input
    bin output
    this xor is in bin mode
    """
    return bin(int(word1, 2) ^ int(word2, 2))[2:].zfill(max(len(word1), len(word2)))


def getPermuted(hexString, i):
    """
    get positions and permute string like that 
    abcdefgh with 21346507 =>> cdegfah
    """
    permutedPosition = list(permList[i])
    permutedHexString = list('--------')
    for n in range(len(permutedPosition)):
        c = int(permutedPosition[n], 16)
        permutedHexString[n] = hexString[c]
    return ''.join(permutedHexString)


def bineryToHex(bin):
    return hex(int(bin, 2))[2:]


def hexToBinery(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex)*4)
