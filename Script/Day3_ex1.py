#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

##====================================================
## Reformat the 250.imdb into other format)
##====================================================


def format_category (c,movie):
    '''
    Takes the c = string  and  m = list of string  that is used to print in specific order
    '''
    test1 = '>' + c + '\n'
    test2 = '\n'.join(movie)
    return test1+test2

def format_title (title,year,rating,votes):
    '''This function takes the specific output from the imdb txt files
    :param title: title of the movie
    :param year: year the movie was released
    :param rating: imdb rating of movie
    :param votes: Votes casted by the viwer
    :return:
    '''
    newline = title + ';' + year + ';' + rating + ';' + votes
    return (newline)


with open ('/Users/salendrapradh/Documents/Python_practise/Lessons/250.imdb', 'r') as f_input, \
        open ('b.txt', 'w') as f_output:
    ## opened a file and write a result in b.txt

    ## Main data structure to get parse data in input files
    categories   =  {}

     f_output.write('#-* Category -*-# \n')
#    f_output.write('# > CATEGORY\n')
#    f_output.write('# Movie: Rating \t Name (Year) \n')



    for line in f_input:

        ## ignore the ones that are not interested
        if line.startswith('#'):
            continue

        ## Only ones that are intersested are
        fields = line.split('|')


        genres   = fields[-2].upper().split(',') ## List of the upper strings
        title   = fields[-1].strip()            ## strip so as to clean it
        year    = fields[2].strip()             ## clean it
        rating  = fields[1].strip()             ## clean it
        votes   = fields[0].strip()


        new_line = format_title(title,year,rating,votes) # transform it into new string

        for genre in genres:

            ## Getting the list of movies in the genre
            movies = categories.get(genre, [])
            #movies.append(new_line)
            #categories[genre] = movies

            if not movies:
                categories[genre] = [new_line]
            else:
                movies.append(new_line)


    for cat,movies in categories.items():

        fc = format_category (cat, movies)
        f_output.write( fc )
        f_output.write('\n')

        # f_output.write('#-* ')
        # f_output.write(cat)
        # f_output.write(' #-*')
        # f_output.write('\n')
        #
        #
        # for m in movies:
        #     f_output.write(m)
        #     f_output.write('\n')