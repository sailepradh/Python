#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def work (filename, option):

    with open (filename, 'rt', encoding =='utf-8') as f:

        line_counter = 0
        words_counter = 0
        chars_counter = 0


        for  line in f:
            line_counter += 1
            line =line.strip()

            if line  == '' or line.startswith(('#','/')):
                continue

            words = line.split(' ')
            words_counter += len(words)

            for words in words:
                chars_counter += len(words)

    if option == '--lines':
        s ='{0} contains {1} lines'.format(filename, line_counter)
        print (s)

    if option == '--words':
        s ='{0} contains {1} words'.format(filename, words_counter)
        print (s)

    if option == '--characters':
        s ='{0} contains {1} characters'.format(filename, chars_counter)
        print (s)

    if option is None:
        longline = '-' * 64
        print ("Filename : ", filename)
        print (longline)
        print ('|  Lines  |  Words |  Characters  |')
        print (longline)
        print (longline)
        print (longline)



def print_usages():

     print('''\
Usage: code.py <filename> [options]

Options are:
--------
--lines         displays the number of lines only
--words         displays the number of words only
--characters    displays the number of characters only

If no option is given, it displays all in a table like:


     Filename: <filename>
     -------------------------------------------
     |   Lines    |    Words   |  Characters   |
     -------------------------------------------
     |    12      |     345    |    67890      |
     -------------------------------------------

''')

if __name__ == '__main__':

    filename = None
    option =None

    if len (sys.argv) >= 2:
        filename =sys.argv[1]

    if len (sys.argv) >= 3:
        filenames =sys.argv[2]

    if not filename or option not in (
        '--lines'
        '--words'
        '--characters',
        None
    )


