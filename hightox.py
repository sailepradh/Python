#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

sequence = []

# articles_df =  pd.read_table("/Users/salendrapradh/Desktop/database.txt", sep=',', header=0)

SNP_df = pd.read_table("/Users/salendrapradh/Desktop/Random_100000_SNP", header=0)

#print (SNP_df)

with open('/Users/salendrapradh/Desktop/HT_a11.txt', 'r', encoding='utf-8') as loopkup:
    for line in loopkup:
        line = line.strip()
        fields = line.split('\t')
        sequence.append(fields)
#print (sequence)

for (filenames,elements) in enumerate(sequence):
    print (filenames)
    print (elements)

#   specname = elements.split(",")
#   print (specname)
#   column1 = elements[0]
#   column2 = elements[1]
#   column3 = elements[2]

#    print (SNP_df[[0,1]])
    result = SNP_df[[elements[0],elements[1],elements[2],elements[3],elements[4],elements[5],elements[6],elements[7],elements[8],elements[9],elements[10],elements[11],elements[12],elements[13], elements[14],elements[15],elements[16],elements[17],elements[18],elements[19],elements[20],elements[21],elements[22],elements[23],elements[24],elements[25],elements[26],elements[27],elements[28],elements[29],elements[30],elements[31],elements[32],elements[33],elements[34],elements[35],elements[36],elements[37],elements[38],elements[39],elements[40],elements[41],elements[42],elements[43],elements[44],elements[45],elements[46],elements[47],elements[48],elements[49],elements[50]]]

    result.to_csv('example_%s.csv' % filenames, index=False, sep='\t', encoding='utf-8')
