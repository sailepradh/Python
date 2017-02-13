#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open ('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.dna.chromosome.7.fa', 'r', encoding= 'utf-8') as DNA:
    lines_after_begin = DNA.readlines()[1:]
    sequence =[]

    for line in lines_after_begin:
        line  = line.strip()
        sequence.append(line)

    complete_list ="".join(sequence)

with open ('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.87.gtf', 'r', encoding = 'utf-8') as GTF:


    for line in GTF:
        if line.startswith ('#'):
            continue
        else:
            fields = line.split('\t')
            biotype = fields[2]
            chromosome = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            gene = fields[-1]


            if ("gene" == biotype) and ("7" == chromosome) and ("ENSG00000001626" in gene):
                (position1, position2) = (start+1, end)

with open ('CFTR.txt', 'w', encoding= 'utf-8') as fasta:
    fasta.write ((complete_list[slice(position1,position2)]))
