#!/usr/bin/python
import string
def get_order(key):
    key = key.replace(' ', '')
    order = len(key) * [None]
    sorted_key = sorted(key)
    for i, ch in enumerate(sorted_key):
        order[i] = key.index(ch)
        key = key.replace(ch, 'z', 1) # string is immutable
#    print order
    return order

def transpose(message, key):
    message = message.replace(' ', '')
    order = get_order(key)
    mes_len = len(message)
    cols = len(key)
    rows = mes_len // cols + 1
    message = message + (' ' * (rows*cols - mes_len))
    str_list = [message[i:i+cols] for i in range(0, mes_len, cols)]
    print '\n'.join(str_list)
    newstr = ''
    for i in order:
        for s in str_list:
            newstr = newstr + s[i] 
    newstr = newstr.replace(' ', '')
    return newstr

# double transposition
def dt_cipher(message, key1, key2):
    newstr = transpose(message, key1)
    newstr = transpose(newstr, key2)
    print newstr

if __name__ == "__main__":
    # test case from http://users.telenet.be/d.rijmenants/en/handciphers.htm
    dt_cipher('WE CONFIRM THE DELIVERY OF THE DOCUMENTS X', 'ALADIN', 'CONSPIRACY')
