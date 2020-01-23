import sys
import os.path
import algFunctions as a


def demo():
    plaintext = "00112233445566778899aabbccddeeff"
    ciphertext = a.encrypt(plaintext, '')
    print(ciphertext)
    decipher = a.decrypt(ciphertext, '')
    print(decipher)


def main():

    demo()
    # if len(sys.argv) > 1 and sys.argv[1] == '-demo':
    #     demo()

    # if len(sys.argv) < 3:
    #     help()

    # mode = sys.argv[1]
    # ifile = sys.argv[2]

    # if mode not in ['-e', '-d'] or not os.path.exists(ifile):
    #     help()

    # try:
    #     with open(ifile, 'rb') as f:
    #         inf = f.read()
    # except:
    #     print ("Error while trying to read input file.")
    #     sys.exit()

    # Nb = 4
    # Nk = 4
    # Nr = 10

    # eggs = ''.join(sys.argv[3:])

    # spam = eggs.find('-c')
    # if spam > -1 and eggs[spam+2:spam+5] in ['128', '192', '256']:
    #     Nk = int(eggs[spam+2:spam+5])//32

    # Nr = Nk + 6

    # key = raw_input(
    #     "Enter a key, formed by {0} hexadecimal digits: ".format(Nk * 8))
    # key = key.replace(' ', '')

    # if len(key) < Nk * 8:
    #     print ("Key too short. Filling with \'0\',"
    #            "so the length is exactly {0} digits.".format(Nk * 8))
    #     key += "0" * (Nk * 8 - len(key))

    # elif len(key) > Nk * 8:
    #     print (
    #         "Key too long. Keeping only the first {0} digits.".format(Nk * 8))
    #     key = key[:Nk * 8]

    # key = process_key(key, Nk)

    # expanded_key = KeyExpansion(key, Nb, Nk, Nr)

    # if mode == '-e':
    #     ofile = ifile + '.aes'
    # elif mode == '-d' and (ifile.endswith('.aes') or ifile.endswith('.cif')):
    #     ofile = ifile[:-4]
    # else:
    #     ofile = raw_input('Enter the output filename: ')
    #     path_end = ifile.rfind('/')
    #     if path_end == -1:
    #         path_end = ifile.rfind('\\')
    #     if path_end != -1:
    #         ofile = ifile[:path_end+1] + ofile

    # if os.path.exists(ofile):
    #     spam = raw_input(
    #         'The file "{0}" already exists. Overwrite? [y/N] '.format(ofile))
    #     if spam.upper() != 'Y':
    #         ofile = raw_input('Enter new filename: ')

    # pb = ProgressBar(len(inf), 0)

    # output = None

    # if mode == '-e':  # Encrypt
    #     inf = padding(inf, Nb)

    # print('')
    # while inf:
    #     block, inf = get_block(inf, Nb)

    #     c = pb.update(len(inf))
    #     if c:
    #         pb.show()

    #     if mode == '-e':  # Encrypt
    #         block = Cipher(block, expanded_key, Nb, Nk, Nr)
    #     elif mode == '-d':  # Decript
    #         block = InvCipher(block, expanded_key, Nb, Nk, Nr)

    #     block = prepare_block(block)
    #     if output:
    #         output += block
    #     else:
    #         output = block

    # if mode == '-d':  # Decript
    #     output = unpadding(output, Nb)

    # with open(ofile, 'wb') as f:
    #     f.write(output)

    # print('')
    # sys.exit()


if __name__ == '__main__':
    main()
