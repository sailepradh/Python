#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Find the movie with the maximum number of votes from the given file of 250.imdb
'''

with open ('/Users/salendrapradh/Documents/Python_practise/Lessons/250.imdb', 'r') as movie:

    voting = 0
    best_title = ''

    for line in movie:

        # we check whethre it starts with # which is not interesting


        if line.startswith ('#'):
            #  ignore the line
            # print ('not interestd')
            pass
        else:
            # split the other with the | delimiters
            fields = line.split('|')

            tmp = int(fields[0])
            title = fields [-1]

            if tmp > voting:
                voting = tmp
                best_title = title
    # finally
    print (voting , best_title, end = "")