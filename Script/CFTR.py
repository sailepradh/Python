#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
The main aim of the task is to find the mutations in the CFTR sequencue of the gene.
We first downloaded the data into download folder and manipulating it with use of handler. In thr first part
of the question we first inputed CFTR in the termaina and foun the total nucleotuide length.
'''

with open ('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.dna.chromosome.7.fa', 'r', encoding= 'utf-8' ) as CFTR:
    lines_after_begin = CFTR.readlines()[1:]
    sum_1 = 0
    for line in lines_after_begin:
        line = line.strip()
        len_1 = len(line)
        #print (len_1)
        sum_1 += len_1
        #print (sum_1)
    print (sum_1)
