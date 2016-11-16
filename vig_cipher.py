# coding: utf8
from pandas import DataFrame, set_option, reset_option
from collections import Counter
from re import sub
from math import log2
from time import time

ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '
ALPHABET_WS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def open_text(filename, w_spaces=False):
    with open(filename, 'r') as file:
        text_str = sub('[^%s]' % ALPHABET, '', sub('[ё]', 'е', file.read().lower()))

    return sub('[ ]', '', text_str) if w_spaces else sub(' {2,}', ' ', text_str)


def save_text(filename, string):
    with open(filename, 'w') as file:
        file.write(string)


def get_symbols_freq(string, get_letter=False):
    """
    Get dictionary of frequency of symbols

    :param string: text
    :param get_letter: return only the most frequent letter (bool)
    :return: Counter or letter
    """

    counter = Counter(string)
    return counter if not get_letter else counter.most_common(1)[0][0]


def get_bg_freq(string, step, show=False):
    """
    Get dictionary of frequencies of bigrams

    :param string: text
    :param step: cycle step (1 or 2)
    :param show: show frequencies in matrix with symbols indices (bool)
    :return: dictionary
    """

    f_dict = {}

    for i in range(0, len(string) - 1, step):
        if string[i] + string[i + 1] in f_dict:
            f_dict[string[i] + string[i + 1]] += 1
        else:
            f_dict[string[i] + string[i + 1]] = 1

    if show:
        df = DataFrame(data=0, index=ALPHABET, columns=ALPHABET)

        for i in f_dict:
            df.set_value(i[0], i[1], f_dict[i])

        set_option('display.max_columns', 10)
        print(df)
        reset_option('display.max_columns')

    return f_dict


def probability(f_dict, power):
    return {i: f_dict[i] / power for i in f_dict}


def get_entropy(p_dict, n):
    """
    Get the n-gram entropy
    H = - (Sum P * log2(P)) / N

    :param p_dict: dictionary of probabilities
    :param n: length of n-gram
    """

    entropy = -sum({i: p_dict[i] * log2(p_dict[i]) for i in p_dict}.values()) / n
    print('H' + str(n) + ' =', round(entropy, 4))


def affinity_index(f_dict, power):
    """
    Get affinity_index of the text
    I = (Sum F * (F - 1)) / (Power * (Power - 1))

    :param f_dict: dictionary of frequencies
    :param power: length of text
    """

    index = sum({i: f_dict[i] * (f_dict[i] - 1) for i in f_dict}.values()) / (power * (power - 1))
    print('I =', round(index, 6))


def get_cm_statistics(string, r):
    """
    Get character matches statistics

    :param string: text
    :param r: length of period
    """

    print('r =', r, 'D =', sum([1 if i == i + r else 0 for i in range(len(string) - r)]))


def encrypt(string, key):
    """
    Encrypt text by Vigenere cipher

    :param string: text
    :param key: str
    :return: cipher text
    """

    new_str = ''
    k = 0

    for i in range(len(string)):
        new_str += ALPHABET_WS[(ALPHABET_WS.index(string[i]) + ALPHABET_WS.index(key[k])) % len(ALPHABET_WS)]
        k = (k + 1) % len(key)

    return new_str


def decrypt(string, key):
    """
    Decrypt text from Vigenere cipher

    :param string: cipher text
    :param key: str
    :return: open text
    """

    new_str = ''
    k = 0

    for i in range(len(string)):
        new_str += ALPHABET_WS[(ALPHABET_WS.index(string[i]) - ALPHABET_WS.index(key[k])) % len(ALPHABET_WS)]
        k = (k + 1) % len(key)

    return new_str


def split_text(string, r):
    """
    Split text into segments by r period

    :param string: text
    :param r: period
    :return: list of segments
    """

    return [string[i::r] for i in range(r)]


def get_key_letter(x, y):
    """
    Get letter of key by formula x - y (mod m)

    :param x: most frequently letter in language
    :param y: most frequently letter in segment
    :return: letter of key
    """

    return ALPHABET_WS[(ALPHABET_WS.index(y) - ALPHABET_WS.index(x)) % len(ALPHABET_WS)]

if __name__ == '__main__':
    start = time()
    text = open_text('text_for_dec.in')

    # H1
    # get_entropy(probability(get_symbols_freq(text), len(text)), 1)

    # H2
    # f_big_dict = get_bg_freq(text, 1)
    # get_entropy(probability(f_big_dict, sum(f_big_dict.values())), 2)

    # Getting key
    '''key_d = ''

    for segment in split_text(text, 17):
        key_d += get_key_letter('о', get_symbols_freq(segment, get_letter=True))

    print(key_d)'''

    # Decrypting
    # save_text('text_decrypted.in', decrypt(text, 'возвращениеджинна'))

    print('Work time:', round(time() - start, 5), 's')
