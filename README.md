# Vigenere cipher
[![Code Climate](https://codeclimate.com/github/AverHLV/Vigenere_cipher/badges/gpa.svg)](https://codeclimate.com/github/AverHLV/Vigenere_cipher)

Vigenere cipher, encryption, decryption, cryptanalysis. Frequency analysis.

## Required modules
* pandas

## Usage
    # text = open_text('text_for_dec.in')
    
    # H1
    # get_entropy(probability(get_symbols_freq(text), len(text)), 1)

    # H2
    # f_big_dict = get_bg_freq(text, 1)
    # get_entropy(probability(f_big_dict, sum(f_big_dict.values())), 2)
    
    # Key length
    '''for i in range(6, 31):
        cm_statistics(text, i)'''

    # Getting key
    # deduce_key(text, 17)

    # Decrypting
    # save_text('text_decrypted.in', decrypt(text, 'возвращениеджинна'))