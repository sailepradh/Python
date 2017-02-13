#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
ls
Following the question calaculating DNA length, we want to manipulate the GTF file to find the annotated  fields in the file
'''



with open ('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.87.gtf', 'r', encoding= 'utf-8') as GTF:

#     feature {}

    for line in GTF:

        if line.startswith ('#'):
             pass
        else:
            fields = line.split('\t')
            biotype = fields[2]
            chromosome = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            gene = fields[-1]


            if (("transcript" == biotype) and ("7" == chromosome) and "ENSG00000001626" in gene):

