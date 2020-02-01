from utils.Rcon import Rcon
import sys


def generateKey(key):
    key = process_key(key, 3)
    expanded_key = KeyExpansion(key, 3, 3, 11)
    return expanded_key


def AddRoundKey(state, key):
    Nb = len(state)
    new_state = [[None for j in range(4)] for i in range(Nb)]

    for i, word in enumerate(state):
        for j, byte in enumerate(word):
            new_state[i][j] = byte ^ key[i][j]

    return new_state

def XORallState(w):
    res=0
    for word in w:
        for el in word:
            res=res^el
    return res
def XORallWordTogether(w):
    res=[0]*3
    for i in range(3):
        for word in w:
            res[i]=res[i]^word[i]
    return res

def KeyExpansion(key, Nb=4, Nk=3, Nr=10):
    w = []
    for word in key:
        w.append(word[:])

    i = Nk

    while i < Nb * (Nr + 1):
        temp = w[i-1][:]
        if i % Nk == 0:
            # temp = SubWord(RotWord(temp))
            XORed = XORallState(w)
            #temp[0] ^= Rcon[(i//Nk)]
            temp[0] ^= Rcon[(XORed%256)]
        # elif Nk > 6 and i % Nk == 4:
        #     temp = SubWord(temp)
        XORedWord=XORallWordTogether(w)
        for j in range(len(temp)):
            temp[j] ^= w[i-Nk][j]
        for n in range(3):
            temp[n]=temp[n]^XORedWord[n]
        w.append(temp[:])

        i += 1

    return w


def process_key(key, Nk=3):
    """
    total number of subkey in each round
    """
    try:
        key = key.replace(" ", "")
        return [[int(key[i*8+j*2:i*8+j*2+2], 16) for j in range(4)]
                for i in range(Nk)]
    except:
        print("Password must be hexadecimal.")
        sys.exit()
