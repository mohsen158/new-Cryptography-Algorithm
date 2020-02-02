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
import numpy as np
import constants as const
from pyfiglet import Figlet
from tqdm import trange
import time
f = Figlet(font='basic')


def allTests():

    encryptionDecryptinTest()
    res = ava.avalancheExecute()
    printAvalancheRes(res)
    randomSequenc = inputOrGenerateRandomSequenc(
        const.RANDOM_SEQUENCE_MAX_SIZE)
    nistTestsExec(randomSequenc)
    # Open Data File and read the binary data of e


def inputOrGenerateRandomSequenc(i):
    data_path = os.path.join(os.getcwd(), 'data', 'data.e')
    binary_data = ''
    if os.path.exists(data_path):
        handle = open(data_path)
        data_list = []
        for line in handle:
            data_list.append(line.strip().rstrip())
        binary_data = ''.join(data_list)
    else:
        binary_data = generateRandomeTestSample(i)
        f = open("data/data.txt", "a")
        f.write(binary_data)
        f.close()
    return binary_data.zfill(i)


def printAvalancheRes(res):
    values = np.array(res)
    min = values.min()
    max = values.max()
    mean = values.mean()
    print(' totla iteration is : ', const.MAX_TESTS_SIZE)
    print(' min value of avalance res is : ', min)
    print(' max value of avalance res is : ', max)
    print(' mean value of avalance res is : ', mean)
    if min > 0:
        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    else:
        print('\x1b[6;30;41m' + 'Fail!' + '\x1b[0m')

    pass


def encryptionDecryptinTest():
    print(f.renderText('Enc-Dec  test:'))
    randomPlainText = generateRandomePlainText()
    randomKeyText = generateRandomePlainText()

    print(' plain text is : \t \x1b[1;45;46m' + randomPlainText + '\x1b[0m')
    cipher = a.encrypt(randomPlainText, randomKeyText)
    print(' cipher  is : \t\t \x1b[1;45;48m' + cipher + '\x1b[0m')
    print(' decrypting ...')
    decipher = a.decrypt(cipher, randomKeyText)
    print(' decrypted  is : \t\t \x1b[1;47;42m' + decipher + '\x1b[0m')
    successText = '\x1b[6;30;42m' + 'Success!' + '\x1b[0m'
    failText = '\x1b[6;30;41m' + 'Fail!' + '\x1b[0m'
    if randomPlainText == decipher:
        print(successText)
    else:
        print(failText)
    pass


def generateRandomeTestSample(i):
    """
    this function generate array of bytes from encryption alg
    the output length is 1000 bit
    """
    randomPlainTextArray = [random.choice('0123456789abcdef')
                            for n in range(24)]
    randomPlainText = "".join(randomPlainTextArray)
    encryptText = randomPlainText
    randomBitsString = ''

    for n in trange(i):
        encryptText = a.encrypt(encryptText, const.KEY)
        randomBitsString = randomBitsString+(str(int(encryptText[23], 16) % 2))
    return randomBitsString


def nistTestsExec(randomSequence):
    print(f.renderText('NIST test:'))
    successText = '\x1b[6;30;42m' + 'Success!' + '\x1b[0m'
    failText = '\x1b[6;30;41m' + 'Fail!' + '\x1b[0m'
    print('The statistical test of the Binary Expansion of e')
    print('2.01. Frequency Test:\t\t\t\t\t\t\t\t',  successText if FrequencyTest.monobit_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.02. Block Frequency Test:\t\t\t\t\t\t\t',  successText if FrequencyTest.block_frequency(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.03. Run Test:\t\t\t\t\t\t\t\t\t\t',  successText if RunTest.run_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.04. Run Test (Longest Run of Ones): \t\t\t\t',  successText if RunTest.longest_one_block_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.05. Binary Matrix Rank Test:\t\t\t\t\t\t', successText if Matrix.binary_matrix_rank_text(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.06. Discrete Fourier Transform (Spectral) Test:\t', successText if SpectralTest.sepctral_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.07. Non-overlapping Template Matching Test:\t\t', successText if TemplateMatching.non_overlapping_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE], '000000001')[1] == True else failText)
    print('2.08. Overlappong Template Matching Test: \t\t\t', successText if TemplateMatching.overlapping_patterns(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.09. Universal Statistical Test:\t\t\t\t\t', successText if Universal.statistical_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.10. Linear Complexity Test:\t\t\t\t\t\t', successText if ComplexityTest.linear_complexity_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.11. Serial Test:\t\t\t\t\t\t\t\t\t', successText if Serial.serial_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.12. Approximate Entropy Test:\t\t\t\t\t\t', successText if ApproximateEntropy.approximate_entropy_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.13. Cumulative Sums (Forward):\t\t\t\t\t', successText if CumulativeSums.cumulative_sums_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE], 0)[1] == True else failText)
    print('2.13. Cumulative Sums (Backward):\t\t\t\t\t', successText if CumulativeSums.cumulative_sums_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE], 1)[1] == True else failText)
    result = RandomExcursions.random_excursions_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])
    print('2.14. Random Excursion Test:')
    print('\t\t STATE \t\t\t xObs \t\t\t\t P-Value \t\t\t Conclusion')

    for item in result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              successText if (item[4] >= 0.01) == True else failText)

    result = RandomExcursions.variant_test(
        randomSequence[:const.RANDOM_SEQUENCE_MAX_SIZE])

    print('2.15. Random Excursion Variant Test:\t\t\t\t\t\t')
    print('\t\t STATE \t\t COUNTS \t\t\t P-Value \t\t Conclusion')
    for item in result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              successText if (item[4] >= 0.01) == True else failText)
        pass


def generateRandomePlainText():
    """
    this function generate array of bytes from encryption alg
    the output length is 1000 bit
    """
    randomPlainTextArray = [random.choice('0123456789abcdef')
                            for n in range(24)]
    randomPlainText = "".join(randomPlainTextArray)
    return randomPlainText
