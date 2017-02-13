#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
In the following task we use GTF file to find further manipulation from the course as given in the website "https://nbisweden.github.io/PythonCourse/vt17/project"
'''

#  Question 1 ) How many transcripts

with open ('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.87.gtf', 'r', encoding= 'utf-8') as GTF:
    main = GTF.readlines()[5:]
    print (main)
