#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''

Following the question calaculating DNA length, we want to manipulate the GTF file to find the annotated  fields in the file
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
#    print (sum_1)


with open ('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.87.gtf', 'r', encoding= 'utf-8') as GTF:
    total_count = 0
    count_7 = 0
    len_all = 0
    sub = 0
    a = 0

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

            if "gene" == biotype:
                total_count = total_count + 1 ## gives me number of gene 58051


            if (("gene" == biotype) and ("7" == chromosome)):
                sub = int(end - start)
                len_all +=  sub


            if (("transcript" == biotype) and ("7" == chromosome) and "ENSG00000001626" in gene):
                #a= a+1
                print (end-start)
#    print (a)
#    print (total_count)
#    print (len_all, end ="\t")

#frac = len_all/sum_1

#print (frac)

## awk
#awk -F '[\t]' '{if ($1 == 7 && $3 == "gene") total +=$5- $4} END {print total}'  Homo_sapiens.GRCh38.87.gtf

