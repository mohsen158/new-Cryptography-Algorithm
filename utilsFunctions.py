def test( ):
     
    return 4


def split(block):
    assert len(block)%3==0
    return block[0:8],block[8:16],block[16:24]
    # return inp[:int(len(inp)/2)], inp[int(len(inp)/2):]



def xor(word1,word2):
    res=[None] * len(word1)
    for i in range(len(word1)):
        res[i]=hex(int (word1[i],16)^int(word2[i],16)).split('x')[-1]
    return res