#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Find the movie with the maximum number of votes from the given file of 250.imdb
'''

with open ('/Users/salendrapradh/Documents/Python_practise/Lessons/250.imdb', 'r') as movie:

    final_list = []

    for line in movie:

        # we check whethre it starts with # which is not interesting


        if line.startswith ('#'):
            pass
        else:
            fields = line.split('|')
            tmp = float(fields[1])
            title = fields [-1]
            runtime = int(fields [3] )
            genre = (fields [-2]).split(",")
            print (genre.lower())
            # if (("drama" == genre.lower() ) and (runtime < (2*3600)) and (tmp > 8.7)):
            #     print  (title, end = "")
            #


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