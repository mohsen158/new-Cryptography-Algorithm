import algFunctions as a
import random
import constants as const
 


def avalancheExecute():
    avalancheTest= [[0 for i in range(96)]for n in range (96)]
    for i in range(const.MAX_TESTS_SIZE):
        basePlainText,baseCipheText = generateRandomeTestSample()
        oneStage =avalanchOneStage(basePlainText,baseCipheText)
        # oneStage= avalanchOneStage(avalancheTest,stage)
        avalancheTest = cumulative2Stages(avalancheTest,oneStage)
        print(i)
    print(avalancheTest)
    pass
def cumulative2Stages(main,stage):
    for i in range(96):
        for j in range(96):
            main[i][j]=main[i][j]+stage[i][j]
    return main       


def mixStages(mainStage , tempStage):
    pass
def avalanchOneStage(basePlainText,baseCipherText):
    """
    this function call in each stage of avalanche test 
    :baseCipherText cipher 
    """
    bineryBasePlainText=list(bin(int(basePlainText, 16))[2:].zfill(96))
    bineryBaseCipherText=list(bin(int(baseCipherText, 16))[2:].zfill(96))
    stage= [[0 for i in range(96)]for n in range (96)]
    for i in range(96):
        toggledBineryPlainText= toggleOneBit(bineryBasePlainText,i)
        toggledBineryPlainTextStr= ''.join(str(item) for item in toggledBineryPlainText)
        toggledBineryPlainTextHex=hex(int(toggledBineryPlainTextStr,2))[2:].zfill(24)
        encryptedToggledP=a.encrypt(toggledBineryPlainTextHex,const.KEY)
        bineryCipherToggled=list(bin(int(encryptedToggledP, 16))[2:].zfill(96))
        diff = dif(bineryBaseCipherText,bineryCipherToggled)
        for j in range(96):
            stage[i][j]=diff[j]
    return stage
    pass


def toggleOneBit(bin ,i):
    bin[i]=int(bin[i],2)^1
    return bin
def dif(baseCipherBin,cipherToggledBin):
    temp =[0]*96
    for i  in range(96):
        temp[i]=int(baseCipherBin[i],2) ^int(cipherToggledBin[i],2)
    return temp
        
    pass
def generateRandomeTestSample():
    """
    this function generate array of bytes from encryption alg 
    the output length is 1000 bit
    """
    randomPlainTextArray = [random.choice('0123456789abcdef')
                            for n in range(24)]
    randomPlainText = "".join(randomPlainTextArray)
 
    encryptText = a.encrypt(randomPlainText, '')
    return randomPlainText , encryptText

