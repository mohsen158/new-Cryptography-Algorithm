from nistTests.FrequencyTest import FrequencyTest
from nistTests.RunTest import RunTest
from nistTests.Matrix import Matrix
from nistTests.Spectral import SpectralTest
from nistTests.TemplateMatching import TemplateMatching
from nistTests.Universal import Universal
from nistTests.Complexity import ComplexityTest
from nistTests.Serial import Serial
from nistTests.ApproximateEntropy import ApproximateEntropy
from nistTests.CumulativeSum import CumulativeSums
from nistTests.RandomExcursions import RandomExcursions
import algFunctions as a
import os
import random
import avalanche as ava

def allTests():

    ava.avalancheExecute()
    # Open Data File and read the binary data of e
    data_path = os.path.join(os.getcwd(), 'data', 'data.e')
    if os.path.exists(data_path):
        handle = open(data_path)
        data_list = []
        for line in handle:
            data_list.append(line.strip().rstrip())
        binary_data = ''.join(data_list)
    else:
        generateRandomeTestSample()
    pass


def generateRandomeTestSample():
    """
    this function generate array of bytes from encryption alg 
    the output length is 1000 bit
    """
    randomPlainTextArray = [random.choice('0123456789abcdef')
                            for n in range(24)]
    randomPlainText = "".join(randomPlainTextArray)
    encryptText = randomPlainText
    randomBitsString = ''
    for n in range(3):
        encryptText = a.encrypt(encryptText, '')
        randomBitsString = randomBitsString+(str(int(encryptText[23], 16) % 2))
    pass

 

def nistTest():
    pass
