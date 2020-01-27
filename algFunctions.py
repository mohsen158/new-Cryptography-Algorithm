import utilsFunctions as u
import constants as c
import sBoxes as sBoxes
from itertools import permutations
from keySchedule import generateKey


def f(word, keys):
    """
    this func is F function
    """
    word = int(word, 16)
    keyHex0 = u.intListToHexString(keys[0])
    keyHex1 = u.intListToHexString(keys[1])
    keyHex2 = u.intListToHexString(keys[2])

    # temp = sBoxes.s[0][word >> 24]

    # temp = (temp + sBoxes.s[1][word >> 16 & 0xff]) % 2**32

    # temp = u.xor(hex(temp).split('x')[-1], keyHex1)
    # temp = ''.join(temp)
    # temp = int(temp, 16)

    # temp = temp ^ sBoxes.s[2][word >> 8 & 0xff]
    # temp = (temp + sBoxes.s[3][word & 0xff]) % 2**32

    # return hex(temp).split('x')[-1].zfill(8)

    temp = sBoxes.s[0][word >> 24]
    temp = (temp ^ sBoxes.s[1][word >> 16 & 0xff])

    temp = u.xor(hex(temp).split('x')[-1], keyHex0)
    temp = ''.join(temp)
    temp = int(temp, 16)

    permIndex = temp & 0x7fff
    temp2 = sBoxes.s[3][word & 0xff] ^ sBoxes.s[2][word >> 8 & 0xff]

    temp2 = u.xor(hex(temp2).split('x')[-1], keyHex1)
    temp2 = ''.join(temp2)
    temp2 = int(temp2, 16)

    temp3 = (temp + temp2) % 2**32

    temp3 = u.xor(hex(temp3).split('x')[-1], keyHex2)
    temp3 = ''.join(temp3)
    temp3 = int(temp3, 16)

    hexTemp = hex(temp3).split('x')[-1].zfill(8)

    # permTemp = list(permutations(hexTemp))
    # permuted = ''. join(permTemp[permIndex])

    permuted = u.getPermuted(hexTemp, permIndex)
    # while temp <= 2**31 - 1:
    #     temp = temp << 1
    # while temp > 2**32 - 1:
    #     temp = temp >> 1
    return permuted


def decipher(block, key):
    keyes = generateKey(key)
    keyes.reverse()
    for i in range(12):
        temp = keyes[i*3]
        keyes[i*3] = keyes[i*3+2]
        keyes[i*3+2] = temp

    for r in range(c.Rounds-1):
        L, M, R = u.split(block)
        Lf = u.xor(M, f(L, keyes[r*3:r*3+3]))
        block = R+L+''.join(str(x) for x in Lf)
        # block = str(Lf)+str(R)+str(L)
    L, M, R = u.split(block)
    Lf = u.xor(M, f(L, keyes[(c.Rounds*3)-3:]))
    block = L+''.join(str(x) for x in Lf)+R
    return block


def cipher(block, key):
    """
    use splite func to splite 3 word
    use round func to cipher for 12 rounds
    """
    keyes = generateKey(key)
    for r in range(c.Rounds-1):
        L, M, R = u.split(block)
        Lf = u.xor(M, f(L, keyes[r*3:r*3+3]))
        block = ''.join(str(x) for x in Lf)+R+L
        # block = str(Lf)+str(R)+str(L)
    L, M, R = u.split(block)
    Lf = u.xor(M, f(L, keyes[(c.Rounds*3)-3:]))
    block = L+''.join(str(x) for x in Lf)+R
    return block
    # print(L+M,R)
    # print (u.split(block))
    # return ''
# def InvCipher


def encrypt(plaintext, key):
    """
    splite inpute text to 96 bits block
    use cipher func to cipher each block

    """
    ciphertext = ""
    # Split plaintext  into 96bit blocks
    plaintext = [plaintext[i: i + c.BLOCKSIZE_HEX]
                 for i in range(0, len(plaintext), c.BLOCKSIZE_HEX)]
    # refine last block with 0
    lengthOfLastBlock = len(plaintext[len(plaintext)-1])
    if (lengthOfLastBlock < c.BLOCKSIZE_HEX):
        for i in range(lengthOfLastBlock, c.BLOCKSIZE_HEX):
            plaintext[len(plaintext)-1] += '0'

    # print(lengthOfLastBlock)
    # TODO key generation things

    for block in plaintext:
        ciphertext += cipher(block, key)

    return ciphertext
# def decrypt():


def decrypt(ciphertext, key):
    """
    splite inpute text to 96 bits block
    use cipher func to cipher each block

    """
    plaintext = ""
    # Split plaintext  into 96bit blocks
    ciphertext = [ciphertext[i: i + c.BLOCKSIZE_HEX]
                  for i in range(0, len(ciphertext), c.BLOCKSIZE_HEX)]
    # refine last block with 0
    # lengthOfLastBlock = len(ciphertext[len(ciphertext)-1])
    # if ( lengthOfLastBlock < c.BLOCKSIZE_HEX):
    #     for i in range(lengthOfLastBlock, c.BLOCKSIZE_HEX):
    #         ciphertext[len(ciphertext)-1] += '0'

    # print(lengthOfLastBlock)
    # TODO key generation things

    for block in ciphertext:
        plaintext += decipher(block, key)

    return plaintext
