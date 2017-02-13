#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Find the movie with the maximum number of votes from the given file of 250.imdb
'''

with open ('/Users/salendrapradh/Documents/Python_practise/Lessons/250.imdb', 'r') as movie:

[]    final_list = []

    for line in movie:

        # we check whethre it starts with # which is not interesting


        if line.startswith ('#'):
            #  ignore the line
            # print ('not interestd')
            pass
        else:
            # split the other with the | delimiters
            fields = line.split('|')

            # tmp = float(fields[1])
            #title = fields [-1]
            genre = (fields [-2]).split(",")
            for g in genre:
                # i got one genre g
                if g in final_list:
                    pass
                else:
                    final_list.append(g)
        print (final_list)

'''             if 'Adventure' in genre:
                if tmp > voting:
                    voting = tmp
                    best_title = title
                if tmp < worst:
                    worst = tmp
                    worst_title= title
    # finally
    print ("Best:", voting , best_title, end = "")
    print ("Worst:", worst ,worst_title, end = "")
    '''