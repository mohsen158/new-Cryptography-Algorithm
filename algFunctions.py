import utilsFunctions as u
import constants as c
import sBoxes as sBoxes


def f(word):
    """
    this func is F function
    """
    word = int(word, 16)
    temp = sBoxes.s[0][word >> 24]
    temp = (temp + sBoxes.s[1][word >> 16 & 0xff]) % 2**32
    temp = temp ^ sBoxes.s[2][word >> 8 & 0xff]
    temp = (temp + sBoxes.s[3][word & 0xff]) % 2**32
    while temp <= 2**31 - 1:
        temp = temp << 1
    while temp > 2**32 - 1:
        temp = temp >> 1
    return hex(temp).split('x')[-1]


def decipher(block, key):
    for r in range(c.Rounds-1):
        L, M, R = u.split(block)
        Lf = u.xor(M, f(L))
        block = R+L+''.join(str(x) for x in Lf)
        # block = str(Lf)+str(R)+str(L)
    L, M, R = u.split(block)
    Lf = u.xor(M, f(L))
    block = L+''.join(str(x) for x in Lf)+R
    return block


def cipher(block, key):
    """
    use splite func to splite 3 word
    use round func to cipher for 12 rounds
    """
    for r in range(c.Rounds-1):
        L, M, R = u.split(block)
        Lf = u.xor(M, f(L))
        block = ''.join(str(x) for x in Lf)+R+L
        # block = str(Lf)+str(R)+str(L)
    L, M, R = u.split(block)
    Lf = u.xor(M, f(L))
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
